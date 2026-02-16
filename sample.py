from flask import flask

app = Flask(_name_)

def normal_function():
    return "This will be deployed on the Agent Server"

@app.route("/")
def home():
  return normal_function()

if _name_ == "_main_"
    app.run(host="0.0.0.0", port=5000)
