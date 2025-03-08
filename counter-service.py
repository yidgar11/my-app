 #!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
counter = 0
# Initialize counters for POST and GET requests
post_counter = 0
get_counter = 0


@app.route('/', methods=["POST", "GET"])
def index():
    global post_counter, get_counter
    if request.method == "POST":
        post_counter += 1
        return "Hmm, Plus 1 please POST "
    elif request.method == "GET":
        get_counter += 1
        return str(f"Our counters are: POST: {post_counter}, GET: {get_counter}")

if __name__ == '__main__':
    app.run(debug=True,port=443,host='0.0.0.0')
