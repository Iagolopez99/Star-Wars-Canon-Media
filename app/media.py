import subprocess
import pandas as pd

# Run scraper to get the latest media data
subprocess.run(["python", "app/scraper.py"])

# Load the updated media table
media_df = pd.read_csv("data/all_media.csv")
