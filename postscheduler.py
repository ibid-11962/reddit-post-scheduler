#!/usr/bin/python3
# post flair comment sticky

import praw
import datetime
import time
from praw.exceptions import APIException

f= open("postscheduler.log","a+")

#Credentials
reddit = praw.Reddit(client_id='',
					 client_secret='',
					 password='',
					 user_agent='postscheduler v.2b by /u/ibid-11962',
					 username='')


from postqueue import posts
###############################################################################
###############################################################################
###############################################################################

def submitPost(sub, title, text, link, image, video, parent, flairid, flairtext, collectionid, sort, commenttext, date, spoiler, nsfw, lock, contest, dontnotify, distinguish, sticky, lockcomment, distinguishcomment, stickycomment):
	currentDate = str(datetime.datetime.now().month) + "," + str(datetime.datetime.now().day)
	if date != currentDate:
		f.write("\n\ntoday is "+ currentDate+ "  --  post is scheduled for "+date)
		return 1
	if parent == None:
		try:
			if image == None and video == None:
				submission = reddit.subreddit(sub).submit(title, selftext=text, url=link, flair_id=flairid, flair_text=flairtext, send_replies=not(dontnotify), nsfw=nsfw, spoiler=spoiler, collection_id=collectionid)	
			else:
				if video == None:
					submission = reddit.subreddit(sub).submit_image(title, image_path=image, flair_id=flairid, flair_text=flairtext, send_replies=not(dontnotify), nsfw=nsfw, spoiler=spoiler, collection_id=collectionid)
				else:
					submission = reddit.subreddit(sub).submit_video(title, video_path=video, thumbnail_path=image, flair_id=flairid, flair_text=flairtext, send_replies=not(dontnotify), nsfw=nsfw, spoiler=spoiler, collection_id=collectionid)
					
			f.write("\n\nPosted --  "+ tolink(submission.url))
			
		except APIException as e:
			if e.field=="ratelimit":
				if wait==True:
					msg = e.message.lower()
					index=msg.find("minute")
					minutes = int(msg[index - 2]) + 1 if index != -1 else 1
					f.write("\n\nRatelimit reached. Waiting "+str(minutes)+" minutes before retrying.")
					time.sleep(minutes*60)
					return 5
				else:
					f.write("\n\nError posting submission -- "+str(e))
		except Exception as e:
			f.write("\n\nError posting submission -- "+str(e))
		try:
			if distinguish:
				submission.mod.distinguish()
				f.write("\nDistinguished")
			if sticky:
				submission.mod.sticky()
				f.write("\nStickied")
			if lock:
				submission.mod.lock()
				f.write("\nLocked")
			if contest:
				submission.mod.contest_mode()
				f.write("\nEnabled Contest Mode")
			if sort != None:
				submission.mod.suggested_sort(sort)
				f.write("\nSet suggested sort to "+sort)
		except Exception as e:
			f.write("\n\nError attributing submission. (Are you a moderator?) -- "+str(e))
	else:
		submission = reddit.comment(parent)

	if commenttext == None:
		return 2
		
	try:
		comment = submission.reply(commenttext)
		f.write("\n\tCommented --  "+ tolink(comment.permalink))
	except Exception as e:
		f.write("\n\tError posting comment -- "+str(e))
	try:
		if stickycomment:
			comment.mod.distinguish(how='yes', sticky=True)
			f.write("\n\tDistinguished and Stickied")
		elif distinguishcomment:
			comment.mod.distinguish(how='yes')
			f.write("\n\tDistinguished")
		if lockcomment:
			comment.mod.lock()
			f.write("\n\tLocked")
	except Exception as e:
		f.write("\n\tError attributing comment. (Are you a moderator?) -- "+str(e))
	return 0

def isdate(futureTime):
	currentTime = str(datetime.datetime.now().month) + "," + str(datetime.datetime.now().day)
	return futureTime == currentTime

def tolink(permalink):
	return "https://reddit.com" + permalink

#Main
if __name__ == "__main__":
	f.write("\n---------------------\nStarted")
	for post in posts:	
		postspecs = {"sub": "test", "title": "test", "text": "", "link": None, "image": None, "video": None, "parent": None, "flairid": None, "flairtext": None, "collectionid": None, "sort": None, "commenttext": None, "date": "7,23", "spoiler": False, "nsfw": False, "lock": False, "contest": False, "dontnotify": False, "distinguish": False, "sticky": False, "lockcomment": False, "distinguishcomment": False, "stickycomment": False}
		postspecs.update(post)
		err = submitPost(sub=postspecs["sub"], title=postspecs["title"], text=postspecs["text"], link=postspecs["link"], image=postspecs["image"], video=postspecs["video"], parent=postspecs["parent"], flairid=postspecs["flairid"], flairtext=postspecs["flairtext"], collectionid=postspecs["collectionid"], sort=postspecs["sort"], commenttext=postspecs["commenttext"], date=postspecs["date"], spoiler=postspecs["spoiler"], nsfw=postspecs["nsfw"], lock=postspecs["lock"], contest=postspecs["contest"], dontnotify=postspecs["dontnotify"], distinguish=postspecs["distinguish"], sticky=postspecs["sticky"], lockcomment=postspecs["lockcomment"], distinguishcomment=postspecs["distinguishcomment"], stickycomment=postspecs["stickycomment"])
		if err == 5:
			submitPost(sub=postspecs["sub"], title=postspecs["title"], text=postspecs["text"], link=postspecs["link"], image=postspecs["image"], video=postspecs["video"], parent=postspecs["parent"], flairid=postspecs["flairid"], flairtext=postspecs["flairtext"], collectionid=postspecs["collectionid"], sort=postspecs["sort"], commenttext=postspecs["commenttext"], date=postspecs["date"], spoiler=postspecs["spoiler"], nsfw=postspecs["nsfw"], lock=postspecs["lock"], contest=postspecs["contest"], dontnotify=postspecs["dontnotify"], distinguish=postspecs["distinguish"], sticky=postspecs["sticky"], lockcomment=postspecs["lockcomment"], distinguishcomment=postspecs["distinguishcomment"], stickycomment=postspecs["stickycomment"])
	f.write("\n\nFinished\n---------------------\n")
	f.close()
