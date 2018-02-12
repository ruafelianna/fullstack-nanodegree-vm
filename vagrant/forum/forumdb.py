# "Database code" for the DB Forum.

import psycopg2 as pg

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = pg.connect("dbname=" + DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc;")
  data = c.fetchall()
  db.close()
  return data

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = pg.connect("dbname=" + DBNAME)
  c = db.cursor()
  c.execute('''insert into posts values ('%s');''' % content)
  db.commit()
  db.close()

