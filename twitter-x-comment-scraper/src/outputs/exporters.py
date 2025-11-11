thonimport json
import os

class Exporter:
    def __init__(self, output_file):
        self.output_file = output_file

    def export_data(self, data):
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)