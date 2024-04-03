import requests
import json
from datetime import datetime, timedelta

channel_id = 2484037 # PUT CHANNEL ID HERE

BASE_URL = "https://api.thingspeak.com/channels/{}/feeds.json".format(channel_id)

print(BASE_URL)

def get_data():
    res = requests.get(BASE_URL)
    data = json.loads(res.text)
    # print(data)

    return data['feeds']

def average_crowd_size(data):
    NUM_DAYS = 7

    # Get all the data from the past week
    today = datetime.now()
    past_week = today - timedelta(days=NUM_DAYS)

    # Get the data from the past week
    data_past_week = [entry for entry in data if datetime.strptime(entry['created_at'], '%Y-%m-%dT%H:%M:%SZ') > past_week]

    # Calculate the average crowd size
    total = 0
    for entry in data_past_week:
        total += int(entry['field1'])

    average = total / len(data_past_week)
    print("Average crowd size for the past week: ")
    print(average)

if __name__ == '__main__':
    # print(time.time())
    data = get_data()
    average_crowd_size(data)
