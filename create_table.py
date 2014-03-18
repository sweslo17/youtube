import sqlite3
conn = sqlite3.connect('video_log.db')
c = conn.cursor()
c.execute("CREATE TABLE log (videoId,date,viewcount,like,unlike)")
conn.commit()