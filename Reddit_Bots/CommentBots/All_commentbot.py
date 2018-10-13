
import cfg

import praw, time, pdb, re, os, csv, datetime

from csvmaker import csvmaker, archive

r = praw.Reddit(username = cfg.username,
                password = cfg.password,
                client_id = cfg.client_id,
                client_secret = cfg.client_secret,
                user_agent = 'RavenousDataBot test friendship maker v0.1')

subreddit = r.subreddit('test')

def comments_to_dict(comments):
    results = []
    for comment in comments:
        item = {
            "id":comment.id,
            "author": comment.author,
        }
        if len(comment.replies) > 0:
            item["replies"] = comments_to_dict(comment.replies)

    results.append(item)
    print(results)
    return results




# def commentbot(subreddit, limit):

#     subreddit = r.subreddit(subreddit)
#     for submission in subreddit.top(limit=limit):
#         Title = submission.title
#         Body = submission.selftext
#         Karma = submission.score
#         DateandTime = datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S')
#         Subreddit = submission.subreddit
#         SubmissionLinkUrl =submission.url
#         SubmissionURL= submission.permalink
#         SubmissionID = submission.id
#         CollectedOn = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        


#         comments_to_dict(submission.comments)


#         commentauthor = [comment.author for comment in submission.comments if hasattr(comment, "body")]

#         print(len(commentauthor))
#         x = 0
#         for comment in commentauthor:
#             print(comment)
#             x+= 1
#             print('----------comment number--'+ str(x))

#         print(Title)

# commentbot('askreddit', 4)



def subcomments(subID):
    submission = r.submission(id=subID)

    forest_comments = submission.comments
    


subcomments('8x1tfa')