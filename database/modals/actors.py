from database.database import create_table_database, query_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actors_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actorsId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


#create_actors_table()
#create_actors_movies_table()

#query_database("PRAGMA table info(movies)")

def create_actor(Actor):
    query = """INSERT INTO actors VALUES (?, ?)"""
    params = (Actor.actorsId, Actor.name)
    query_database(query, params, True)

Actor1 = Actor(1, 'Lenis')
#create_actor(Actor1)

def get_actors(Actor):
    query = """SELECT * FROM actors WHERE actorsId = (?) OR name = (?)"""
    params = (Actor.actorsId, Actor.name)
    query_database(query, params, True)

# get_movie(Actor1)

def update_actors(Actor):

        query = """UPDATE actors SET name = 'Vandamas' WHERE name = (?) OR actorsId = (?)"""
        parameters = (Actor.actorsId, Actor.name)
        querry_database(query, parameters, True)


# update_movie(Actor1)

def delete_actor(Actor):
        query = """DELETE FROM actors WHERE actorsId = (?) OR name = (?)"""
        parameters = (Actor.actorsId, Actor.name)
        querry_database(query, parameters, True)


# delete_actor(Actor1)
