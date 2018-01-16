#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname=news user=vagrant")
cur = conn.cursor()


query = "select count(*) as views, path from log where path like '/article/%' group by path order by views desc limit 3;"

q1_query = "select count(*) as views, articles.title from log join articles on log.path like '%/' || articles.slug group by articles.id order by views desc limit 3;"
q2_query = "select count(*) as views, authors.name from log join articles on log.path like '%/' || articles.slug join authors on articles.author =  authors.id group by authors.id order by views desc;"
test_query = "select cast(log.time as date) as log_date, count(*) from log group by log_date order by count(*) desc limit 10;"
q3_query = "select cast(log.time as date) as log_date, sum(case when status = '404 NOT FOUND' then 1 else 0 end) as error_requests, count(*) as all_requests from log group by log_date having sum(case when status = '404 NOT FOUND' then 1 else 0 end)*100/count(*) >= 1;"
test_query = "select cast(log.time as date) as log_date, sum(case when status = '404 NOT FOUND' then 1 else 0 end) as error_requests, count(*) as all_requests from log group by log_date order by error_requests;"
cur.execute(q3_query)
results = cur.fetchall()
for result in results:
    print(result)

'''sum(case when code == 200 then 1 else 0 end) '''





