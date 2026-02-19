from flask import Flask, request


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



#Get and Post  means that the route can handle both GET and POST HTTP methods. 
#GET is typically used to retrieve data from the server, while POST is used to send data to the server for processing. By specifying both methods, the route can handle requests that either fetch information or submit data, making it versatile for different types of interactions with the client.
#@app.route("/submit", methods=["GET", "POST"])

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST": 
        # Handle POST request (e.g., form submission)
        data = request.form.get("data")
        return f"Data received: {data}"
    else:
        # Handle GET request (e.g., display form)
        return '''
            <form method="post">
                <input type="text" name="data" placeholder="Enter some data">
                <input type="submit" value="Submit">
            </form>
        '''