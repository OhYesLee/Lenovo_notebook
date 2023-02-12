import sqlite3
import time



def get_blog_list():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog")
    result = c.fetchall()
    conn.close()
    return result


def add_blog(subject, content):         # 제목, 내용
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    today = time.strftime('%Y%m%d')     # 현재 시간
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)",
        (subject, content, today))
    conn.commit()
    conn.close()


def read_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM blog WHERE id=?", (_id,))
    result = c.fetchone()
    conn.close()
    return result


def modify_blog(_id, subject, content):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE blog SET subject=?, content=? WHERE id=?",
        (subject, content, _id))
    conn.commit()
    conn.close()


def remove_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("DELETE FROM blog WHERE id=?", (_id,))
    conn.commit()
    conn.close()

