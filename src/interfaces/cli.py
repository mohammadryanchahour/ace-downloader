import sys
import os
from src.core.download_manager import DownloadManager
from src.core.youtube_downloader import YouTubeDownloader

class CLI:
    def __init__(self):
        self.download_manager = DownloadManager()

    def show_menu(self):
        print("Welcome to the Download Manager")
        print("1. Download YouTube Video")
        print("2. Exit")

    def get_user_choice(self):
        choice = input("Enter your choice: ")
        return choice

    def download_youtube_video(self):
        video_url = input("Enter the YouTube video URL: ")
        output_path = input("Enter the output path: ")
        resolution = input("Enter the desired resolution (e.g., 720p, leave blank for highest): ") or None
        
        try:
            downloader = YouTubeDownloader(video_url)
            self.download_manager.add_to_queue(downloader)
            self.download_manager.start_downloads()
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_choice()
            if choice == "1":
                self.download_youtube_video()
            elif choice == "2":
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
