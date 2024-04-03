import logging
import sqlite3


def get_logger():
    return logging.getLogger(__name__)


logging.basicConfig(level=logging.INFO, format='%(name)s - %(message)s       level: %(levelname)s')
conn = sqlite3.connect('Data Base.db')
c = conn.cursor()


def create_connection():
    global conn
    global c
    conn = sqlite3.connect('Data Base.db')
    c = conn.cursor()


def delete_connection():
    global conn
    conn.commit()
    conn.close()


def create_table():
    create_connection()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
    id        INTEGER PRIMARY KEY
                      UNIQUE
                      NOT NULL,
    isPremium INTEGER NOT NULL
                      DEFAULT (0),
    username  TEXT    DEFAULT 'user'
);''')

    delete_connection()
    get_logger().log(level=logging.INFO, msg="Has the table been created or does it exist")


def add(id_telegram: int, username: str):
    create_connection()

    if len(c.execute('''SELECT * FROM users WHERE id = {id};'''.format(id=id_telegram)).fetchall()) == 0:
        c.execute('''INSERT INTO users(id) VALUES ({id});'''
                  .format(id=id_telegram))
        get_logger().log(level=logging.INFO, msg="The user has been added")
    else:
        c.execute('''UPDATE users SET username = '{username}' WHERE id = {id};'''
                  .format(username=username, id=id_telegram))
        get_logger().log(level=logging.INFO, msg="The user has been updated")

    delete_connection()


def delete(id_telegram: int):
    create_connection()

    if len(c.execute('''SELECT * FROM users WHERE id = {id};'''.format(id=id_telegram)).fetchall()) != 0:
        c.execute('''DELETE FROM users WHERE id = {id};'''.format(id=id_telegram))
        get_logger().log(level=logging.INFO, msg="The user has been deleted")

    delete_connection()


def set_premium(id_telegram: int, premium: bool):
    create_connection()

    if len(c.execute('''SELECT * FROM users WHERE id = {id};'''.format(id=id_telegram)).fetchall()) != 0:
        c.execute('''UPDATE users SET isPremium = {is_premium} WHERE id = {id};'''
                  .format(is_premium=premium, id=id_telegram))
        if premium:
            get_logger().log(level=logging.INFO, msg="Premium added")
        else:
            get_logger().log(level=logging.INFO, msg="Premium removed")

    delete_connection()


conn.close()
