import os
import terminal
import json
import instaloader
import instaloaderManager

# Defining username and password variables that will get updated after validating the JSON
username = None
password = None

# Defining the available actions
actions = {
    '1': '1. Download Posts'
}

# Showing the boot logo
terminal.boot()

# Checking whether configuration.json exists
if not os.path.exists('./configuration.json'):
    terminal.error('No configuration.json file found.', shouldExit=True)

# Validating the JSON file
try:
    with open('./configuration.json', 'r') as file:
        file = json.load(file)

        if 'username' in file and 'password' in file:
            username = file['username']
            password = file['password']
        else:
            raise KeyError
except ValueError:
    terminal.error('The configuration.json file is invalid.', shouldExit=True)
except KeyError:
    terminal.error(f'The username or password is missing from configuration.json.', shouldExit=True)

terminal.info(f'Attempting to login to Instagram as {username}.')

# Trying to sign in to Instagram
L = instaloader.Instaloader(quiet=True)
try:
    L.login(user=username, passwd=password)
except instaloader.exceptions.BadCredentialsException:
    terminal.error(f'The password is not valid.', shouldExit=True)
except instaloader.exceptions.ConnectionException as ConnectionException:
    terminal.error(ConnectionException, shouldExit=True)

terminal.success(f'Logged in as {username}.')

terminal.info('Enter profile name: ')
profile = input()

# Validating profile
try:
    profile = instaloader.Profile.from_username(L.context, profile)
except instaloader.exceptions.ProfileNotExistsException:
    terminal.error(f'The profile {profile} does not exist.', shouldExit=True)

# Checking if the profile can be interacted with
if profile.is_private and not profile.followed_by_viewer:
    terminal.error(f'{profile.username} is private and you are not following them.', shouldExit=True)

# Showing available options
terminal.info(f'What action do you want to perform on {profile.username}?')
for action in actions.values():
    terminal.info(action, prefix=False)
action = input()
while action not in actions:
    terminal.error('Invalid action. Available actions:')
    for action in actions.values():
        terminal.info(action, prefix=False)
    action = input()

match action:
    case '1':
        instaloaderManager.download_posts(L, profile)