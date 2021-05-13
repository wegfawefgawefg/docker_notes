from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Python Flask in Docker!</h1>
    <p>A sample web-apalsdiojkfhasdlkfjhasdfjhghjs;odfigjsrunning Flask i check this outnside Docker.</p>
    <h1>LIVERELOAD</h1>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') #port=urmom