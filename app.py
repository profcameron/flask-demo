import datetime
import random
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

def bergen():
    html_content = """
    <html>
    <head>
        <title>College Colors Page</title>
        <style>
            body { background-color: white; color: black; text-align: center; font-family: Arial, sans-serif; }
            h1 { color: #660099; }
            p { color: #FF6600; font-weight: bold; }
            .button {
                background-color: #FF6600; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                text-decoration: none; 
                font-size: 16px;
                cursor: pointer;
                border-radius: 5px;
            }
            .button:hover {
                background-color: #660099;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Our College Page</h1>
        <p>This page uses our college colors!</p>
        <a href="#" class="button">Learn More</a>
    </body>
    </html>
    """
    return Response(html_content, mimetype="text/html")

def calculations():
    now = datetime.date.today()
    rand_num = random.randint(1, 100)
    # The format string is necessary here to display the variables 
    html_content = f"""
    <html>
    <head>
        <title>Date, Time, and Random Number</title>
        <style>
            body {{ background-color: white; color: black; text-align: center; font-family: Arial, sans-serif; }}
            h1 {{ color: #660099; }}
            p {{ color: #FF6600; font-size: 20px; }}
        </style>
    </head>
    <body>
        <h1>Current Date and Time</h1>
        <h1>Random Number</h1>
    </body>
    </html>
    """
    return Response(html_content, mimetype="text/html")

if __name__ == "__main__":
    app.run(debug=True)
