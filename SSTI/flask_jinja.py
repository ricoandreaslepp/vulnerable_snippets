from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "hello!"

if __name__ == "__main__":
    app.run(debug=True)