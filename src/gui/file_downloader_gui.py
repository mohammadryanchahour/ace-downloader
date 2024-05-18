# src/gui/file_downloader_gui.py
import os
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QProgressBar
from src.core.file_downloader import download_file, extract_video_url, extract_video_url_selenium

class FileDownloaderWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.default_output_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.init_ui()

    def init_ui(self):
        self.url_label = QLabel('Enter URL:')
        self.url_entry = QLineEdit()

        self.output_label = QLabel('Output directory:')
        self.output_entry = QLineEdit()
        self.output_entry.setText(self.default_output_path)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.on_browse_clicked)

        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.on_download_clicked)

        self.progress_bar = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_entry)
        layout.addWidget(self.browse_button)
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
        self.progress_bar.setValue(0)

        video_url = extract_video_url(url)
        if not video_url:
            video_url = extract_video_url_selenium(url)

        if video_url:
            def progress_callback(downloaded, total_size):
                progress = (downloaded / total_size) * 100
                self.progress_bar.setValue(int(progress))

            download_file(video_url, output_path, progress_callback)
        else:
            print("Video URL could not be extracted.")
