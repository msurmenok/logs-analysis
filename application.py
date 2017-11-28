#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname=news user=vagrant")
cur = conn.cursor()


query = "select count(path) as views, path from log where path like '/article/%' group by path order by views desc limit 3;"

cur.execute(query)
str = cur.fetchall()
print(str)





