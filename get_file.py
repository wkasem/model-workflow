import urllib.request
from pathlib import Path
import sys
import os
name = sys.argv[0]
url = sys.argv[1]

url_path = Path(url)

urllib.request.urlretrieve(url, os.getenv('WORKSPACE_DIR') + name + ".mp4")
