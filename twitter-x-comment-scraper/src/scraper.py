thonimport requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO)

def fetch_comments(tweet_url):
    """
    Fetches comments from a given tweet URL.
    Args:
        tweet_url (str): URL of the tweet to scrape comments from.
    Returns:
        list: List of comments extracted from the tweet.
    """
    try:
        logging.info(f"Fetching comments for tweet: {tweet_url}")
        response = requests.get(tweet_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        comments = []

        for comment in soup.find_all('div', {'data-testid': 'tweetText'}):
            comment_data = {
                'commentId': comment.get('data-tweet-id'),
                'replyContent': comment.get_text(),
                'createdAt': comment.find_next('time').get('datetime')
            }
            comments.append(comment_data)
        
        logging.info(f"Extracted {len(comments)} comments.")
        return comments
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching tweet: {e}")
        return []

def save_comments_to_file(comments, filename='comments.json'):
    """
    Saves the extracted comments to a JSON file.
    Args:
        comments (list): List of comment dictionaries.
        filename (str): File name to save the comments.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(comments, f, indent=4)
        logging.info(f"Comments saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving comments: {e}")

if __name__ == "__main__":
    tweet_url = "https://twitter.com/some_tweet"  # Example tweet URL
    comments = fetch_comments(tweet_url)
    save_comments_to_file(comments)