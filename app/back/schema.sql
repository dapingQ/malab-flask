drop table if exists news;
create table news (
  id integer primary key autoincrement,
  title text not null,
  author text not null,
  context text not null
);

