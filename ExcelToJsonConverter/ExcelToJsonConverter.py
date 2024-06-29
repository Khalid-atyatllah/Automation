import pandas as pd
import json

class ExcelToJsonConverter:
    def __init__(self, excel_path, json_path):
        self.excel_path = excel_path
        self.json_path = json_path
        self.df = None

    def load_excel(self):
        self.df = pd.read_excel(self.excel_path)

    def create_json_structure(self, info1, info2, info3):
        json_structure = {
            "fields": {
                "info1": info1,
                "info2": info2,
                "info3": info3
            }
        }
        return json_structure

    def process_data(self):
        self.df['all'] = self.df.apply(
            lambda row: self.create_json_structure(
                row['info1'],
                row['info2'],
                row['info3']
            ),
            axis=1
        )

    def save_to_json(self):
        json_list = self.df['all'].tolist()
        with open(self.json_path, 'w') as fp:
            json.dump(json_list, fp, indent=4)
        print("JSON file has been created successfully.")

    def convert(self):
        self.load_excel()
        self.process_data()
        self.save_to_json()
