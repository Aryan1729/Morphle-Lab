Flask System Monitor App


This is a simple Flask application that displays system information, including the current user, server time (IST), and output of the top command.

Features

Displays system username

Shows current server time in IST timezone

Fetches and displays system process details using top

Installation

Prerequisites

Python 3.x installed

Flask and other dependencies installed

Install Dependencies

Run the following command to install the required dependencies:

pip install flask pytz

Usage

Running the Application

Start the Flask application by running:

python app.py

By default, the app runs on port 5000. You can access it in a browser at:

http://127.0.0.1:5000/htop

To access from another device on the same network, use:

http://<your-ip-address>:5000/htop

Deployment

For production use, consider deploying with Gunicorn and NGINX.

Deploying with Gunicorn

You can run the Flask app using Gunicorn for better performance:

gunicorn -w 4 -b 0.0.0.0:5000 app:app

Setting Up Nginx as a Reverse Proxy

To serve the Flask application using Nginx, add the following configuration in your Nginx config file:

server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Restart Nginx to apply the changes:

sudo systemctl restart nginx

Testing

To test if the app is working correctly, you can use:

curl http://127.0.0.1:5000/htop

This should return the system information in HTML format.

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

Contact

For any queries or suggestions, feel free to reach out via email or open an issue on GitHub.

