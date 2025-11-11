thonfrom textblob import TextBlob
import logging

logging.basicConfig(level=logging.INFO)

def analyze_sentiment(comment_text):
    """
    Analyzes the sentiment of a given comment.
    Args:
        comment_text (str): The text of the comment.
    Returns:
        dict: Sentiment analysis result including polarity and subjectivity.
    """
    try:
        logging.info(f"Analyzing sentiment for comment: {comment_text}")
        blob = TextBlob(comment_text)
        sentiment = {
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity
        }
        return sentiment
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return {}

if __name__ == "__main__":
    sample_comment = "This is a sample tweet. So cool!"
    sentiment = analyze_sentiment(sample_comment)
    print(f"Sentiment analysis: {sentiment}")