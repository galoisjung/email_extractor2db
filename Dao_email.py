import json

import pymysql
import sqlite3

with open('conf.json') as f:
    config = json.load(f)


class connection_sql:
    def __init__(self, spam=False):
        self.conn = pymysql.connect(host='localhost', user=config["SQL_ID"], passwd=config["SQL_PASSWORD"],
                                    db=config["DB"])

        if not spam:
            self.query_1 = '''
            CREATE TABLE IF NOT EXISTS ham(
            id INT PRIMARY KEY AUTO_INCREMENT,
            `from` LONGTEXT,
            `to` LONGTEXT,
            date VARCHAR(255),
            subject LONGTEXT NOT NULL,
            content LONGTEXT)
            '''
            self.query_2 = "INSERT INTO ham(`from`,`to`, date, subject, content) VALUES(%s,%s,%s,%s,%s)"
        else:
            self.query_1 = '''
            CREATE TABLE IF NOT EXISTS spam(
            id INT PRIMARY KEY AUTO_INCREMENT,
            `from` LONGTEXT,
            `to` LONGTEXT,
            date VARCHAR(255),
            subject LONGTEXT NOT NULL,
            content LONGTEXT)
            '''
            self.query_2 = "INSERT INTO spam(`from`,`to`, date, subject, content) VALUES(%s,%s,%s,%s,%s)"


class connection_sqlite:
    def __init__(self, spam=False):
        self.conn = sqlite3.connect("email.db")

        if not spam:
            self.query_1 = '''
            CREATE TABLE IF NOT EXISTS ham(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            `from` LONGTEXT,
            `to` LONGTEXT,
            date VARCHAR(255),
            subject LONGTEXT NOT NULL,
            content LONGTEXT)
            '''
            self.query_2 = "INSERT INTO ham(`from`,`to`, date, subject, content) VALUES(?,?,?,?,?)"
        else:
            self.query_1 = '''
            CREATE TABLE IF NOT EXISTS spam(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            `from` LONGTEXT,
            `to` LONGTEXT,
            date VARCHAR(255),
            subject LONGTEXT NOT NULL,
            content LONGTEXT)
            '''
            self.query_2 = "INSERT INTO spam(`from`,`to`, date, subject, content) VALUES(?,?,?,?,?)"


def add(email, conection, spam=False):
    con_instance = conection(spam)

    conn = con_instance.conn
    curs = conn.cursor()

    fm = email['From']
    to = email['To']
    date = email['Date']
    subject = email['Subject']
    content = email['Content']

    curs.execute(con_instance.query_1)
    conn.commit()

    curs.execute(con_instance.query_2, (fm, to, date, subject, content,))
    conn.commit()

    conn.close()


def ham_get():
    conn, curs = connection_sql()

    query = "SELECT subject FROM ham"

    curs.execute(query)
    conn.commit()

    result = curs.fetchall()

    label = [True] * len(result)

    result = zip(result, label)

    conn.close()

    return result


def spam_get():
    conn, curs = connection_sql()

    query = "SELECT subject FROM spam"

    curs.execute(query)
    conn.commit()

    result = curs.fetchall()

    label = [False] * len(result)

    result = zip(result, label)

    conn.close()

    return result
