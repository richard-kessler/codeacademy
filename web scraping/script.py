import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Request
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

# Convert Request to Content
webpage_content = webpage_response.content

# Parse Content with bs
soup = BeautifulSoup(webpage_content, "html.parser")
print(soup)

# Find all rating tags
ratings_links = soup.find_all(attrs={"class": "Rating"})

ratings = []
for link in ratings_links:
  ratings.append(float(link))

