import time
import json
import requests
import googletrans

def check_internet_connectivity():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    print("\nWelcome To Project Indus Hackathon!\n")
    time.sleep(1)
    print("Kindly Keep The Hindi Text In The 'input_data.txt' File For Conversion\n")
    time.sleep(1)
    if check_internet_connectivity():
        print("Internet Connection Available! Dialect Conversion Started...")
        print(f"\nGoogle Translate Supported Languages => {googletrans.LANGUAGES}\n")
        with open('input_file.txt', encoding='utf-8') as input_file:
            input_data = input_file.readlines()
            translator = googletrans.Translator()
            print(f"Input File Raw Data => {input_data}")
            detection = translator.detect(str(input_data))
            print(f"Detection => {detection}\n")
            with open('dialect_list.json') as dialect_list:
                dialectList = json.load(dialect_list)["data"]
                for dialect_item in dialectList:
                    print(f"Translating Hindi Input To {dialect_item['dialect']} Dialect Of Region {dialect_item['region']}...")
                    time.sleep(1)
                    try:
                        if dialect_item["code"] != "" and dialect_item["code"] in googletrans.LANGUAGES:
                            translation  = translator.translate(str(input_data), dest=str(dialect_item["code"]))
                            print(f"{translation}\n")
                        else:
                            print(f"Dialect => {dialect_item['dialect']} Unsupported By Google Translate...\n")
                    except Exception as e:
                        print(f"Exception => {e}\n")
                        continue
        print("Internet Connection Available! Dialect Conversion Finished...")
    else:
        print("Internet Connection Unavailable! Dialect Conversion Skipped...")

if __name__ == "__main__":
    main()
    
# https://cloud.google.com/translate/docs/languages
# https://pypi.org/project/googletrans/4.0.0rc1/
# pip install googletrans==4.0.0rc1 --target=destination_directory
# https://pypi.org/project/requests/
# pip install requests --target=destination_directory