#!/usr/bin/python
import praw
import pdb
import re
import os
import random

# Create the Reddit instance
reddit = praw.Reddit('ComputerConverterBot')

# and login
# reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('all')

for submission in subreddit.hot(limit=10):
    random = random.randint(0, 4)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("1 foot", submission.body, re.IGNORECASE):
            # Reply to the post
            if (random == 1):
                submission.reply("1 foot? More like 0.98 NVIDIA Founder's Edition RTX 3090s")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)
            elif (random == 2):
                submission.reply("1 foot? More like 0.923 Gigabyte Vision RTX 3070 TIs")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)
            elif (random == 3):
                submission.reply("1 foot? More like 2.18 AMD Ryzen 2600s")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)
            elif (random == 4):
                submission.reply("1 foot? More like 1.52 G.Skill Trident Z Royal RAM Sticks")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
