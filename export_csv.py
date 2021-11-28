import csv
import psycopg2

username = 'Matvienko'
password = '111'
database = 'Matvienko_DB'

csv_out = 'Matvienko_DB_{}.csv'

TABLES = [
  'volcano',
  'eruption',
  'eruption_types'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
  cur = conn.cursor()

  for i in TABLES:
    cur.execute('SELECT * FROM ' + i)
    fields = [x[0] for x in cur.description]
    with open(csv_out.format(i), 'w') as outfile:
      csv.writer(outfile).writerow(fields)
      for row in cur:
        csv.writer(outfile).writerow([str(x) for x in row])