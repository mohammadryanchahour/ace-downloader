import unittest
import os
from src.core.youtube_downloader import YouTubeDownloader

class TestYouTubeDownloader(unittest.TestCase):

    def setUp(self):
        self.video_url = "https://www.youtube.com/watch?v=3f99GPLff_M"
        self.output_path = "downloads/"
        self.downloader = YouTubeDownloader(video_url=self.video_url)

    def test_download_video_success(self):
        result = self.downloader.download_youtube_video(self.output_path)
        self.assertTrue(os.path.exists(os.path.join(self.output_path, "output.mp4")), "Video not downloaded successfully.")

    def test_download_video_invalid_url(self):
        invalid_downloader = YouTubeDownloader(video_url="invalid_url")
        with self.assertRaises(Exception):
            invalid_downloader.download_youtube_video(self.output_path)

    def tearDown(self):
        # Clean up any downloaded files after tests
        if os.path.exists(os.path.join(self.output_path, "output.mp4")):
            os.remove(os.path.join(self.output_path, "output.mp4"))

if __name__ == "__main__":
    unittest.main()
