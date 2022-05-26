from flask import Flask, jsonify
import csv

all_movies = []
filename = r"C:\Users\bhuvi\Google Drive\Coding\Python\Project 141 - Article Recommendation\articles.csv"

with open(filename, encoding="utf8") as f:
  csvreader = csv.reader(f)
  for movie in csvreader: 
    all_movies.append(movie)

# liked_movies = []
# not_liked_movies = []
# did_not_watch = []

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "go to /get-article",
        "status": "success"
    })

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data": all_movies[1],
        "status": "success"
    })

# @app.route("/liked-movie", methods=["POST"])
# def liked_movie():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     liked_movies.append(movie)
#     return jsonify({
#         "status": "success"
#     }), 201

# @app.route("/unliked-movie", methods=["POST"])
# def unliked_movie():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     not_liked_movies.append(movie)
#     return jsonify({
#         "status": "success"
#     }), 201

# @app.route("/did-not-watch", methods=["POST"])
# def did_not_watch():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     did_not_watch.append(movie)
#     return jsonify({
#         "status": "success"
#     }), 201

if __name__ == "__main__":
  app.run()