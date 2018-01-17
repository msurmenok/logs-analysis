#!/usr/bin/python3
"""
Module to generate reports from a log file.

The report is answering three questions:
    - What are the most popular three articles of all time;
    - Who are the most popular article authors of all time;
    - On which days did more than 1% of requests lead to errors.
"""

import psycopg2

conn = psycopg2.connect("dbname=news user=vagrant")
cur = conn.cursor()


def print_report(list):
    """
    Print result in two columns where the second column is views.
    Attributes:
        results (list): result that contains at least two columns
    """
    for result in list:
        print(result[1] + " --- " + str(result[0]) + " views")
    print("\n-----------------------------------------------------\n")


# Query to find the most popular three articles of all time.
q1_query = "SELECT COUNT(*) AS views, articles.title " \
           "FROM log " \
           "JOIN articles ON log.path LIKE '%/' || articles.slug " \
           "GROUP BY articles.id " \
           "ORDER BY views DESC limit 3;"

# Query to find the most popular article authors of all time.
q2_query = "SELECT COUNT(*) AS views, authors.name " \
           "FROM log " \
           "JOIN articles ON log.path LIKE '%/' || articles.slug " \
           "JOIN authors ON articles.author =  authors.id " \
           "GROUP BY authors.id " \
           "ORDER BY views DESC;"

# Query to find days when more than 1% of requests lead to errors.
q3_query = "SELECT CAST(log.time AS DATE) AS log_date, COUNT(*) " \
           "FROM log " \
           "GROUP BY log_date " \
           "HAVING SUM(" \
           "CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END" \
           ") * 100 / COUNT(*) >= 1;"

# Execute queries and printing report.
cur.execute(q1_query)
results = cur.fetchall()
print("LOG ANALYSIS")
print("------------------------------------------------------\n")
print("1) The most popular three articles of all time:\n")
print_report(results)

cur.execute(q2_query)
results = cur.fetchall()
print("2) The most popular article authors of all time:\n")
print_report(results)

cur.execute(q3_query)
results = cur.fetchall()
print("3) Days when more than 1% of requests lead to errors:\n")
for result in results:
    print(result[0].strftime("%d %B %Y"))
print("\n------------------------------------------------------")
