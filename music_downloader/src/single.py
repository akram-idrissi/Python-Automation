import os
from pytube import YouTube, Playlist


def is_youtube_url(link):
    """ tells if the url is a youtube url """
    if "youtube" in link:
        return link
    return None


def new_dir(title):
    """ makes a new directory and change the current one """
    if not os.path.exists(title):
        os.makedirs(title)
    os.chdir(title)


def its_video(link):
    """ tells if the url is a video or not """
    try:
        playlist = Playlist(link)
        playlist.playlist_id
    except KeyError:
        return link


def add_extension(path):
    """ adds the .txt extension if it doesn't exist """
    ext = ".txt"
    if ext not in path:
        path = path + ext
    return path


def remove_none(links):
    """ remove None from the given list of urls """
    good_urls = [link for link in links if link is not None]
    return good_urls


def gather_objects(urls):
    """ returns a list of YouTube objects """
    urls = remove_none(urls)
    youtube_urls = list(map(is_youtube_url, urls))
    valid_urls = list(map(its_video, youtube_urls))
    stream_objects = list(map(YouTube, valid_urls))

    return stream_objects


def extract_from_file(path):
    """ returns a list ytb objects from a file of urls """
    path = add_extension(path)

    with open(path, "r") as f:
        urls = [line for line in f.read().split("\n")]

    return gather_objects(urls)


def file_download(path, audio=False):
    """ download the file urls in two formats audio/video """
    streams = extract_from_file(path)

    if not audio:
        for stream in streams:
            print("Start downloading videos, please wait...")
            stream.streams.get_highest_resolution().download()
            print("Videos have been downloaded")
    else:
        for stream in streams:
            print("Start downloading audios, please wait...")
            stream.streams.get_audio_only().download()
            print("Audios have been downloaded")


def one_video_download(link, audio=False, title=None):
    """ download the url in two formats audio/video """
    youtube_url = is_youtube_url(link)
    if youtube_url:
        valid_url = its_video(link)

    ytb_obj = YouTube(valid_url)
    stream = ytb_obj.streams

    if audio:
        new_dir(title)
        print("Start downloading audio, please wait...")
        stream.get_audio_only().download()
        print("Audio has been downloaded")
    else:
        new_dir(title)
        print("Start downloading video, please wait...")
        stream.get_highest_resolution().download()
        print("Video has been downloaded")


def main(link=None, path=None, audio=False, title=None):
    if url:
        if audio:
            one_video_download(link, audio=True, title=title)
        else:
            one_video_download(link, audio=False, title=title)

    elif path:
        if audio:
            file_download(path, audio=True, title=title)
        else:
            file_download(path, audio=False, title=title)


url = "https://www.youtube.com/watch?v=y-9MaAW_9dY"
main(url=url, audio=True, title="")

