# Zipf-s-law-
built a Python program that scrapes a webpage,and proves ziph's law


Web Scraping: Using the requests library, you send an HTTP GET request to retrieve the HTML content of a specified URL. You check if the response is successful (status code 200) before proceeding.

HTML Parsing: The BeautifulSoup library is employed to parse the HTML content, extracting all text from the page. This step is crucial for filtering out any HTML tags and irrelevant data.

Text Cleaning: A regular expression (re.findall) is used to identify and extract words from the text. This process includes converting all text to lowercase to ensure that word counts are case-insensitive, and removing special characters for accurate counting.

Word Frequency Counting: The Counter class from the collections module counts the occurrences of each word in the cleaned text, producing a dictionary-like object that provides easy access to word frequencies.

Data Visualization: You sort the word counts in descending order and prepare the data for visualization using pandas. The plotly.express library is then utilized to create a bar chart that displays word frequencies, with colors representing frequency levels through a color gradient.

User Interaction: The program prompts the user to input a URL, making it interactive. This allows users to analyze different webpages without modifying the code.

Dynamic Presentation: The resulting bar chart is presented with aesthetically pleasing features, such as rotated x-axis labels for better readability, enhancing user experience and understanding of the data.
