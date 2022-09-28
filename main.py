import os
import terminal
import json
import instaloader
import instaloaderManager

username = None

# Defining the available actions
actions = {
    '1': '1. Download Posts'
}

# Showing the boot logo
terminal.boot()

# Making sure the platform is windows
if not os.name == 'nt':
    terminal.error('This script is currently only available on Windows.', shouldExit=True)

sessions = os.listdir(f'{os.getenv("localappdata")}/Instaloader')

for index, session in enumerate(sessions):
    # Removing the "session-" prefix
    sessions[index] = session[8:]

# Checking if there are any sessions available
if not os.path.exists(f'{os.getenv("localappdata")}/Instaloader') or len(sessions) == 0:
    terminal.info('There are no sessions available. Would you like to run the cookie_script.py? [y/n]')
    answer = input()
    while answer.lower() not in ['y', 'n', 'yes', 'no']:
        terminal.error('Invalid answer. Accepted answers: y, n, yes, no.')
        answer = input()
    if answer in ['y', 'yes']:
        exec(open('./cookie_script.py', 'r').read())
    exit(1)

terminal.info('Which account do you want to use?')
terminal.info(f'Available accounts: ' + ', '.join(sessions))
username = input()
while username not in sessions:
    terminal.error(f'Invalid account. Available accounts: ' + ', '.join(sessions))
    username = input()

terminal.info(f'Attempting to login to Instagram as {username}.')

# Trying to sign in to Instagram
L = instaloader.Instaloader(quiet=True)
try:
    L.load_session_from_file(username=username)
except instaloader.exceptions.BadCredentialsException:
    terminal.error(f'The password is not valid.', shouldExit=True)
except instaloader.exceptions.ConnectionException as ConnectionException:
    terminal.error(ConnectionException, shouldExit=True)

terminal.success(f'Logged in as {username}.')

terminal.info('Enter the profile name you want to interact with: ')
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