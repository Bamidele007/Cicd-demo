from flask import Flask
from urllib.parse import quote as url_quote
app = Flask(__name__)

# Other routes and logic
@app.route("/")
def hello():
   return "Hello Realzzy007 World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
