from database.database import create_table_database


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)

def create_genres_movies_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genresId INTEGER,
                        FOREIGN KEY (genresId) REFERENCES genres(genresId),
                        moviesId INTEGER,
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId)))"""
    create_table_database(query)

#create_genres_table()
#create_genres_movies_table()

def create_genres(Genre):
    query = """INSERT INTO genres VALUES (?, ?)"""
    params = (Genre.genresId, Genre.name)
    query_database(query, params, True)

Genre1 = Genre(none, 'Veiksmo')
#create_genres(Genre1)

def get_genres(Genre):
    query = """SELECT * FROM genres WHERE genresId = (?) OR name = (?)"""
    params = (Genre.genresId, Genre.name)
    query_database(query, params, True)

# get_genres(Genre1)

def update_genres(Genre):

        query = """UPDATE directors SET name = 'Komedija' WHERE name = (?) OR genresId = (?)"""
        parameters = (Genre.genresId, Genre.name)
        querry_database(query, parameters, True)


# update_genres(Genre1)

def delete_genres(Genre):
        query = """DELETE FROM genres WHERE genresId= (?) OR name = (?)"""
        parameters = (Genre.genresId, Genre.name)
        querry_database(query, parameters, True)


# delete_genres(Genre1)