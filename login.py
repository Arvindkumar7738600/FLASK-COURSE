from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)

#home page Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        #USING NESTED IF ELSE STATEMENT
        # Simple authentication logic (for demonstration purposes)
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return Response('Invalid credentials. Try again.', mimetype='text/plain', status=401) #minetype is used to specify the type of content being returned, in this case, plain text. The status code 401 indicates that the request was unauthorized due to invalid credentials.
    
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''