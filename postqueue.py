###############################################################################
#Notes:
#every item is assumed None/False if left out
#everything is a string and should be entered in quotes except the following, which should just be the word True without quotes:
#	spoiler, nsfw, lock, contest, dontnotify, distinguish, sticky, lockcomment, distinguishcomment, stickycomment
#date is "M,D"
#text should be "" for an epmty title-only post
#image and video are pathstrings
#a videopost can use image to set a thumbnail
#link is a urlstring
#parent is a the ID of the comment or post you want to reply to (if not making a post)
#A lot of features will not work if you aren't a moderator

#link post:		date, sub, title, link
#text post:		date, sub, title, text
#title post:	date, sub, title
#image post:	date, sub, title, image
#video post:	date, sub, title, video, [image (for thumbnails)]
#comment:		date, parent, commenttext
#
#Every post (but not comment) can have flairs, collections, and sugessted sorts set using flairid, flairtext, collectionid, and sort.
#They can also have the following booleans set to True (without quotes): spoiler, nsfw, lock, contest, dontnotify, distinguish, sticky, wait
#
#wait doesn't change the post but will tell the scheduler to wait for any ratelimit to finish and retry a post before continuing.
#
#Every post can use the commenttext property to leave a comment under the post.
#If commenttext is used, then the following booleans can be set: lockcomment, distinguishcomment, and stickycomment
#
#Each post should be inside curly braces and seperated by commas. Each property should be designated with `"propertyname": property` and be seperated by commas. 

#examples

#{"sub": "pics",
#"title": "Monday Meme Megathread",
#"text": "**Please post all of your memes in this thread.**\n\rMemes found anywhere else will be removed.",
#"flairtext": "megathread",
#"sticky": True,
#"distinguish": True,
#"dontnotify": True,
#"comment": "[Here's a fun meme to start things off](https://i.imgur.com/97i2mJS.jpg)",
#"date": "9,30"}


posts = [

#---------------------#
{"sub": "subredditname",
"title": "titletext",
"text": "bodytext",
"commenttext": "commenttext",
"date": "8,11"},

#---------------------#

{"sub": "subredditname",
"title": "titletext",
"link": "linkurl",
"commenttext": "commenttext",
"date": "8,18"},

#---------------------#

{"sub": "subredditname",
"title": "titletext",
"image": "path/to/image",
"commenttext": "commenttext",
"date": "7,20"},

]
###############################################################################
