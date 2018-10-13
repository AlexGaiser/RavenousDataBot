#! python3

#First Reddit Bot
#this bot is a prototype

import praw, time, pdb, re, os

import config_fbot

print('test start')

r = praw.Reddit(username = config_fbot.username,
				password = config_fbot.password,
				client_id = config_fbot.client_id,
				client_secret = config_fbot.client_secret,
				user_agent = 'FriendshipRobottest test friendship maker v0.1')


config_fbot.init()

config_fbot.replyDatabase()

posts_replied_to = config_fbot.posts_replied_to

subreddit = r.subreddit('pythonforengineers')
x=0
replycount = 0
for submission in subreddit.hot(limit = 60):
	
	if submission.id not in posts_replied_to:
		if re.search("test", submission.title, re.IGNORECASE):
			print('bot replying to: '+	submission.title)
			submission.reply('I am testing too! GREAT JOB FOR US!')
			posts_replied_to.append(submission.id)
			print('ID successfully added')
			replycount += 1
			with open ('posts_replied_to.txt', 'w') as f: 
				for post_id in posts_replied_to:
					f.write(post_id+"\n")

		else:
			print('nothing here')
	elif submission.id in posts_replied_to:
		print('already replied bro')
	x=x+1
	print(x)

print('successfully replied to ' + str(replycount) + ' comments')

