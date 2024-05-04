# download_manager/src/core/youtube_downloader.py
import os
from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    print(f"\rDownloading... {progress:.2f}%", end='')

def on_complete(stream, file_path):
    print("\nDownload completed!")

def download_youtube_video(video_url, output_path, resolution=None):
    """
    Download a YouTube video with progress tracking.

    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): The path where the video will be saved.
        resolution (str): The desired resolution of the video (e.g., "720p", "480p", "360p", "1080p"). If None, the highest resolution will be used.
    """
    try:
        yt = YouTube(video_url)

        # Set callbacks for progress and completion
        yt.register_on_progress_callback(on_progress)
        yt.register_on_complete_callback(on_complete)

        if resolution:
            video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', resolution=resolution, only_video=True).first()
            audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).first()
        else:
            video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).first()
            audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).first()

        if video_stream and audio_stream:
            video_stream.download(output_path=output_path, filename='video.mp4')
            audio_stream.download(output_path=output_path, filename='audio.mp4')

            os.system(f'ffmpeg -i {os.path.join(output_path, "video.mp4")} -i {os.path.join(output_path, "audio.mp4")} -c:v copy -c:a copy {os.path.join(output_path, "output.mp4")}')

            os.remove(os.path.join(output_path, "video.mp4"))
            os.remove(os.path.join(output_path, "audio.mp4"))

            print(f"\nVideo downloaded successfully to {os.path.join(output_path, 'output.mp4')}")
        else:
            print(f"\nNo available streams for resolution: {resolution}")

    except Exception as e:
        print(f"\nError downloading video: {e}")
