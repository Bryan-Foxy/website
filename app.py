from flask import Flask, render_template, url_for

#coConfig file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/project")
def project():
    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)