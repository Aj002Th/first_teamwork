#  database.py
#  coding=gbk

import mysql.connector


def sql_connect():  # 建立和数据库的连接
    conn = mysql.connector.connect(user='root', password='', database='first_teamwork', buffered=True)
    cursor = conn.cursor()
    return conn, cursor


def save_add(username, student_nums):
    conn, cursor = sql_connect()

    sql = 'insert into `users` (`username`, `student_nums`) values (%s, %s)'
    cursor.execute(sql, (username, student_nums))

    conn.commit()
    cursor.close()
    conn.close()


def find_all_users():
    conn, cursor = sql_connect()

    sql = 'select `username` from `users`'
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data




