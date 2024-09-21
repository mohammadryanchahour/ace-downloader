import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QComboBox, QFileDialog, QTabWidget, QMainWindow, QAction, QDialog
)
from PyQt5.QtCore import Qt
from src.core.download_manager import DownloadManager
from src.core.youtube_downloader import YouTubeDownloader

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ace Downloader")
        self.setGeometry(100, 100, 600, 400)  # Make window larger
        self.setMinimumSize(600, 400)         # Set minimum window size for diagonal resizing

        self.download_manager = DownloadManager()

        # Create a main widget to contain tabs
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # YouTube Tab
        self.youtube_tab = QWidget()
        self.setup_youtube_tab()
        self.tabs.addTab(self.youtube_tab, "YouTube")

        # File Download Tab
        self.file_tab = QWidget()
        self.setup_file_tab()
        self.tabs.addTab(self.file_tab, "File")

        # Video Download Tab
        self.video_tab = QWidget()
        self.setup_video_tab()
        self.tabs.addTab(self.video_tab, "Video")

        layout.addWidget(self.tabs)
        self.main_widget.setLayout(layout)

    def setup_youtube_tab(self):
        layout = QVBoxLayout()

        self.label_url = QLabel("YouTube Video URL:")
        layout.addWidget(self.label_url)
        self.entry_url = QLineEdit(self)
        layout.addWidget(self.entry_url)

        self.label_path = QLabel("Output Path:")
        layout.addWidget(self.label_path)
        self.entry_path = QLineEdit(self)
        layout.addWidget(self.entry_path)

        self.button_browse = QPushButton("Browse", self)
        self.button_browse.clicked.connect(self.browse_output_path)
        layout.addWidget(self.button_browse)

        self.label_resolution = QLabel("Resolution (e.g., 720p):")
        layout.addWidget(self.label_resolution)
        self.combo_resolution = QComboBox(self)
        self.combo_resolution.addItems(["360p", "480p", "720p", "1080p", "Best"])
        layout.addWidget(self.combo_resolution)

        self.button_download = QPushButton("Download YouTube Video", self)
        self.button_download.clicked.connect(self.download_youtube_video)
        layout.addWidget(self.button_download)

        self.youtube_tab.setLayout(layout)

    def setup_file_tab(self):
        layout = QVBoxLayout()
        self.label_file_url = QLabel("File URL:")
        layout.addWidget(self.label_file_url)
        self.entry_file_url = QLineEdit(self)
        layout.addWidget(self.entry_file_url)

        self.label_file_path = QLabel("Output Path:")
        layout.addWidget(self.label_file_path)
        self.entry_file_path = QLineEdit(self)
        layout.addWidget(self.entry_file_path)

        self.button_browse_file = QPushButton("Browse", self)
        self.button_browse_file.clicked.connect(self.browse_file_output_path)
        layout.addWidget(self.button_browse_file)

        self.button_download_file = QPushButton("Download File", self)
        self.button_download_file.clicked.connect(self.download_file)
        layout.addWidget(self.button_download_file)

        self.file_tab.setLayout(layout)

    def setup_video_tab(self):
        layout = QVBoxLayout()
        self.label_video_url = QLabel("Video URL:")
        layout.addWidget(self.label_video_url)
        self.entry_video_url = QLineEdit(self)
        layout.addWidget(self.entry_video_url)

        self.label_video_path = QLabel("Output Path:")
        layout.addWidget(self.label_video_path)
        self.entry_video_path = QLineEdit(self)
        layout.addWidget(self.entry_video_path)

        self.button_browse_video = QPushButton("Browse", self)
        self.button_browse_video.clicked.connect(self.browse_video_output_path)
        layout.addWidget(self.button_browse_video)

        self.button_download_video = QPushButton("Download Video", self)
        self.button_download_video.clicked.connect(self.download_video)
        layout.addWidget(self.button_download_video)

        self.video_tab.setLayout(layout)

    def browse_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_path:
            self.entry_path.setText(output_path)

    def browse_file_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_path:
            self.entry_file_path.setText(output_path)

    def browse_video_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_path:
            self.entry_video_path.setText(output_path)

    def download_youtube_video(self):
        video_url = self.entry_url.text()
        output_path = self.entry_path.text()
        resolution = self.combo_resolution.currentText() if self.combo_resolution.currentText() != "Best" else None
        
        try:
            # Create YouTubeDownloader instance with output_path and resolution
            downloader = YouTubeDownloader(video_url, output_path, resolution)
            self.download_manager.add_to_queue(downloader)
            self.download_manager.start_downloads()
            QMessageBox.information(self, "Success", "YouTube video download started successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")


    def download_file(self):
        file_url = self.entry_file_url.text()
        output_path = self.entry_file_path.text()
        try:
            # Placeholder: Add logic to handle file downloads
            QMessageBox.information(self, "Success", "File download started successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")

    def download_video(self):
        video_url = self.entry_video_url.text()
        output_path = self.entry_video_path.text()
        try:
            # Placeholder: Add logic to handle video downloads
            QMessageBox.information(self, "Success", "Video download started successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
