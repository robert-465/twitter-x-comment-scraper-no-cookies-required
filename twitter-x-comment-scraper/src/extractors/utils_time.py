thonfrom datetime import datetime

def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def format_duration(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}m {seconds}s"