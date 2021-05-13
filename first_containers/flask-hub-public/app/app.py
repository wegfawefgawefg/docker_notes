from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Python Flask in Docker!</h1>
    <p>Sample docker webapp.</p>
    <h1>with livereload?</h1>
    """

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
    
# port 8080
# orm db: port 8081
