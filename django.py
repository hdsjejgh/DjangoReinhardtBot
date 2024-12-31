import praw
from hhh import *

username = 'DjangoReinhardtBot'
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     username=username,
                     password=password,
                     user_agent='django123456',)

subreddit = reddit.subreddit('jazzcirclejerk')

hot = subreddit.hot(limit=20)

for post in hot:
    if not post.stickied:
        if ("django reinhardt" in post.title.lower() or "django reinhardt" in post.selftext.lower()) and post.author != username:
            post.add_comment("Django reinhardt")
        comments = post.comments.list()
        for comment in comments:
            try:
                if "django reinhardt" in comment.body.lower() and comment.author != username and username not in [com.author for com in comment.replies]:
                    comment.reply("Django reinhardt")
            except AttributeError:
                pass