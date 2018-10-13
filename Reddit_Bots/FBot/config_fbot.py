#config 

import praw, time, pdb, re, os

username = 'FriendshipRobotTest' #username for bot

password = '1q2w3e4r5t' # password for bot account


client_id = 'pERvZ3i6wcwTsw' # on preferences page, personal use script code 

client_secret = 	'zIV64hroD7-rZ0gaA-tDNV1MtlE' # secret code on preferences page

def init():
	global posts_replied_to
	posts_replied_to = []
	print('variables defined')

def replyDatabase():
	global posts_replied_to
	if not os.path.isfile('posts_replied_to.txt'):
			posts_replied_to = []
			print('posts_replied_to made')
	else:
		with open ("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = list(filter(None, posts_replied_to))
		print('posts_replied_to already made')

