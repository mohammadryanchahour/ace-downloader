import time
import requests
import logging
from .downloader import Downloader

class FileDownloader(Downloader):
    def __init__(self, url, destination):
        super().__init__()
        self.url = url
        self.destination = destination

    def start(self):
        """Starts the file download."""
        logging.info(f"Starting download from {self.url} to {self.destination}")
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))

            with open(self.destination, 'wb') as file:
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

            logging.info("Download completed successfully.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading file: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
