import playlist
import pytube


class LoadSong:
    def __init__(self, link):
        self.pst = playlist.LoadPlaylist(link)
        self.link = link
        self.title = ""

    def is_valid(self):
        if "youtube" in self.link:
            try:
                _ = pytube.Playlist(self.link).playlist_id
            except KeyError:
                return self.link

    def download(self):
        ytb = pytube.YouTube(self.link)
        ytb.streams.get_highest_resolution().download()
        self.title = ytb.title

    def run(self):
        if self.is_valid():
            print(f"Downloading {self.title}..")
            self.download()
            mp4_videos = self.pst.load()
            for video in mp4_videos:
                self.pst.to_mp3("", video)
            self.pst.clean()
            print("Done")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=y-9MaAW_9dY"
    app = LoadSong(url)
    app.run()



