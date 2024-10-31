## use for this
## python script.py input.json output.txt

import json
import re
import sys

def extract_hashes_from_json(data):
    hashes = set()
    hash_patterns = {
        'MD5': r'\b[a-fA-F0-9]{32}\b',
        'SHA1': r'\b[a-fA-F0-9]{40}\b',
        'SHA256': r'\b[a-fA-F0-9]{64}\b'
    }
    
    # recursively look for the patterns of hashes above
    def search_hashes(value):
        if isinstance(value, str):
            for pattern in hash_patterns.values():
                found_hashes = re.findall(pattern, value)
                hashes.update(found_hashes)
        elif isinstance(value, dict):
            for v in value.values():
                search_hashes(v)
        elif isinstance(value, list):
            for item in value:
                search_hashes(item)
                
    search_hashes(data)
    return hashes

def main(input_file, output_file):
    try:
        # load JSON 
        with open(input_file, 'r') as file:
            data = json.load(file)

        # extract
        hashes = extract_hashes_from_json(data)

        # write hashes to output file with new lines
        with open(output_file, 'w') as file:
            for h in sorted(hashes):
                file.write(h + '\n')

        print(f"Successfully extracted {len(hashes)} hashes to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)
