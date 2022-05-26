import csv

all_movies = []

with open(r'C:\Users\bhuvi\Google Drive\Coding\Python\Project 142 - Flash Mockup 2\articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []