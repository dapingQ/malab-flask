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
    return redirect(url_for('show_news'))
