import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        print(type(row[idx]))
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect(":memory:")
con.row_factory = dict_factory
cur = con.cursor()
request = """create table person(
        person_id integer primary key autoincrement unique,
        name text not null
    )"""
cur.execute(request)
request = """insert into person (name) values
    ('Bob'),
    ('Jon')"""

cur.execute(request)
cur.execute("select * from person")
print(cur.fetchall())
# print(cur.fetchone()["name"])

con.close()