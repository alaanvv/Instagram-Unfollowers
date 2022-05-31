import instaloader

# ---

config = open('config.txt', 'r').readlines()
user = config[0].split('=')[1].replace('\n', '')
password = config[1].split('=')[1].replace('\n', '')

# ---

insta = instaloader.Instaloader()

def login(): # Login eventually takes a few tries to work
    try:
        insta.login(user, password)
    except:
        login()
login()

profile = instaloader.Profile.from_username(insta.context, user)

# ---

follower_list = [follower + '\n' for follower in profile.get_followers()]

try:
    file_list = open('follower.txt', 'r').readlines()

except:
    open('follower.txt', 'w')
    file_list = []

# ---

file = open('follower.txt', 'w')

for line in follower_list:
    file.write(line)

file.close()

# ---

unfollowers = list(set(file_list) - set(follower_list))

if unfollowers == []:
    print('No unfollowers')

else: 
    print('Unfollowers:\n')
    for unf in unfollowers:
        print('>', unf)

input('ENTER')
