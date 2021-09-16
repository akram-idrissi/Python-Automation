import os
from pytube import Playlist


def is_youtube_url(link):
    """ tells if the url is a youtube url """
    if "youtube" in link:
        return link
    return None


def new_dir(title):
    """ makes a new directory and changes the current one """
    if not os.path.exists(title):
        os.makedirs(title)
    os.chdir(title)


def is_playlist(link):
    """ returns url if its a playlist url """
    try:
        playlist = Playlist(link)
        playlist.playlist_id
        return playlist
    except KeyError:
        return None


def playlist_download(link, audio=False, title=None):
    ytb_url = is_youtube_url(link)
    playlist_urls = is_playlist(link)

    if playlist_urls:
        if audio:
            new_dir(title)
            print(f"Start downloading {playlist_urls.title} audio format")
            for link in playlist_urls.videos:
                link.streams.get_audio_only().download()
            print(f"It's done, you'll find the songs in the {title} folder")
        else:
            new_dir(title)
            print(f"Start downloading {playlist_urls.title} video format")
            for link in playlist_urls.videos:
                link.streams.get_audio_only().download()
            print(f"It's done, you'll find the songs in the {title} folder")


url = "https://www.youtube.com/watch?v=j9FV40_1Z9M&list=PLIwluRGeyvBJUKr3lZJA7bskD5__FglLe"
playlist_download(url, audio=True, title="Que La Famille")

