#! python3

#First Reddit Bot
#this bot is a prototype

import config_fbot
import praw, time, pdb, re, os
print('test start')

config_fbot.init()

config_fbot.replyDatabase()

posts_replied_to = config_fbot.posts_replied_to


r = praw.Reddit(username = config_fbot.username,
					password = config_fbot.password,
					client_id = config_fbot.client_id,
					client_secret = config_fbot.client_secret,
					user_agent = 'FriendshipRobottest test friendship maker v0.2')
	
subreddit = r.subreddit('test')


x=0
for submission in subreddit.hot(limit = 5):
	#try:
		if submission.id not in posts_replied_to:
			if 'test' in submission.body:
				print('friend found')
				submission.reply('Testing as well I see. Good luck my friend. I wish you well in the tests to come.')
				posts_replied_to.append(submission.id)
				print('ID successfully added')
				with open ('posts_replied_to.txt', 'w') as f: 
					for post_id in posts_replied_to:
						f.write(post_id+"\n")
			else:
					print('nothing here')
		elif submission.id in posts_replied_to:
			print('already replied bro')
	
	#except:
		#print('waiting 9.5 minutes')
		#time.sleep(9.5*60)				
x=x+1
print(x)





print('test done')

