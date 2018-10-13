#! python3
 # reddit RavenousDonaldBot



import cfg

import praw, time, pdb, re, os, csv, datetime, csvmaker,sys

from csvmaker import csvmaker, archive

from RavenousDataBot import RavenousDataBot, logger

os.chdir(os.path.dirname(os.path.abspath(__file__)))


print(datetime.datetime.now())
print(sys.version)


print('DONALD STARTED')
###logs into RavenousDataBot user
r = praw.Reddit(username = cfg.username,
				password = cfg.password,
				client_id = cfg.client_id,
				client_secret = cfg.client_secret,
				user_agent = 'RavenousDataBot test friendship maker v0.1')





RavenousDataBot('the_donald', 'new', 1000, 'donaldnew.csv', 'donaldarchive.txt')
RavenousDataBot('the_donald', 'hot', 500,'hotdonald.csv', 'hotdonaldarchive.txt')




logger()