from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"🔔 [{datetime.now()}] New Alert Received!")

    if data:
        symbol = data.get('symbol', 'UNKNOWN')
        price = data.get('price', '0.000')
        interval = data.get('interval', 'UNKNOWN')
        signal = data.get('signal', 'UNKNOWN')

        print(f"📈 Symbol   : {symbol}")
        print(f"💰 Price    : {price}")
        print(f"🕒 Interval : {interval}")
        print(f"🚦 Signal   : {signal}")

        # 💾 Save alert to logs.txt
        with open("logs.txt", "a") as f:
            f.write(f"[{datetime.now()}] {symbol} | {price} | {interval} | {signal}\n")

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
