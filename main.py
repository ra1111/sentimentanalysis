# Import the necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import PyPDF2

# Download the vader_lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Function to read text from a PDF file
def read_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

# Function to perform sentiment analysis on text
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# Read text from PDF
text = read_pdf('sample.pdf')

# Perform sentiment analysis on the text
sentiment_scores = analyze_sentiment(text)

# Print the sentiment scores
print(sentiment_scores)
