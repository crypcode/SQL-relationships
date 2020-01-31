from database.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)

def create_directors_movie_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        moviesId INTEGER,
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId),
                        directorsId INTEGER
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId))"""
    create_table_database(query)

#create_directors_table()
#create_directors_movie_table()

def create_director(Director):
    query = """INSERT INTO directors VALUES (?, ?)"""
    params = (Director.actorsId, Director.name)
    query_database(query, params, True)

Director1 = Director(1, 'Tarantino')
#create_director(Director1)

def get_directors(Director):
    query = """SELECT * FROM directors WHERE directorsId = (?) OR name = (?)"""
    params = (Director.directorsId, Director.name)
    query_database(query, params, True)

# get_directors(Director1)

def update_directors(Director):

        query = """UPDATE directors SET name = 'Kventinas' WHERE name = (?) OR directorsId = (?)"""
        parameters = (Director.directorsId, Director.name)
        querry_database(query, parameters, True)


# update_directors(Director1)

def delete_directors(Director):
        query = """DELETE FROM directors WHERE directorsId = (?) OR name = (?)"""
        parameters = (Director.directorsId, Director.name)
        querry_database(query, parameters, True)


# delete_directors(Director1)