import os
import unittest
from src.core.file_downloader import FileDownloader

class TestFileDownloader(unittest.TestCase):

    def setUp(self):
        self.file_url = "https://example.com/file.zip"
        self.output_path = "downloads/"
        self.downloader = FileDownloader(url=self.file_url)

    def test_download_file_success(self):
        # Test downloading a file (you may want to mock this)
        result = self.downloader.download_file(self.output_path)
        self.assertTrue(os.path.exists(os.path.join(self.output_path, "file.zip")), "File not downloaded successfully.")

    def test_download_file_invalid_url(self):
        invalid_downloader = FileDownloader(file_url="invalid_url")
        with self.assertRaises(Exception):
            invalid_downloader.download_file(self.output_path)

    def tearDown(self):
        # Clean up any downloaded files after tests
        if os.path.exists(os.path.join(self.output_path, "file.zip")):
            os.remove(os.path.join(self.output_path, "file.zip"))

if __name__ == "__main__":
    unittest.main()
