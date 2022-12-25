import os

def get_sessions():
    if not os.path.exists(f'{os.getenv("localappdata")}/Instaloader'): return []

    sessions = os.listdir(f'{os.getenv("localappdata")}/Instaloader')

    for index, session in enumerate(sessions):
        # Removing the "session-" prefix
        sessions[index] = session[8:]

    return sessions