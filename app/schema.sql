drop table if exists members;
create table members (
  id integer primary key autoincrement,
  name text not null,
  e-mail text not null,
  school text not null
);

