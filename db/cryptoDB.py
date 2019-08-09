from pysqlcipher import dbapi2 as sqlcipher


def insert_user(table, user, pwd, mail):
    try:
        db = sqlcipher.connect("users.db")

        db.executescript('pragma key="testing"; pragma kdf_iter=64000;')
        db.execute('''CREATE TABLE IF NOT EXISTS ''' + table +
             '''(id INTEGER PRIMARY KEY AUTOINCREMENT, usr text, pwd text, email text)''')

        # Insert a row of data
        db.execute('INSERT INTO ' + table + '(usr, pwd, email) VALUES ("' + user + '", "' +
                   pwd + '", "' + mail + '");')
        rows = db.execute('select * from ' + table + ';').fetchall()
        db.commit()

    finally:
        db.close()

def get_random_user(table):
    try:
        db = sqlcipher.connect("users.db")
        db.executescript('pragma key="testing"; pragma kdf_iter=64000;')
        row = db.execute('SELECT * FROM ' + table + ' ORDER BY RANDOM() LIMIT 1;').fetchall()
        return row[0]
    finally:
        db.close()


def get_selected_user(table, user):
    try:
        db = sqlcipher.connect("users.db")
        db.executescript('pragma key="testing"; pragma kdf_iter=64000;')
        row = db.execute("select * from " + table + " where usr like '" + user + "' LIMIT 1").fetchall()
        return row[0]
    finally:
        db.close()

if __name__ == "__main__":
    insert_user("patatabrava", "anon", "example", "anon@gmail.com")
    a = get_random_user("patatabrava")
