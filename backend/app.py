from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello there, this is group 2's application and it's running with Flask!"

if __name__ == "__main__":
    app.run(port=8081)