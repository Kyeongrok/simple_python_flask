from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    msg = f"hello{os.getenv('HELLO')}"
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)
