import os
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QProgressBar
from src.core.youtube_downloader import download_youtube_video

class YouTubeDownloaderWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.default_output_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.init_ui()

    def init_ui(self):
        self.url_label = QLabel('Enter YouTube URL:')
        self.url_entry = QLineEdit()

        self.output_label = QLabel('Output directory:')
        self.output_entry = QLineEdit()
        self.output_entry.setText(self.default_output_path)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.on_browse_clicked)

        self.resolution_label = QLabel('Resolution:')
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems(["1080p", "720p", "480p", "360p"])

        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.on_download_clicked)

        self.progress_bar = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_entry)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.resolution_label)
        layout.addWidget(self.resolution_combo)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def on_browse_clicked(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.output_entry.setText(folder_path)

    def on_download_clicked(self):
        url = self.url_entry.text()
        output_path = self.output_entry.text()
        resolution = self.resolution_combo.currentText()

        self.progress_bar.setValue(0)

        # def on_progress_callback(chunk_size, total_size):
        #     progress = (chunk_size / total_size) * 100
        #     self.progress_bar.setValue(progress)

        download_youtube_video(url, output_path, resolution)
