from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return render_template('result.html', name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
