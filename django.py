import praw
from hhh import *

username = 'RobertFrippBot'
search = ['Robert fripp', 'The great deceiver', 'Groon']
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     username=username,
                     password=password,
                     user_agent='fripp12345',)

subreddit = reddit.subreddit('KingCrimsonCircleJerk')

hot = subreddit.hot(limit=20)


for post in hot: #iterates over top 20 hot posts in subreddit
    print(post.title)
    if not post.stickied: #makes sure post isnt a pinned post
        comments = post.comments.list()
        for item in search: #tests each item to see if the post mentions it
            if (item.lower() in post.title.lower() or item.lower() in post.selftext.lower()) and post.author != username and username not in [com.author for com in comments]:
                post.reply(item) #if mentioned, comment the item, then stop searching
                break
        for comment in comments: #does the same thing but with comments
            for item in search:
                try:
                    if item.lower() in comment.body.lower() and comment.author != username and username not in [com.author for com in comment.replies]:
                        comment.reply(item)
                except AttributeError: #makes sure it doesnt break because praw is incapable of loading the more comments button
                    pass #you are a multi million dollar company reddit, why cant you do this??