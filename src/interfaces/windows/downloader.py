from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QHBoxLayout
)
from PyQt5.QtCore import Qt, pyqtSignal

class DownloaderWindow(QWidget):
    # Signal to trigger actions like pause/resume/cancel
    pause_download = pyqtSignal()
    resume_download = pyqtSignal()
    cancel_download = pyqtSignal()

    def __init__(self, download_manager, downloader):
        super().__init__()
        self.download_manager = download_manager
        self.downloader = downloader

        self.setWindowTitle("Downloading...")
        self.setGeometry(200, 200, 400, 150)

        # Progress Tracker (using the ProgressTrackerWidget we created earlier)
        self.progress_tracker = QProgressBar(self)
        self.progress_tracker.setAlignment(Qt.AlignCenter)
        self.progress_tracker.setValue(0)

        # Download control buttons
        self.pause_button = QPushButton("Pause", self)
        self.resume_button = QPushButton("Resume", self)
        self.cancel_button = QPushButton("Cancel", self)

        # Connect buttons to actions
        self.pause_button.clicked.connect(self.on_pause)
        self.resume_button.clicked.connect(self.on_resume)
        self.cancel_button.clicked.connect(self.on_cancel)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Downloading: {self.downloader.video_url}"))
        layout.addWidget(self.progress_tracker)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.resume_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def on_pause(self):
        """Pause the download."""
        self.pause_download.emit()
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(True)

    def on_resume(self):
        """Resume the download."""
        self.resume_download.emit()
        self.resume_button.setEnabled(False)
        self.pause_button.setEnabled(True)

    def on_cancel(self):
        """Cancel the download."""
        self.cancel_download.emit()
        self.close()

    def update_progress(self, value):
        """Update the progress bar."""
        self.progress_tracker.setValue(value)
