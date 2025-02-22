from flask import Flask
from pytz import timezone
import os
import subprocess
from datetime import datetime


app = Flask(__name__)


@app.route('/htop')
def htop():

    username = os.getenv('USER') or os.getlogin()

 
    ist_time = datetime.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')

  
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

   
    response = f"""
    <html>
        <body>
            <h1>System Info</h1>
            <p><strong>Name:</strong> Aryan Raj</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)