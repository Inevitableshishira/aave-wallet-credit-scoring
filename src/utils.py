import requests
import json
from io import BytesIO

def load_json_from_gdrive(gdrive_url):
    file_id = gdrive_url.split("/d/")[1].split("/")[0]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(download_url)
    response.raise_for_status()
    return json.loads(response.content)
