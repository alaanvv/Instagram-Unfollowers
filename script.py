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
# Reading the actual followers in a list

follower_list = []

for follower in profile.get_followers():

    follower_list.append(follower.username + '\n')

# ---
# Reading the file before writing

try:
    file_list = open('cache/follower.txt', 'r').readlines()

except:
    file = open('cache/follower.txt', 'w')
    file_list = open('cache/follower.txt', 'r').readlines()

# ---
# Writing the new followers list to the file

file = open('cache/follower.txt', 'w')

for line in follower_list:
    file.write(line)

file.close()

# ---
# Comparing the lists

unfollowers = list(set(file_list) - set(follower_list)) # Getting elements that arent in the new list

if unfollowers == []:
    print('No unfollowers')

else: 
    print('Unfollowers:\n')
    for unf in unfollowers:
        print('>', unf)
