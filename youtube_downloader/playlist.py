from moviepy.editor import *
from pytube import Playlist


class LoadPlaylist:

    def __init__(self, link):
        self.link = link

    def is_valid(self):
        play_list = Playlist(self.link)
        return True if "youtube" in self.link and play_list.playlist_id else False

    @staticmethod
    def make_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def to_mp3(path_mp3, vid):
        mp3 = "".join([os.path.splitext(vid)[0], ".mp3"])
        mp3_path = os.path.join(path_mp3, mp3)

        video = VideoFileClip(vid)
        audio = video.audio
        audio.write_audiofile(mp3_path)
        audio.close()
        video.close()

    @staticmethod
    def download(play_list):
        for link in play_list.videos:
            link.streams.get_highest_resolution().download()

    @staticmethod
    def load():
        return [file_name for file_name in os.listdir() if os.path.splitext(file_name)[1] == ".mp4"]

    @staticmethod
    def clean():
        for video in os.listdir():
            if os.path.splitext(video)[1] == ".mp4":
                os.remove(video)

    def run(self):
        if self.is_valid():
            play_list = Playlist(self.link)
            print(f"Downloading {play_list.title}..")
            self.download(play_list)
            mp4_videos = self.load()
            title = play_list.title + " - mp3"
            self.make_dir(title)
            for video in mp4_videos:
                self.to_mp3(title, video)
            self.clean()
            print("Done")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=j9FV40_1Z9M&list=PLIwluRGeyvBJUKr3lZJA7bskD5__FglLe"
    app = LoadPlaylist(url)
    app.run()
