import logging

class Downloader:
    def __init__(self):
        self._paused = False
        self._should_stop = False

    def start(self):
        """Starts the download. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses should implement this!")

    def pause(self):
        """Pauses the download."""
        self._paused = True
        logging.info("Download has been paused.")

    def resume(self):
        """Resumes the download."""
        self._paused = False
        logging.info("Download has been resumed.")

    def stop(self):
        """Stops the download."""
        self._should_stop = True
        logging.info("Download has been requested to stop.")
