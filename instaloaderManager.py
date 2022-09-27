import instaloader
import terminal
import os


def download_posts(L, profile):
    terminal.info(f'{"Updating" if os.path.exists(profile.target) else "Downloading"} profile {profile.username}...')

    # Getting the posts
    posts = profile.get_posts()

    # Downloading the selected profile.
    for index, post in posts:
        if L.download_post(post, target=profile.username):
            terminal.info(f'Post "{post.title}" has been downloaded. [{index}/{len(posts)}]')
        else:
            terminal.error(f'Post "{post.title}" couldn\'t be downloaded. [{index}/{len(posts)}]')

    terminal.success(f'{"Updated" if os.path.exists(profile.target) else "Downloaded"} profile {profile.username}.')
