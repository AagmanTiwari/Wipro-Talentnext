# 01. Regular Expression to check if a string is octal
# An octal number consists of digits from 0 to 7 only.
# Given string ['789', '123', '004']


import re

# List of input strings
strings = ['789', '123', '004']

# Loop through each string to check if it contains only octal digits (0–7)
for s in strings:
    if re.fullmatch(r'[0-7]+', s):  # Match only if all characters are between 0 and 7
        print(f"{s} is octal")
    else:
        print(f"{s} is not octal")

# 02. Extract the user ID, domain name, and suffix from the following email addresses.
# Emails given:
# zuck@facebook.com  
# sunder33@google.com  
# jeff42@amazon.com

import re

# Multi-line string containing email addresses
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

# Regular expression to capture user ID, domain name, and suffix separately
pattern = r'(\w+)@(\w+)\.(\w+)'

# Extract all matches using the regex pattern
matches = re.findall(pattern, emails)

# Print each part of the email in a readable format
for user, domain, suffix in matches:
    print(f"User: {user}, Domain: {domain}, Suffix: {suffix}")


# 03. Split the following irregular sentence into proper words.
# Given sentence: sentence = "A, very   very; irregular_sentence"
# Expected output: A very very irregular sentence

import re

# Irregular sentence with extra punctuation and inconsistent spacing
sentence = "A, very   very; irregular_sentence"

# Replace commas, underscores, and semicolons with spaces
cleaned = re.sub(r'[,_;]', ' ', sentence)

# Split the sentence into words using one or more spaces
words = re.split(r'\s+', cleaned.strip())

# Join the cleaned words into a single sentence
print(' '.join(words))  # Output: A very very irregular sentence


# 04. Clean up the following tweet so that it contains only the user's message.

# Remove: URLs, hashtags, mentions, punctuations, RTs, and CCs.

# Tweet given: 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pX0d cc: @garybernhardt #rstats'
# Desired output: 'Good advice What I would do differently if I was learning to code today'

import re

# Original tweet including mentions, hashtags, links, and metadata
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pX0d cc: @garybernhardt #rstats"

# Remove URLs, Twitter mentions, hashtags, 'RT', and 'cc:'
cleaned = re.sub(r'http\S+|@\S+|#\S+|RT\s|cc:', '', tweet)

# Remove all punctuation except for words and spaces
cleaned = re.sub(r'[^\w\s]', '', cleaned)

# Print the final cleaned message
print(cleaned.strip())  # Output: Good advice What I would do differently if I was learning to code today



# 05. Extract all the text portions between the tags from the following HTML page:

# URL: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

# Goal: Get visible content inside HTML tags such as headings and paragraphs.

# Sample desired output:
# ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 
#  'This is a new paragraph! ', 'This is a another paragraph!', 
#  'This is a new sentence without a paragraph break, in bold italics.']


import requests
from bs4 import BeautifulSoup

# URL of the raw HTML content
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"

# Fetch the HTML content using requests
r = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Get all text between HTML tags and store in a list
texts = [tag.get_text() for tag in soup.find_all()]

# Print the extracted text
print(texts)

# 06. Given below list of words, identify the words that begin and end with the same
# character.
# civic
# trust
# widows
# maximum
# museums
# aa
# as

# List of input words
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

# Initialize an empty list to store matching words
matching_words = []

# Loop through each word in the list
for word in words:
    # Check if the first and last character of the word are the same
    if word[0] == word[-1]:
        matching_words.append(word)

# Print the matching words
print("Words that begin and end with the same character:", matching_words)




