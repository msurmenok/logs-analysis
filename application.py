#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname=news user=vagrant")
cur = conn.cursor()

# Query to find the most popular three articles of all time.
q1_query = "select count(*) as views, articles.title " \
           "from log " \
           "join articles on log.path like '%/' || articles.slug " \
           "group by articles.id " \
           "order by views desc limit 3;"

# Query to find the most popular article authors of all time.
q2_query = "select count(*) as views, authors.name " \
           "from log " \
           "join articles on log.path like '%/' || articles.slug " \
           "join authors on articles.author =  authors.id " \
           "group by authors.id " \
           "order by views desc;"

# Query to find days when more than 1% of requests lead to errors.
q3_query = "select cast(log.time as date) as log_date, count(*) " \
           "from log " \
           "group by log_date " \
           "having sum(" \
           "case when status = '404 NOT FOUND' then 1 else 0 end" \
           ") * 100 / count(*) >= 1;"

# Execute queries and printing report.
cur.execute(q1_query)
results = cur.fetchall()
print("LOG ANALYSIS")
print("------------------------------------------------------\n")
print("1) The most popular three articles of all time:\n")
for result in results:
    print(result[1] + " --- " + str(result[0]) + " views")
print("\n-----------------------------------------------------\n")

cur.execute(q2_query)
results = cur.fetchall()
print("2) The most popular article authors of all time:\n")
for result in results:
    print(result[1] + " --- " + str(result[0]) + " views")
print("\n------------------------------------------------------\n")

cur.execute(q3_query)
results = cur.fetchall()
print("3) Days when more than 1% of requests lead to errors:\n")
for result in results:
    print(result[0].strftime("%d %B %Y"))
print("\n------------------------------------------------------")
