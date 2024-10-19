import requests

def get_video_comments(video_id):
    api_key = 'AIzaSyCkVIWYstX31aqA2OzcKD30QEqDTWWf4zg'  # Paste the API key here
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in data['items']]
    return comments