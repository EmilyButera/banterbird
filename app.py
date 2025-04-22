from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/posts')
def get_posts():
    with(open("data.json", "r")) as file:
        post = json.load(file)

@app.route('/api/posts', methods=['POST'])
def add_post():
    new_post = request.get_json()
    with(open("data.json", "r")) as file:
        post = json.load(file)
        post.insert(0, new_post)
    with(open("data.json", "r")) as file:
        json.dump(posts, file, indent=4)
    return jsonify({"status": "sucess"}), 201

if __name__ == '__main__':
    app.run(debug=True)
