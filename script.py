# Importing libs

import instaloader

# ---
# Setup

config = open('config.txt', 'r').readlines()
user = config[0].split('=')[1].replace('\n', '')
password = config[1].split('=')[1].replace('\n', '')

# ---
# Getting profile object

insta = instaloader.Instaloader() # Instagram object

def login(): # Login eventually takes a few tries to work
    try:
        insta.login(user, password)
    except:
        login()
login()

profile = instaloader.Profile.from_username(insta.context, user)

# ---
# Reading the actual followees in a list

followee_list = []

for followee in profile.get_followers():

    followee_list.append(followee.username + '\n')

# ---
# Reading the file before writing

try:
    file_list = open('cache/followee.txt', 'r').readlines()

except:
    file = open('cache/followee.txt', 'w')
    file_list = open('cache/followee.txt', 'r').readlines()

# ---
# Writing the new followees list to the file

file = open('cache/followee.txt', 'w')

for line in followee_list:
    file.write(line)

file.close()

# ---
# Comparing the lists

unfollowees = list(set(file_list) - set(followee_list)) # Getting elements that arent in the new list

if unfollowees == []:
    print('No unfollowees')

else: 
    print('Unfollowees:\n')
    for unf in unfollowees:
        print('>', unf)
