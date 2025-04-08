from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import RequestBlocked

from urllib.parse import urlparse, parse_qs
import requests, os, time
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()



def proxy_list():
    url = "https://www.sslproxies.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find("table").find_all("tr")

    proxy_list = []

    for row in rows:
        cols = row.find_all('td')

        if len(cols) < 7:
            continue

        
        ip = cols[0].text.strip()
        port = cols[1].text.strip()
        https = cols[6].text.strip()

        if https.lower() == "yes":
            proxy = f"http://{ip}:{port}"
            proxy_list.append(proxy)
    
    return proxy_list



def get_video_id(youtube_url):
    query = urlparse(youtube_url)
    return parse_qs(query.query)['v'][0]


def try_with_proxy(video_id, proxy_list):
    for proxy in proxy_list:
        try:
            print(f"Trying with proxy: {proxy}")
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id,
                proxies={"https": proxy}
            )
            return transcript
        except RequestBlocked:
            print(f"Blocked by YouTube with proxy: {proxy}")
        except Exception as e:
            print(f"Proxy failed ({proxy}): {e}")
        time.sleep(0.5)
    return None


def video_text():
    video_url = "https://www.youtube.com/watch?v=mxcMhYtHERM"
    video_id = get_video_id(video_url)
    transcript = try_with_proxy(video_id, proxy_list())

    if not transcript:
        print("❌ Failed to fetch transcript.")
        return "Transcript could not be retrieved."

    text = "\n".join([line["text"] for line in transcript])
    print(text)
    return text


def transcript():
    api_key = os.environ.get('API_KEY')
    if not api_key:
        print("❌ API_KEY not found in environment variables.")
        return

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

    if "choices" not in result:
        print("❌ API Error:", result)
        return "Failed to get recipe."

    print(result['choices'][0]['message']['content'])
    return result['choices'][0]['message']['content']


