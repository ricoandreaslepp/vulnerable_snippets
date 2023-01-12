from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def home():
    if request.args.get('name'):
        return render_template_string(request.args.get('name'))
    
    return "Hello, send us your name!"

if __name__ == "__main__":
    app.run(debug=True)
