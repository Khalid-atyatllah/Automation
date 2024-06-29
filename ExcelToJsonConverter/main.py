import json
from ExcelToJsonConverter import ExcelToJsonConverter

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def main():
    config = load_config('config.json')
    excel_path = config['excel_path']
    json_path = config['json_path']
    
    converter = ExcelToJsonConverter(excel_path, json_path)
    converter.convert()

if __name__ == "__main__":
    main()
