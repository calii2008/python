import sqlite3

from matplotlib.pyplot import connect
from module import movie , MovieCreate
from streamlit import connection


def create_conection():
    """create a database connection"""
    connection = sqlite3.connect("movie.db")
    connection.row_factory = sqlite3.now
    return connection

def create_table():
    """create tabels if they dont exite"""
    connection = create_conection()
    cursor = connection.execute("""
    createn tabel if dont exist movies(
    id integer primary kay autoincnt,
    title text not null
    
    
    
    
    """)