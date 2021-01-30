from flask import Flask, render_template
app = Flask(__name__
@app.route("/")
def home():
    return render_template("index.htm")

@app.route("/conducciontemeraria")
def about():
    return render_template("conducciontemeraria.htm")

if __name__ == "__main__":
    app.run(debug=True)