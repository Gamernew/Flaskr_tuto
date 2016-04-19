drop table if exists entries;
-- Create table entries with id, title and text
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
