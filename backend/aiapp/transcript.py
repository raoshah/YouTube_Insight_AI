from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import requests, os

def get_video_id(youtube_url):
    query = urlparse(youtube_url)
    return parse_qs(query.query)['v'][0]

def video_text():
    video_url = "https://www.youtube.com/watch?v=mxcMhYtHERM"
    video_id = get_video_id(video_url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = "\n".join([line["text"] for line in transcript])
    print(text)
    return text


def transcript():
    print(os.environ.get('API_KEY'))
    api_key = os.environ.get('API_KEY')
    prompt = f"Based on this video transcript, give me a cooking recipe:\n\n{video_text()}"

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "meta-llama/llama-4-maverick:free", 
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    result = response.json()
    print(result)
    
    return result['choices'][0]['message']['content']

