thonimport json
import os
import time
from extractors.twitter_parser import TwitterParser
from outputs.exporters import Exporter
from config.settings import SETTINGS

def main():
    twitter_url = SETTINGS['twitter_url']
    output_file = SETTINGS['output_file']
    
    parser = TwitterParser(twitter_url)
    comments = parser.scrape_comments()
    print(f"Scraped {len(comments)} comments.")
    
    exporter = Exporter(output_file)
    exporter.export_data(comments)
    print(f"Data exported to {output_file}.")

if __name__ == "__main__":
    main()