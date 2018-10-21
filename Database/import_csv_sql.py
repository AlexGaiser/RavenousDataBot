# convert csv to sql table


import sqlite3, csv

connection = sqlite3.connect("reddit_politics.db")

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE reddit_posts(POST_NUMBER PRIMARY KEY, 
    Title STR, 
    Body STR, 
    Karma INT, 
    DateandTime DATE, 
    Subreddit STR, 
    Post_Author STR, 
    Submission Link STR, 
    Submission_URL STR, 
    Submission_ID STR,
    Top_Comment STR,
    Top_Comment_Author STR,
    Top_Comment_Upvotes INT,
    Datetime_Collected DATE,
    Sort);
    
    """
    )

with open ('pol_reddit_posts.csv', 'r') as politics_table:
    dr = csv.DictReader(politics_table)
    to_db = [(i['POST_NUMBER'],i['Title'],i['Body'],i['Karma'], i['Date and Time'], i['Subreddit'], i['Post Author'], i['Submission Link'], i['Submission URL'], i['Submission ID'], i['Top Comment'], i['Top Comment Author'], i['Top Comment Upvotes'], i['Datetime Collected'], i['Sort']) for i in dr]
    
cursor.executemany("INSERT INTO reddit_posts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)

connection.commit()

cursor.execute("SELECT * FROM reddit_posts")

print('fetchall: ')
result = cursor.fetchall()

for r in result:
    print(r)



