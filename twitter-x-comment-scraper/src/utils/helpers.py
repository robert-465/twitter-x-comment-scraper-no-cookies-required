thonimport logging

logging.basicConfig(level=logging.INFO)

def filter_comments_by_sentiment(comments, min_polarity=0.1):
    """
    Filters comments based on sentiment polarity.
    Args:
        comments (list): List of comment dictionaries.
        min_polarity (float): Minimum polarity value to filter positive comments.
    Returns:
        list: List of comments with sentiment polarity greater than min_polarity.
    """
    filtered_comments = []
    for comment in comments:
        if comment.get('sentiment', {}).get('polarity', 0) >= min_polarity:
            filtered_comments.append(comment)
    
    logging.info(f"Filtered {len(filtered_comments)} positive comments.")
    return filtered_comments