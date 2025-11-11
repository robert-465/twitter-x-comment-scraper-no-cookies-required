thonimport json
import logging

logging.basicConfig(level=logging.INFO)

def export_results(comments, filename='output.json'):
    """
    Exports the results to a JSON file.
    Args:
        comments (list): List of comments to export.
        filename (str): Output file name.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(comments, f, indent=4)
        logging.info(f"Results exported to {filename}")
    except Exception as e:
        logging.error(f"Error exporting results: {e}")