import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) 
app.config.from_object(__name__) 

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'malab.db'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'd208d110'
    )
)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# database
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """connect the db """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# initialize db
@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialize the database.')

@app.route('/',methods=['GET'])
def show_entries():
    db = get_db()
    cur = db.execute('select title, author, context from news order by id desc')
    news_list = cur.fetchall()
    return render_template('index.html', news_list = news_list)

@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Please confirm your username.'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Please confirm your password.'
        else:
            session['logined_in'] = True
            return redirect(url_for('admin'))
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('/'))

@app.route('/admin')
def dashboard():
    # db = get_db()
    # cur = db.execute('select id, author, title from news order by id asc')
    # news_list = cur.fetchall()
    return render_template('admin/dashboard.html')


@app.route('/admin/news',methods=['GET'])
def show_news():
    db = get_db()
    cur = db.execute('select id, author, title from news order by id asc')
    news_list = cur.fetchall()
    return render_template('admin/admin-news.html', news_list=news_list)


@app.route('/admin/news/add',methods=['GET', 'POST'])
def add_news():
    db = get_db()
    db.execute('insert into news (title, author, context) values (?, ?, ?)', 
        [request.form['news-title'], request.form['news-author'], request.form['news-context']])
    db.commit()
    # return redirect(url_for('show_news'))
    return redirect(url_for('show_news'))

if __name__ == '__main__':
    app.run(debug=True)