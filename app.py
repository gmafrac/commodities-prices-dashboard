from flask import Flask, render_template, Response
import json
import time
import random

app = Flask(__name__)

# Load the data
with open('data.json', 'r') as f:
    data = json.load(f)

# Function to generate random data
def generate_data():
    while True:
        for commodity in data['commodities']:
            # Generate random price update
            new_price = random.uniform(0.9, 1.1) * commodity['prices'][-1]
            commodity['prices'].append(new_price)
        yield f"data: {json.dumps(data)}\n\n"
        time.sleep(2)  # Simulate delay

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(generate_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)