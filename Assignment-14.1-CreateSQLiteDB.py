import sqlite3
import re
import os
from sqlite3 import Error

dbfile = "coursera_py.sqlite"
fname = "mbox.txt"
sql_create_table = 'CREATE TABLE Counts (org TEXT, count INTEGER)'
sql_insert_value = 'INSERT INTO Counts (org, count) VALUES (?,?)'
domains = {}

# make sure the database is re-created every time the program starts
if os.path.isfile(dbfile):
    try:
        os.remove(dbfile)
    except:
        print("Error while deleting file ", dbfile)

def open_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def execute_statement(conn, sql, params=None):
    try:
        cur = conn.cursor()
        if params is None: cur.execute(sql)
        else: cur.execute(sql, params)
    except Error as e:
        print(e)

my_db = open_connection(dbfile)

with my_db:
    # create table
    execute_statement(my_db, sql_create_table)

    fh = open(fname)

    for line in fh.readlines():
        line = line.lower().rstrip()
        domain = re.findall('^from.*?@(.*?)\s.*', line)

        if len(domain) == 0 :
            continue

        if domain[0] not in domains:
            domains[domain[0]] = 1
        else:
            domains[domain[0]] += 1

    for domain, count in domains.items():
        execute_statement(my_db, sql_insert_value, params=(domain, count))