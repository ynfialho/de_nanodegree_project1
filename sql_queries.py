"""
Query centric script executed by ETL process.
"""
# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS fact_songplays"
user_table_drop = "DROP TABLE IF EXISTS dim_users"
song_table_drop = "DROP TABLE IF EXISTS dim_songs"
artist_table_drop = "DROP TABLE IF EXISTS dim_artists"
time_table_drop = "DROP TABLE IF EXISTS dim_time"

# CREATE TABLES
songplay_table_create = """
    CREATE TABLE fact_songplays(
    songplay_id SERIAL NOT NULL,
    start_time TIMESTAMP REFERENCES dim_time(start_time),
    user_id VARCHAR(50) REFERENCES dim_users(user_id),
    level VARCHAR(20),
    song_id VARCHAR(100) REFERENCES dim_songs(song_id),
    artist_id VARCHAR(100) REFERENCES dim_artists(artist_id),
    session_id INTEGER NOT NULL,
    location VARCHAR(255),
    user_agent TEXT,
    PRIMARY KEY (songplay_id))"""

user_table_create = """
    CREATE TABLE dim_users(
    user_id VARCHAR NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    gender VARCHAR(3),
    level VARCHAR(20),
    PRIMARY KEY (user_id))"""

song_table_create = """
    CREATE TABLE dim_songs(
    song_id VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    artist_id VARCHAR(100),
    year INTEGER,
    duration DOUBLE PRECISION,
    PRIMARY KEY (song_id))"""

artist_table_create = """
    CREATE TABLE dim_artists(
    artist_id VARCHAR(100) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    PRIMARY KEY (artist_id))"""

time_table_create = """
    CREATE TABLE dim_time(
    start_time TIMESTAMP,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER,
    PRIMARY KEY (start_time))"""

# INSERT RECORDS
user_table_insert = """
    INSERT INTO dim_users 
    (user_id, firstName, lastName, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) DO UPDATE SET 
    level = excluded.level """

song_table_insert = """
    INSERT INTO dim_songs 
    (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) 
    DO NOTHING;"""

artist_table_insert = ("""
    INSERT INTO dim_artists 
    (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) 
    DO NOTHING;""")

time_table_insert = """
    INSERT INTO dim_time 
    (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) 
    DO NOTHING;"""

songplay_table_insert = """
    INSERT INTO fact_songplays 
    (start_time, user_id, level, song_id, artist_id, session_id, 
    location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

# FIND SONGS BY ARTIST ID
song_select_join = """
    SELECT s.song_id, a.artist_id FROM dim_songs s, dim_artists a
    WHERE s.artist_id = a.artist_id  
        AND s.title = %s
        AND a.name = %s
        AND s.duration = %s"""


# QUERY LISTS
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,
                        songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
