from database.database import create_table_database


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        boxofficeId INTEGER PRIMARY KEY AUTOINCREMENT,
                        gross REAL)"""
    create_table_database(query)

#create_box_offices_table()

def create_box_office(BoxOffice):
    query = """INSERT INTO box_offices VALUES (?, ?)"""
    params = (BoxOffice.boxofficeId, BoxOffice.gross)
    query_database(query, params, True)

BoxOffice1 = BoxOffice(1, 990909)
#create_box_office(BoxOffice1)

def get_box_offices(BoxOffice1):
    query = """SELECT * FROM box_offices WHERE boxofficeId = (?) OR gross = (?)"""
    params = (BoxOffice.boxofficeId, BoxOffice.gross)
    query_database(query, params, True)

# get_box_offices(BoxOffice1)

def update_box_offices(BoxOffice1):

        query = """UPDATE box_offices SET gross = 9990909 WHERE gross = (?) OR boxofficeId= (?)"""
        parameters = (BoxOffice.boxofficeId, BoxOffice.gross)
        querry_database(query, parameters, True)


# update_box_offices(BoxOffice1)

def delete_box_offices(BoxOffice1):
        query = """DELETE FROM box_offices WHERE boxofficeId = (?) OR gross = (?)"""
        parameters = (BoxOffice.boxofficeId, BoxOffice.gross)
        querry_database(query, parameters, True)


# delete_box_offices(BoxOffice1)