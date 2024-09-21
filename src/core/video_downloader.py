# src/ace_downloader/core/video_downloader.py

import time
import requests
import logging
from .downloader import Downloader
from bs4 import BeautifulSoup

class VideoDownloader(Downloader):
    def __init__(self, page_url):
        super().__init__()
        self.page_url = page_url
        self.video_urls = []

    def extract_video_links(self):
        """Extracts video links from the provided page URL."""
        logging.info(f"Extracting video links from {self.page_url}")
        try:
            response = requests.get(self.page_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            for video_tag in soup.find_all('video'):
                source = video_tag.find('source')
                if source and 'src' in source.attrs:
                    self.video_urls.append(source['src'])
                logging.info(f"Found video URL: {source['src']}")

        except Exception as e:
            logging.error(f"Error extracting video links: {e}")

    def download_video(self, url, destination):
        """Downloads a video from a URL to a specified destination."""
        logging.info(f"Starting download from {url} to {destination}")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))

            with open(destination, 'wb') as file:
                for data in response.iter_content(chunk_size=1024):
                    if self._should_stop:
                        logging.info("Download stopped.")
                        return
                    if self._paused:
                        logging.info("Download paused.")
                        while self._paused:
                            time.sleep(1)
                    file.write(data)
                    logging.info(f"Downloaded {file.tell()}/{total_size} bytes")

            logging.info("Video download completed successfully.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading video: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def start(self):
        """Starts the video download process."""
        self.extract_video_links()
        for i, url in enumerate(self.video_urls):
            destination = f"video_{i + 1}.mp4"
            self.download_video(url, destination)
