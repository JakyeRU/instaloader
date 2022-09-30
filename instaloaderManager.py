import instaloader
import terminal
import os
from pathlib import Path


def download_posts(L, profile):
    terminal.info(f'{"Updating" if os.path.exists(f"./{profile.username}") else "Downloading"} profile {profile.username}...')

    # Getting the posts
    posts = profile.get_posts()

    # Downloading the selected profile.
    for index, post in enumerate(posts):
        if L.download_post(post, target=profile.username):
            terminal.info(f'Post "{post.caption}" has been downloaded. [{index+1}/{profile.mediacount}]')
        else:
            terminal.error(f'Post "{post.caption}" couldn\'t be downloaded. [{index+1}/{profile.mediacount}]')

    terminal.success(f'{"Updated" if os.path.exists(f"./{profile.username}") else "Downloaded"} profile {profile.username}.')


def download_stories(L, profile):
    terminal.info(f'{"Updating" if os.path.exists(f"./{profile.username}/stories") else "Downloading"} profile {profile.username} stories...')

    # Getting the stories
    stories = L.get_stories(userids=[profile.userid])

    # Downloading the stories
    for story in stories:
        for item in story.get_items():
            # Downloading the story item
            if not L.download_storyitem(item, Path(f"./{profile.username}/stories")):
                terminal.error(f'{profile.username} story couldn\'t be downloaded.')

    terminal.success(f'{"Updated" if os.path.exists(f"./{profile.username}/stories") else "Downloaded"} profile {profile.username} stories.')
