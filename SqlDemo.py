import sqlite3
from SpotifyAPI import GetSong
import json


conn = sqlite3.connect('spotify.db')


c = conn.cursor()

# c.execute("""DROP Table playlist""")

# c.execute("""CREATE TABLE playlist (
#     playlistLink TEXT,
#     plalistName TEXT 
# )""")

# c.execute("""INSERT INTO playlist VALUES ('www.testlink2.com','testplaylist2')""")

with open('spotifyplaylist.json') as f:
    data = json.load(f)
print(data)

# c.execute("SELECT * FROM playlist")

#GetSong()

# print(c.fetchone())


conn.commit()

conn.close()