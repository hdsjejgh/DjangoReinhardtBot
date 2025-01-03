import praw
import cv2
import easyocr
from hhh import * #this file has all the info put in the praw.Reddit class like passowrd, id, etc
import asyncio

username = 'RobertFrippBot'
search = {'Robert fripp':"Robert fripp", 'Great deceiver':'The great deceiver', 'Groon':'Groon', 'Fripp':"Robert fripp", 'Robert':"Robert fripp", 'Lizard':"Lizard is ass"}

reddit = praw.Reddit(client_id=id,
                         client_secret=secret,
                         username=username,
                         password=password,
                         user_agent='fripp12345', )
subreddit = reddit.subreddit('KingCrimsonCircleJerk')
hot = subreddit.hot(limit=20)

async def replytopost(post, item, comments):
    if ("".join(item.lower().split()) in "".join(post.title.lower().split()) or "".join(item.lower().split()) in "".join(post.selftext.lower()).split()) and post.author != username and username not in [com.author for com in comments]:
        await post.reply(item)  # if mentioned, comment the item, then stop searching
        return False
    return True

async def replytocomment(comment, item):
    if "".join(item.lower().split()) in "".join(comment.body.lower().split()) and comment.author != username and username not in [com.author for com in comment.replies]:
        await comment.reply(item)
        return False
    return True

async def main():
    async for post in subreddit.h: #iterates over top 20 hot posts in subreddit
        print(post.title)
        if not post.stickied: #makes sure post isnt a pinned post
            comments = post.comments.list()
            for item in search.items(): #tests each item to see if the post mentions it
                if await replytopost(post, search[item], comments):
                    break
            for comment in comments: #does the same thing but with comments
                for item in search.items():
                    try:
                        if await replytocomment(comment, search[item]):
                            break
                    except AttributeError: #makes sure it doesnt break because praw is incapable of loading the more comments button
                        pass #you are a multi million dollar company reddit, why cant you do this??

if __name__ == '__main__':
    asyncio.run(main())