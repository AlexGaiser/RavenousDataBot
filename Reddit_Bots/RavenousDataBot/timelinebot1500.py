#! python3
#timelinebot v1.0.0
#This is the main script to run timelinebot
'''
Todo: 
1. write titles to csv [done]
2. write content body to csv [done]
3. write current karma to csv [done]
4. write date and time of submission to csv [done]
5. determine how to extract keywords or repeated words from submissions
6. write keywords or repeated words to csv
7. write top comment to csv[done]
8. writer number of comments to csv
9. write subreddit of origin to csv [done]
10. organize collected data into columns [done]
11. write post url to csv [done]
12. write submission url if applicable [done]
13. write string with commas to csv [done]
14. keep track of submissions collected [done]
15. Create New File with Timestamp each time runs(oh hold, may not be needed) [done, writes time collected in csv]
16. Solve first append cut off bug
17. Solve UnicodeEncodeError [done]
18. Solve extra line bug [done]
19. Find a way to track posts that have already been collected
20. solve top comment author missing bug
'''
import cfg
import praw, time, pdb, re, os, csv, datetime



print('Test Started')
###logs into timelinebot user
r = praw.Reddit(username = cfg.username,
				password = cfg.password,
				client_id = cfg.client_id,
				client_secret = cfg.client_secret,
				user_agent = 'timelinebot test friendship maker v0.1')

#test subreddit askreddit, will be changed to /all

#setting variables
subreddit = r.subreddit("all")


headers = 'Title, Body, Karma, Date and Time, Subreddit, Post Author, Submission Link, Submission URL, SubmissionID, Top Comment, Top Comment Author, Top Comment Upvotes, Datetime Collected \n' #headers of csv

csvname = str ('Reddit_All.csv' )
archivename = str ('timelinearchive.txt')
cwd = (os.getcwd())
csvfilepath =  (cwd+ '\\'+'\\' + csvname)
archivefilepath =  (cwd+ '\\'+'\\' + archivename)

#The above creates file path regardless of directory (Hopefully)


print(csvname)
if not os.path.isfile(csvname):#creates a csv with headers if doesn't exist in current directory
	f = open(csvname,"w")
	f.write(headers)
	print('File Created')
else:
	print("file already made proceeding to test")

if not os.path.isfile(archivename):
	posts_collected = []
	p = open(archivename, 'w')
	p.write('Archive for timelinebot \n')
	print('posts_collected file made')
else:
	with open (archivename, "r") as p:
		posts_collected = p.read()
		posts_collected = posts_collected.split("\n")
		posts_collected = list(filter(None, posts_collected))

def timelinebot():
	for submission in subreddit.new(limit=1500):
		Title = submission.title
		Body = submission.selftext
		Karma = submission.score
		DateandTime = datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S')
		Subreddit = submission.subreddit
		SubmissionLinkUrl =submission.url
		SubmissionURL= submission.permalink
		SubmissionID = submission.id
		CollectedOn = datetime.datetime.now()
		try:
			PostAuthor = submission.author.name
		except:
			PostAuthor = 'PA'+'[deleted]'
			print('submission author was deleted')
			


		comment_body = [comment.body for comment in submission.comments if hasattr(comment, "body")]
		try: 
			top_comment = comment_body[0]
		except: 
			top_comment = 'CB'+'[deleted]'
		
		try: 
			top_comment_author = submission.comments[0].author.name
			mail
		except:
			top_comment_author = 'CA'+ '[deleted]'
			print('comment author was deleted')
		

		try: 
			top_comment_upvotes = str(submission.comments[0].score)
		except:
			top_comment_upvotes = 'CS'+'[deleted]'


		DataList = [
		str(Title), 
		str(Body), 
		str(Karma), 
		str(DateandTime), 
		str(Subreddit),
		str(PostAuthor),  
		str(SubmissionLinkUrl), 
		str(SubmissionURL), 
		str(SubmissionID), 
		str(top_comment), 
		str(top_comment_author), 
		str(top_comment_upvotes),
		str(CollectedOn)
		 ]
		#[variables.encode("utf-8") for variables in DataList]
		with open (archivefilepath, "r") as p:
				posts_collected = p.read()
				posts_collected = posts_collected.split("\n")
				posts_collected = list(filter(None, posts_collected))
		if SubmissionID not in posts_collected:
			for i in DataList:
				print(str(i).encode('utf-8'))
			with open (csvname, "a", newline = '', encoding='utf-8', errors = 'replace') as Output_CSV:
				csvWriter = csv.writer(Output_CSV)
				csvWriter.writerow(DataList)
		
			#csvWriter.writerow((Body)+'\n')
			print('csv appended')

			p = open(archivename,'a')
			p.write(SubmissionID + "\n") 
			print('Post added')	
		elif submission.id in posts_collected:
			print('already collected')
			



timelinebot()

subreddit = r.subreddit("askreddit")
csvname = str ('Reddit_Stories.csv' )
archivename = str ('storytimelinearchive.txt')
cwd = (os.getcwd())
csvfilepath =  (cwd+ '\\'+'\\' + csvname)
archivefilepath =  (cwd+ '\\'+'\\' + archivename)

if not os.path.isfile(csvname):#creates a csv with headers if doesn't exist in current directory
	f = open(csvname,"w")
	f.write(headers)
	print('File Created')
else:
	print("file already made proceeding to test")

if not os.path.isfile(archivename):
	posts_collected = []
	p = open(archivename, 'w')
	p.write('Archive for timelinebot \n')
	print('posts_collected file made')
else:
	with open (archivename, "r") as p:
		posts_collected = p.read()
		posts_collected = posts_collected.split("\n")
		posts_collected = list(filter(None, posts_collected))

timelinebot()

subreddit= r.subreddit('tifu')

timelinebot()
print('collection completed')

subreddit = r.subreddit('The_Donald')

timelinebot()

subreddit = r.subreddit('politics')

timelinebot()

subreddit = r.subreddit('legaladvice')