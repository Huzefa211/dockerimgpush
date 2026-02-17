from flask import Flask

app = Flask(__name__)

def normal_function():
    return "Moosa, Furqan bhai jaldi se meri plaaato ki website banao time nahi hai itna"

@app.route("/")
def home():
    return normal_function()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
