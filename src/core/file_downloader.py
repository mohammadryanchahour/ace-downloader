import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def download_file(url, output_path, progress_callback=None):
    """
    Download a file from a URL.

    Args:
        url (str): The URL of the file.
        output_path (str): The path where the file will be saved.
        progress_callback (function, optional): Callback function for progress updates.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        if os.path.isdir(output_path):
            filename = os.path.join(output_path, os.path.basename(url))
        else:
            filename = output_path

        total_length = response.headers.get('content-length')

        with open(filename, 'wb') as f:
            if total_length is None:  # No content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in response.iter_content(chunk_size=4096):
                    if chunk:
                        dl += len(chunk)
                        f.write(chunk)
                        if progress_callback:
                            progress_callback(dl, total_length)
        
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Error downloading file: {e}")

def extract_video_url(page_url):
    """
    Extract video URL from a webpage.

    Args:
        page_url (str): The URL of the webpage.

    Returns:
        str: The extracted video URL.
    """
    try:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for video tag
        video_tag = soup.find('video')
        if video_tag:
            source_tag = video_tag.find('source')
            if source_tag:
                return source_tag['src']

        # Check for video in scripts or other tags
        for script in soup.find_all('script'):
            if 'video' in script.text:
                # Implement further parsing logic here if needed
                pass

        return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None
    except Exception as e:
        print(f"Error extracting video URL: {e}")
        return None

def extract_video_url_selenium(page_url):
    """
    Extract video URL from a JavaScript-heavy webpage using Selenium.

    Args:
        page_url (str): The URL of the webpage.

    Returns:
        str: The extracted video URL.
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service('/home/kakkarott/Tools/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(page_url)

        # Example for finding video tag
        video_tag = driver.find_element(By.TAG_NAME, 'video')
        if video_tag:
            source_tag = video_tag.find_element(By.TAG_NAME, 'source')
            if source_tag:
                video_url = source_tag.get_attribute('src')
                driver.quit()
                return video_url

        # Example for finding video in scripts or other tags
        scripts = driver.find_elements(By.TAG_NAME, 'script')
        for script in scripts:
            if 'video' in script.get_attribute('innerHTML'):
                # Implement further parsing logic here if needed
                pass

        driver.quit()
        return None
    except Exception as e:
        print(f"Error extracting video URL with Selenium: {e}")
        return None

