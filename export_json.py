import json
import psycopg2

username = 'Matvienko'
password = '111'
database = 'Matvienko_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
  cur = conn.cursor()
  TABLES = [
    'volcano',
    'eruption',
    'eruption_types'
  ]
  for i in TABLES:
    cur.execute('SELECT * FROM ' + i)
    rows = []
    fields = [x[0] for x in cur.description]
    for row in cur:
      rows.append(dict(zip(fields, row)))
    data[i] = rows

with open('Matvienko_all.json', 'w') as json_out:
  json.dump(data, json_out, default=str)