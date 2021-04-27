import sqlite3 as sl

# create/connect to the database named movies.db
con = sl.connect('movies.db')

# once you have a connection, you can create a cursor object and call its execute() mehtod to perform SQL commands
c = con.cursor()

# get the count of tables with the name
c.execute('''SELECT count(name) FROM sqlite_master WHERE type ='table' AND name='Movies' ''')

# if the count is 1, then table exists
if c.fetchone()[0]==1 :
    print('Table exists.')
else :
    # does not exists, create
    print('Table does not exist.')

    # create a table with a primary key, Movie_Name field of text, Genre field of text, and Release_Date field of text
    with con:
        con.execute("""
        CREATE TABLE Movies (
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Movie_Name TEXT,
            Genre TEXT,
            Release_Date TEXT
        );
    """)


        # create sql to insert data into the table
        sql = 'INSERT INTO Movies (ID, Movie_Name, Genre, Release_Date) values(?, ?, ?, ?)'
        data = [
            (1,'American Psycho','Drama','2000'),
            (2,'Inside Man','Drama','2006'),
            (3,'Dawn of the Dead','Horror','2004'),
            (4,'Mean Girls','Comedy','2004'),
            (5,'Avatar','Action','2009'),
            (6,'Armageddon','Sci-Fi','1998'),
            (7,'The Breakfast Club','Comedy','1985'),
            (8,'Die Hard','Action','1988'),
            (9,'Forrest Gump','Drama','1994'),
            (10,'Ghostbusters','Fantasy','1984')

        ]

        # run sql query
        with con:
            con.executemany(sql, data)

# connect and read back data
with con:
    data = con.execute("SELECT * FROM Movies WHERE Release_Date >= '2000'")
    for row in data:
        print(row)

with con:
    data = con.execute("SELECT * FROM Movies WHERE Release_Date < '2000'")
    for row in data:
        print(row)
