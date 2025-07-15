import sys
import os
from flask import Flask, request, jsonify
from datetime import datetime

# 👇 Ensure logs print immediately on Render
sys.stdout.reconfigure(line_buffering=True)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    timestamp = datetime.now()

    print(f"\n🔔 [{timestamp}] New Alert Received!")

    if data:
        symbol = data.get('symbol', 'UNKNOWN')
        price = data.get('price', 'UNKNOWN')
        interval = data.get('interval', 'UNKNOWN')
        signal = data.get('signal', 'UNKNOWN')

        print(f"📈 Symbol   : {symbol}")
        print(f"💰 Price    : {price}")
        print(f"🕒 Interval : {interval}")
        print(f"🚦 Signal   : {signal}")

        # Save to log file
        with open("logs.txt", "a") as f:
            f.write(f"[{timestamp}] {data}\n")

        return jsonify({'status': 'received'}), 200

    else:
        print("❌ No data received.")
        return jsonify({'status': 'error', 'message': 'No data received'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
