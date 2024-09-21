# tests/test_video_downloader.py

import unittest
from src.core.video_downloader import VideoDownloader

class TestVideoDownloader(unittest.TestCase):

    def setUp(self):
        self.video_url = "https://example.com/video.mp4"
        self.downloader = VideoDownloader(page_url=self.video_url)

    def test_video_downloader_initialization(self):
        self.assertIsInstance(self.downloader, VideoDownloader)

if __name__ == "__main__":
    unittest.main()
