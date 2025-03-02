# Flask Workshop

## Introduction
Welcome to the Flask Workshop! This hands-on session will introduce you to Flask, a lightweight web framework for Python. By the end of this workshop, you'll have a working Flask web application, even if you've never used Flask before.

## Prerequisites
To participate in this workshop, you need to have Python installed on your system. If you do not have Python installed, you can download it from the official website:

[Download Python](https://www.python.org/downloads/)

Make sure to select the option to **Add Python to PATH** during installation.

### Installing Flask with pip
Flask and its dependencies can be easily installed using `pip`, Python’s package manager. To install Flask, run the following command in your terminal or command prompt:

```sh
pip install flask
```

To verify that Flask is installed, run:

```sh
python -m flask --version
```

## Using Git
This workshop uses Git to manage and distribute the project files. If you do not have Git installed, you can download it from:

[Download Git](https://git-scm.com/downloads)

### Setting Up Git
After installing Git, you need to configure it by running the following commands in your terminal or command prompt:

```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

To verify that Git is installed and configured correctly, run:

```sh
git --version
```

### Cloning the Repository
To clone the repository, open a terminal or command prompt and run:

```sh
git clone https://github.com/profcameron/flask-demo.git
```

Then, navigate to the project directory:

```sh
cd flask-demo
```

## Alternative: Downloading a ZIP File
If you prefer not to use Git, you can download the project as a ZIP file:

1. Go to [Flask Workshop GitHub Repository](https://github.com/profcameron/flask-demo).
2. Click on the **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file to your preferred location.
5. Open a terminal or command prompt and navigate to the extracted folder.

## Running the Flask Application
To start the Flask web server, run the following command inside the project directory:

```sh
python app.py
```

Once the server is running, open your web browser and go to:

```
http://127.0.0.1:5000
```

This will load the main page of your Flask application.

