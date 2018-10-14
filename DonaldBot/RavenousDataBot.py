#! python3
 # reddit RavenousDonaldBot



import cfg

import praw, time, pdb, re, os, csv, datetime, csvmaker,sys

from csvmaker import csvmaker, archive

os.chdir(os.path.dirname(os.path.abspath(__file__)))


print(datetime.datetime.now())
print(sys.version)



###logs into RavenousDataBot user
r = praw.Reddit(username = cfg.username,
				password = cfg.password,
				client_id = cfg.client_id,
				client_secret = cfg.client_secret,
				user_agent = 'RavenousDataBot test friendship maker v0.1')

def logger(s,message):
    timecollected = datetime.datetime.now()
    
    archive(s)
    
    log = open(s,'a')
    log.write(str(timecollected)+ "\n") 
    print(message + str(timecollected))





def RavenousDataBot(subreddit, sort, limit, csvname, archivename):
    




    import cfg

    import praw, time, pdb, re, os, csv, datetime, csvmaker,sys

    from csvmaker import csvmaker, archive

    from RavenousDataBot import RavenousDataBot, logger



    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    logger('paralog' + str(subreddit) + str(sort)+'txt', str(subreddit)+str(sort)+ 'logged')

    print(datetime.datetime.now())
    print(sys.version)

    r = praw.Reddit(username = cfg.username,
    				password = cfg.password,
    				client_id = cfg.client_id,
    				client_secret = cfg.client_secret,
    				user_agent = 'RavenousDataBot test friendship maker v0.1')




    headers = 'Title, Body, Karma, Date and Time, Subreddit, Post Author, Submission Link, Submission URL, SubmissionID, Top Comment, Top Comment Author, Top Comment Upvotes, Datetime Collected \n' #headers of csv
    subreddit = r.subreddit(subreddit)
    


    if sort == "new":
        sort = subreddit.new(limit = limit)
        print("new")
    elif sort == "top":
        sort = subreddit.top(limit = limit)
    elif sort == "controversial":
        sort = subreddit.controversial(limit = limit)
    else:
        sort = subreddit.hot(limit = limit)
        "hot"


    csvmaker(csvname, headers)

    archive(archivename)
    print(archivename)
    print(csvname)
    # for submission in sort(limit=limit):


    for submission in sort:
        print('*************' + str(subreddit) + '  ' + str(sort) + '******************')

        Title = submission.title
        Body = submission.selftext
        Karma = submission.score
        DateandTime = datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S')
        Subreddit = submission.subreddit
        SubmissionLinkUrl =submission.url
        SubmissionURL= submission.permalink
        SubmissionID = submission.id
        CollectedOn = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
        
        def write_post_to_csv(archivename, csvname):
            
            print('WRITING WRITING ' + str(subreddit) + '  ' + str(sort) + 'WRITING WRITING')


            with open (archivename, "r") as p:
                        posts_collected = p.read()
                        posts_collected = posts_collected.split("\n")
                        posts_collected = list(filter(None, posts_collected))
            if SubmissionID not in posts_collected:
                for i in DataList:
                    print(str(i).encode('utf-8'))
                
                with open (csvname, "a", newline = '', encoding='utf-8', errors = 'replace') as Output_CSV:
                    csvWriter = csv.writer(Output_CSV)
                    csvWriter.writerow(DataList)
                print('csv appended')

                p = open(archivename,'a')
                p.write(SubmissionID + "\n") 
                print('Post added') 
            
            elif submission.id in posts_collected:
                print('already collected')



        write_post_to_csv(archivename, csvname)

    print('##################### Function Ended #####################')


            
