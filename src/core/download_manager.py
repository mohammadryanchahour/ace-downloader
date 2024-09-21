import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DownloadManager:
    def __init__(self, max_concurrent_downloads=3):
        self.max_concurrent_downloads = max_concurrent_downloads
        self.executor = ThreadPoolExecutor(max_workers=max_concurrent_downloads)
        self.download_queue = []
        self.futures = []
        self.paused_downloads = []

    def add_to_queue(self, downloader):
        """Adds a downloader task to the queue."""
        if downloader is None:
            logging.error("Attempted to add a None downloader to the queue.")
            return
        self.download_queue.append(downloader)
        logging.info(f"Download added to queue: {downloader}")

    def start_downloads(self):
        """Starts downloads while respecting the concurrent download limit."""
        while self.download_queue or self.futures:
            while len(self.futures) < self.max_concurrent_downloads and self.download_queue:
                next_download = self.download_queue.pop(0)
                try:
                    future = self.executor.submit(next_download.start)
                    self.futures.append(future)
                    logging.info(f"Started download: {next_download}")
                except Exception as e:
                    logging.error(f"Failed to start download {next_download}: {e}")

            for future in as_completed(self.futures):
                try:
                    result = future.result()
                    logging.info(f"Download completed: {result}")
                except Exception as e:
                    logging.error(f"Error during download: {e}")
                finally:
                    self.futures.remove(future)

            time.sleep(1)

    def pause_download(self, downloader):
        """Pauses an ongoing download."""
        if downloader not in self.paused_downloads:
            try:
                downloader.pause()
                self.paused_downloads.append(downloader)
                logging.info(f"Download paused: {downloader}")
            except Exception as e:
                logging.error(f"Error pausing download {downloader}: {e}")
        else:
            logging.warning(f"Download already paused: {downloader}")

    def resume_download(self, downloader):
        """Resumes a paused download."""
        if downloader in self.paused_downloads:
            try:
                downloader.resume()
                self.paused_downloads.remove(downloader)
                future = self.executor.submit(downloader.start)
                self.futures.append(future)
                logging.info(f"Download resumed: {downloader}")
            except Exception as e:
                logging.error(f"Error resuming download {downloader}: {e}")
        else:
            logging.warning(f"Download not found in paused downloads: {downloader}")

    def stop_all(self):
        """Stops all active downloads."""
        for future in self.futures:
            try:
                future.cancel()
            except Exception as e:
                logging.error(f"Error canceling future: {e}")
        self.futures = []
        logging.info("All downloads stopped.")
