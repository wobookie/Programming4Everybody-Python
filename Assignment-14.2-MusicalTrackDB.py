import sqlite3
import re
import os.path
import xml.etree.ElementTree as ET
from sqlite3 import Error

dbfile = 'coursera_py_music.sqlite'
datafile = 'Library.xml'

# make sure the database is re-created every time the program starts
if os.path.isfile(dbfile):
    try:
        os.remove(dbfile)
    except:
        print("Error while deleting file ", dbfile)

# read in XML data
try:
    xml_doc = open(datafile).read()
    root = ET.fromstring(xml_doc)
except:
    print("Error while reading file ", datafile)
    exit()

print(xml_doc)

sql_create_tables = ('''CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );''',
    '''CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );''',
    '''CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );''',
    '''CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );''')

sql_insert_value = 'INSERT INTO Counts (org, count) VALUES (?,?)'

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
        print(sql, params)
        if params is None: cur.execute(sql)
        else: cur.execute(sql, params)
    except Error as e:
        print(e)
    return cur.lastrowid

my_db = open_connection(dbfile)



with my_db:
    # create tables
    for sql_create_table in sql_create_tables:
        execute_statement(my_db, sql_create_table)


    for artist in root.findall('.//count'):
