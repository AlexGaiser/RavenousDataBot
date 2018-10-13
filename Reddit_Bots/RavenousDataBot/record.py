#! python3
#WILL CREATE a text file and add submission ids to it to prevent double collection of 
#data 
import praw, time, pdb, re, os




def filemaker(): 
	if not os.path.isfile('posts_collected.txt'):
		posts_collected = []
	else:
		with open ("posts_collected.txt", "r") as f:
			posts_collected = f.read()
			posts_collected = posts_collected.split("\n")
			posts_collected = list(filter(None, posts_collected))

def postcollector():
	if submission.id not in posts_collected:
		with open ('posts_collected.txt', 'w') as f: 
			for post_id in posts_collected:
				f.write(post_id+"\n")
		print('ID successfully added')
			
	elif submission.id in posts_collected:
		print('already collected')

filemaker()
postcollector()