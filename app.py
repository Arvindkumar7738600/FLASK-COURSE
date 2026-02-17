from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I Am Arvind Kumar'

@app.route("/about")
def about():
    return 'I am a software developer with a passion for creating innovative solutions. I have experience in various programming languages and frameworks, and I enjoy working on projects'


@app.route("/contact")
def contact():
    return 'You can contact me at +91-1234567890'