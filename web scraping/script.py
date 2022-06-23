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

# Extract rate and convert to float value
ratings = [float(rate.get_text()) for rate in ratings_links[1:]]
#print(ratings)

# Histogram to show ratings
plt.hist(ratings)
plt.show()

# Find chocolatier companies
all_choc = [choc.get_text() for choc in soup.select(".Company")[1:]]
#print(all_choc)

# Create Dataframe for all companies and ratings
df = pd.DataFrame({"Company": all_choc, "Rating": ratings})
#print(df)

# Find Top 10 companies by rating
mean_ratings = df.groupby("Company").Rating.mean()
top_ten = mean_ratings.nlargest(10)
#print(top_ten)

#list of cocoa percentages
cocoa_pct = [int(float(pct.get_text().strip("%"))) for pct in soup.select(".CocoaPercent")[1:]]
#print(cocoa_pct)

# Add cocoa_pct to existing dataframe
df["CocoaPercentage"] = cocoa_pct
#print(df)

# Generate scatter plot of ratings vs % cocoa
plt.scatter(df["CocoaPercentage"], df["Rating"], color="g")
plt.title("Rating vs Cocoa %")
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
