thonimport requests
from bs4 import BeautifulSoup
from datetime import datetime

class TwitterParser:
    def __init__(self, url):
        self.url = url

    def scrape_comments(self):
        print(f"Scraping comments from {self.url}")
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        comments = self.parse_comments(soup)
        return comments

    def parse_comments(self, soup):
        comments = []
        for comment_div in soup.find_all('div', class_='tweet'):
            comment = {
                'commentId': comment_div['data-tweet-id'],
                'userId': comment_div['data-user-id'],
                'isBlueVerified': 'verified' in comment_div['class'],
                'twitterName': comment_div.find('strong').text.strip(),
                'twitterUsername': comment_div.find('a', class_='username').text.strip(),
                'viewCount': self.get_view_count(comment_div),
                'replyContent': comment_div.find('p').text.strip(),
                'likeCount': self.get_like_count(comment_div),
                'replyCount': self.get_reply_count(comment_div),
                'retweetCount': self.get_retweet_count(comment_div),
                'quoteCount': self.get_quote_count(comment_div),
                'bookmarkCount': self.get_bookmark_count(comment_div),
                'createdAt': datetime.now().strftime('%a %b %d %H:%M:%S +0000 %Y')
            }
            comments.append(comment)
        return comments

    def get_view_count(self, comment_div):
        return comment_div.find('span', class_='view-count').text if comment_div.find('span', class_='view-count') else 0

    def get_like_count(self, comment_div):
        return int(comment_div.find('span', class_='like-count').text.replace(',', ''))

    def get_reply_count(self, comment_div):
        return int(comment_div.find('span', class_='reply-count').text.replace(',', ''))

    def get_retweet_count(self, comment_div):
        return int(comment_div.find('span', class_='retweet-count').text.replace(',', ''))

    def get_quote_count(self, comment_div):
        return int(comment_div.find('span', class_='quote-count').text.replace(',', ''))

    def get_bookmark_count(self, comment_div):
        return int(comment_div.find('span', class_='bookmark-count').text.replace(',', ''))