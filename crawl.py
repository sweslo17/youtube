import requests
import datetime
import time
import sqlite3
conn = sqlite3.connect('video_log.db')
c = conn.cursor()
last = datetime.datetime.now()
def get_data(date,videoId):
	data = requests.get("https://gdata.youtube.com/feeds/api/videos/"+videoId+"?v=2&alt=json").json()
	like = int(data['entry']['yt$rating']['numLikes'])
	unlike = int(data['entry']['yt$rating']['numDislikes'])
	print str(date) + ": ('%s','%s','%s','%s','%s')" % (videoId,date,None,like,unlike)
	c.execute("INSERT INTO log (videoId,date,viewcount,like,unlike) VALUES ('%s','%s','%s','%s','%s')" % (videoId,date,None,like,unlike))
	conn.commit()

if __name__ == "__main__":
	get_data(last,"rm5kI7X6sJ0")
	get_data(last,"yj9Dy0IMmi0")
	
	#print (datetime.datetime.now()-last).total_seconds()
	while True:
		if (datetime.datetime.now()-last).total_seconds() > 300:
			last = datetime.datetime.now()
			get_data(last,"rm5kI7X6sJ0")
			get_data(last,"yj9Dy0IMmi0")
		else:
			time.sleep(5)