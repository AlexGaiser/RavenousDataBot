#! python3

#First Reddit Bot
#this bot is a prototype

import praw, time, pdb, re, os

import config

print('test start')

r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = 'FriendshipRobottest test friendship maker v0.1')



if not os.path.isfile('posts_replied_to.txt'):
	posts_replied_to = []
else:
	with open ("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

subreddit = r.subreddit('pythonforengineers')
x=0

for submission in subreddit.hot(limit = 60):
	
	if submission.id not in posts_replied_to:
		if re.search("test", submission.title, re.IGNORECASE):
			print('bot replying to: '+	submission.title)
			submission.reply('I am testing too! GREAT JOB FOR US!')
			posts_replied_to.append(submission.id)
			print('ID successfully added')
			with open ('posts_replied_to.txt', 'w') as f: 
				for post_id in posts_replied_to:
					f.write(post_id+"\n")
		else:
			print('nothing here')
	elif submission.id in posts_replied_to:
		print('already replied bro')
	x=x+1
	print(x)


