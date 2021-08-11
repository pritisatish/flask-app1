
from flask import Flask

app = Flask(__name__)

@app.route('/')
#@app.route('/home')
def home_view():
    return "<h1>Welcome to NSOFT</h1>"

if __name__ == '__main__':
    app.run(debug=True)
