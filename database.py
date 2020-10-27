import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXIST movies (
    title TEXT,
    release REAL,
    watched INTEGER
);
"""

INSERT_MOVIES = "INSERT INTO movies VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"

connection = sqlite3.connect("data.db")

def create_tables():
    pass


def add_movie(title, release):
    pass


def get_movies(upcoming=False):
    pass


def watch_movie(title):
    pass

def get_watched_movies():
    pass
