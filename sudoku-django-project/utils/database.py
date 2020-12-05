"""Functions to initially populate the database.
Uses mysql-connector-python instead of the Django ORM."""

import classes
import mysql.connector as sql

def get_connection_details() -> dict:
    """Open file containing database credentials that Django uses, and returns in the form of a dictionary"""
    with open(r"sudoku-django-project\sudoku\my.cnf", "r") as f:
        details = {}
        a = f.readlines()
        a.pop(0)
        for line in a:
            line = line.strip().split("=")
            key, value = map(str.strip, line)
            details[key] = value
    return details

def mock_leaderboard_values(cnx: sql.MySQLConnection) -> None:
    """Used to fill database with mock values for testing.
        Leaderboard table is in the form:
            id - auto generated integer
            name - CHAR(20)
            Time - INT in seconds.
        All names in this is suffixed with the word `mock` so that they can be easily deleted."""
    cursor = cnx.cursor()
    test_values = [
        (None, "bruh_mock", 35),
        (None, "damn_mock", 123),
        (None, "oof_mock", 69), 
        (None, "shriram_mock", 420),
        (None, "cs_mock", 1323),
        (None, "pretkejk_mock", 989),
        (None, "risab_mock", 9),
        (None, "john_mock", 122),
        (None, "i_mock", 123),
        (None, "cant think_mock", 32),
        (None, "new names_mock", 54)
    ]
    try:
        cursor.executemany("INSERT INTO mainapp_leaderboard", test_values)
        cnx.commit()
    except Exception as e:
        print(str(e))
    
def clean_leaderboard(cnx: sql.MySQLConnection, mock: bool = True) -> None:
    """Used to clear data from leaderboard. Set mock=False if you want to clear all data in the table"""
    cursor = cnx.cursor()

    if mock is True:
        statement = "DELETE FROM mainapp_leaderboard WHERE name LIKE '%mock%'"
        out = "Deleted all mock values."
    else:
        statement = "DELETE FROM mainapp_leaderboard"
        out = "Deleted all values."
    cursor.execute(statement)
    cnx.commit()

    print(out)
    return 
