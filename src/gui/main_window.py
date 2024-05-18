import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from src.gui.file_downloader_gui import FileDownloaderWidget
from src.gui.youtube_downloader_gui import YouTubeDownloaderWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ace Downloader')
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Create tab for file downloader
        file_downloader_tab = QWidget()
        file_downloader_widget = FileDownloaderWidget()
        file_downloader_layout = QVBoxLayout()
        file_downloader_layout.addWidget(file_downloader_widget)
        file_downloader_tab.setLayout(file_downloader_layout)
        tab_widget.addTab(file_downloader_tab, 'File Downloader')

        youtube_downloader_tab = QWidget()
        youtube_downloader_widget = YouTubeDownloaderWidget()
        youtube_downloader_layout = QVBoxLayout()
        youtube_downloader_layout.addWidget(youtube_downloader_widget)
        youtube_downloader_tab.setLayout(youtube_downloader_layout)
        tab_widget.addTab(youtube_downloader_tab, 'YouTube Downloader')

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.resize(500, 300)

def run_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
