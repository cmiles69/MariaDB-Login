#!/usr/bin/env python3
# coding = utf-8

# Original Credit: coderslegacy.com
# https://coderslegacy.com/python-tkinter-project-with-mysql-database/
# https://www.youtube.com/watch?v=SOU4TubaDf0

# This File
# Craig Miles: -> trocoxijaxe@gmail.com

# Module Imports
import mariadb
import sys

# Connect to MariaDB platform
def initialize_connection():
    try:
        conn = mariadb.connect(
            user = 'user1',
            password = 'password1',
            host = 'localhost' )

        # auto commit is on by default

    except mariadb.Error as e:
        print( f'Error connecting to MariaDB database: {e}' )
        sys.exit( 1 )

    cursor = conn.cursor()

    create_database( cursor )
    create_table( cursor )

    return( conn, cursor )

#=============================================================================

def create_database( cursor ):
    cursor.execute( '''SHOW DATABASES;''' )
    temp = cursor.fetchall()
    print( 'show databases temp is ->', temp )
    databases = [ item[0] for item in temp ]
    print( 'databases is ->', databases )


    if 'tutorial' not in databases:
        cursor.execute( '''CREATE DATABASE IF NOT EXISTS tutorial;''' )

    cursor.execute( '''USE tutorial;''' )
    cursor.execute( '''SELECT DATABASE();''' )
    print( 'Selected database is ->', cursor.fetchone())
   # print( 'cursor statement ->', cursor.statement )

#=============================================================================

def create_table( cursor ):
    cursor.execute( '''SHOW TABLES;''' )
    temp = cursor.fetchall()
    print( 'show tables temp is ->', temp )
    tables = [ item[0] for item in temp ]
    print( 'tables is ->', tables )

# AUTOINCREMENT Wrong! is -> AUTO_INCREMENT Grrrrr

    if 'users' not in tables:
        cursor.execute( '''CREATE TABLE IF NOT EXISTS users (
            id         INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
            firstname  VARCHAR( 100 ),
            lastname   VARCHAR( 100 ),
            pword      VARCHAR( 30 ),
            email      VARCHAR( 100 ) UNIQUE,
            gender     VARCHAR( 5 ),
            age        INTEGER,
            address    VARCHAR( 200 ),
            modified   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP );''' )

#=============================================================================

# Begin Program
# initialize_connection() # Uncomment to run once stand alone


