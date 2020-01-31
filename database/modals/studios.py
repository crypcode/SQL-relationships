from database.database import create_table_database


def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studioId INTEGER PRIMARY KEY AUTOINCREMENT,
                        studioName TEXT)"""
    create_table_database(query)


#create_studios_table()

def create_studio(Studio):
    query = """INSERT INTO studiod VALUES (?, ?)"""
    params = (Studio.studioId, Studio.name)
    query_database(query, params, True)

Studio1 = Studio(none, 'Marvel')
#create_studio(Studio1)

def get_studios(Studio):
    query = """SELECT * FROM studios WHERE studioId = (?) OR name = (?)"""
    params = (Studio.studioId, Studio.name)
    query_database(query, params, True)

# get_studios(Studio1)

def update_studios(Studio):

        query = """UPDATE studios SET name = 'whitefilms' WHERE name = (?) OR studioId = (?)"""
        parameters = (Studio.studioId, Studio.name)
        querry_database(query, parameters, True)


# update_studios(Studio1)

def delete_studios(Studio):
        query = """DELETE FROM genres WHERE genresId= (?) OR name = (?)"""
        parameters = (Studio.studioId, Studio.name)
        querry_database(query, parameters, True)


# delete_studios(Studio1)