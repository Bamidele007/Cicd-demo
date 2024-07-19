from flask import Flask
app = Flask(__name__)
# Before
from werkzeug.urls import url_quote

@app.route("/")
def hello():
   return "Hello Realzzy007 World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
