from flask import Flask, render_template
import requests
import json
app = Flask(__name__)
@app.route('/')
def data():
    # Replace YOUR_CHANNEL_ID and YOUR_READ_API_KEY with your own values
    channel_id = '2022689'
    read_api_key = 'M546L1X4JB2J8H6W'
    # Make an HTTP GET request to retrieve the data
    url = f'https://api.thingspeak.com/channels/{channel_id}/fields/1.json?api_key={read_api_key}'
    response = requests.get(url)
    # Extract the data from the response and return it as a list
    if response.status_code == 200:
        data = response.json()['feeds']
        list3 = [feed['created_at'] for feed in data]
        values = [d['field1'] for d in data]
        with open('na.json') as f:
            bird_names = json.load(f)
        with open('lo.json') as l:
            location_name = json.load(l)
        list1 = []
        list2 = []
        for value in values:
            bird_name = bird_names.get(value, 'Unknown')
            list1.append(bird_name) 
            location = location_name.get(value, 'Unknown')
            list2.append(location)
        return render_template('data.html',list1=list1,list2=list2,list3=list3)
        #return render_template('data.html', values=values)
    else:
        return 'Error retrieving data'
if __name__ == '__main__':
    app.run()