from youtube_transcript_api import YouTubeTranscriptApi
import requests
import os
import re
import time
from dotenv import load_dotenv

load_dotenv()
channel_id = os.environ.get("YT_CHANNEL_ID")
yt_api_key = os.environ.get("YT_API_KEY")

def get_video_ids_from_channel(yt_api_key, channel_id):
    # YouTube API URL for getting videos from a channel
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "type": "video",
        "maxResults": 50,  # Maximum allowed by the API
        "key": yt_api_key
    }

    video_ids = []
    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            raise Exception("Failed to fetch video data")

        data = response.json()
        video_ids.extend([item['id']['videoId'] for item in data['items']])

        # Check if there is a nextPageToken, and if so, set it in params for the next request
        page_token = data.get("nextPageToken")
        if not page_token:
            break  # Exit the loop if no more pages
        params['pageToken'] = page_token

    return video_ids

def get_video_details(yt_api_key, video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={yt_api_key}&part=snippet"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if ('items' in data and len(data['items'])) > 0:
            return data['items'][0]['snippet']['title']
    return None

def sanitize_filename(title):
    # Remove invalid characters from file names
    return re.sub(r'[^a-zA-Z0-9 \-]', '', title)

def transcribe_and_save(yt_api_key, video_ids):
    for video_id in video_ids:
        title = get_video_details(yt_api_key, video_id)
        if title:
            title = sanitize_filename(title)
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = "\n".join([entry['text'] for entry in transcript])
                with open(f"andrews-podcast/{title}.txt", "w", encoding="utf-8") as file:
                    file.write(transcript_text)
                print("successfully transcripted video #:",(video_ids.index(video_id)+1))
            except Exception as e:
                print(f"Error transcribing video {video_id}: {e}")

start_time = time.time()

video_ids = get_video_ids_from_channel(yt_api_key, channel_id)
# print(video_ids)
print("Total videos in channel: ",len(video_ids))
transcribe_and_save(yt_api_key, video_ids)

end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")