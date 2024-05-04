import os
import argparse
from src.core.youtube_downloader import download_youtube_video

def run_cli():
    default_output_path= os.path.join(os.path.expanduser('~'), 'Downloads')
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="URL of the YouTube video")
    parser.add_argument("-o", "--output", default=default_output_path, help="Output directory for downloaded video")
    parser.add_argument("-r", "--resolution", default=None, help="Desired resolution of the video (e.g., '720p', '480p', '360p')")
    args = parser.parse_args()
    
    download_youtube_video(args.url, args.output, args.resolution)
