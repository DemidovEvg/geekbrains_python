import sqlite3
# допустимые типы INTEGER, REAL, TEXT и BLOB.

con = sqlite3.connect(":memory:")
with con:
    cur = con.cursor()
    print(cur.description)
    request = """create table person(
        person_id integer primary key autoincrement unique,
        name text not null
    )"""
    cur.execute(request)
    request = """insert into person (name) values
    ('Bob'),
    ('Jon'),
    ('Den')"""
    cur.execute(request)
    con.commit
    request = """select * from person"""
    cur.execute(request)
    record = cur.fetchall()
    print(record)
    print(cur.description)

    cur.execute("create table lang (name, first_appeared)")
    # This is the qmark style:
    cur.execute("insert into lang values (?, ?)", ("C", 1972))
    # The qmark style used with executemany():
    lang_list = [
        ("Fortran", 1957),
        ("Python", 1991),
        ("Go", 2009),
    ]
    cur.executemany("insert into lang values (?, ?)", lang_list)
    # And this is the named style:
    cur.execute("select * from lang where first_appeared=:year", {"year": 1972})