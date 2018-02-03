import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, descr text, link text, user integer, pwd integer, note text)")
        self.conn.commit()

    def insert(self, descr, link, user, pwd, note):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)", (descr, link, user, pwd, note))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, descr="", link="", user="", pwd="", note=""):
        self.cur.execute("SELECT * FROM book WHERE descr=? OR link=? OR user=? OR pwd=? OR note=?", (descr, link, user, pwd, note))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, descr, link, user, pwd, note):
        self.cur.execute("UPDATE book SET descr=?, link=?, user=?, pwd=?, note=? WHERE id=?", (descr, link, user, pwd, note, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#insert("The Sun","John Smith",1918,913123132)
# delete(3)
#update(4,"The moon","John Smooth",1917,99999)
# print(view())
#print(search(link="John Smooth"))
