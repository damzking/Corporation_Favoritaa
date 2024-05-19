import json

notebook_file = 'TSRA-Favorita.ipynb'

with open(notebook_file, 'r', encoding='utf-8') as f:
    try:
        json.load(f)
        print("Notebook is valid JSON.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
