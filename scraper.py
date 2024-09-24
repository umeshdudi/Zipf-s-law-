import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import plotly.express as px
import pandas as pd

def scrape_text(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return ""
    
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

def clean_and_count_words(text):
    # Remove special characters and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def plot_all_words(word_counts):
    # Sort words by frequency in descending order and prepare data for Plotly
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    words, counts = zip(*sorted_word_counts.items())
    
    # Create a DataFrame for Plotly
    df = pd.DataFrame({'Words': words, 'Frequency': counts})  # Include all words
    
    # Create a bar chart with color gradient based on frequency
    fig = px.bar(df, x='Words', y='Frequency', 
                 title='Word Frequencies in the Webpage',
                 labels={'Words': 'Words', 'Frequency': 'Frequency'},
                 color='Frequency',  # Use Frequency for color
                 color_continuous_scale='Rainbow')  # You can choose other color scales as well
    
    fig.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels
    fig.show()

def main(url):
    text = scrape_text(url)
    if text:
        word_counts = clean_and_count_words(text)
        plot_all_words(word_counts)

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to scrape: ")
    main(url)


#https://www.e-education.psu.edu/writingpersonalstatementsonline/p4_p4.html