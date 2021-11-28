import csv
import psycopg2

username = 'Matvienko'
password = '111'
database = 'Matvienko_DB'
host = 'localhost'
port = '5432'


INPUT_CSV_FILE = 'volcano_db.csv'

query_0 = '''
create table volcanic (
    volc_number int PRIMARY KEY NOT NULL,
    volc_name character varying(40) NULL,
    volc_country character varying(50) NULL
)
'''

query_1 = '''
DELETE FROM volcanic
'''

query_2 = '''
INSERT INTO volcanic (volc_number, volc_name, volc_country) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute('drop table if exists volcanic')
    cur.execute(query_0)
    cur.execute(query_1)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (row['Number'], row['Name'], row['Country'])
            cur.execute(query_2, values)
    conn.commit()