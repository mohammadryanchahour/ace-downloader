import os
import logging
import yt_dlp
from .video_downloader import VideoDownloader

class YouTubeDownloader(VideoDownloader):
    def __init__(self, video_url, output_path, resolution=None):
        super().__init__(video_url)
        self.video_url = video_url
        self.output_path = output_path
        self.resolution = resolution

    def download_youtube_video(self):
        """Download a YouTube video with separate audio and video streams using yt-dlp."""
        try:
            ydl_opts = {
                'format': f'bestvideo[height<={self.resolution}]+bestaudio/best[height<={self.resolution}]' if self.resolution else 'best',
                'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }]
            }

            os.makedirs(self.output_path, exist_ok=True)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_url])

            logging.info(f"Video downloaded successfully to {self.output_path}")

        except Exception as e:
            logging.error(f"Error downloading video: {e}")

    def start(self):
        """Starts the YouTube download process."""
        self.download_youtube_video()
