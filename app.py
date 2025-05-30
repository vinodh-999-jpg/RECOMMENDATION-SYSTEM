from flask import Flask, render_template, request
from surprise import Dataset, Reader, SVD
import pandas as pd

app = Flask(__name__)

# Sample user-movie ratings
sample_data = [
    {'user': 1, 'item': 'Inception', 'rating': 5, 'genre': 'Sci-Fi'},
    {'user': 1, 'item': 'The Matrix', 'rating': 4, 'genre': 'Sci-Fi'},
    {'user': 2, 'item': 'The Godfather', 'rating': 5, 'genre': 'Crime'},
    {'user': 2, 'item': 'Scarface', 'rating': 4, 'genre': 'Crime'},
    {'user': 3, 'item': 'Titanic', 'rating': 5, 'genre': 'Romance'},
    {'user': 3, 'item': 'The Notebook', 'rating': 4, 'genre': 'Romance'},
    {'user': 4, 'item': 'Interstellar', 'rating': 5, 'genre': 'Sci-Fi'},
    {'user': 4, 'item': 'The Shawshank Redemption', 'rating': 5, 'genre': 'Drama'},
    {'user': 5, 'item': 'RRR', 'rating': 5, 'genre': 'Telugu'},
    {'user': 5, 'item': 'Pushpa', 'rating': 4, 'genre': 'Telugu'},
    {'user': 6, 'item': 'Baahubali', 'rating': 5, 'genre': 'Telugu'},
    {'user': 6, 'item': 'Ala Vaikunthapurramuloo', 'rating': 4, 'genre': 'Telugu'}
]


df = pd.DataFrame(sample_data)

def train_model():
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    return algo

def get_trending_movies_by_genre(genre):
    fallback = {
        "Sci-Fi": ["Inception", "The Matrix", "Interstellar"],
        "Crime": ["The Godfather", "Scarface", "Pulp Fiction"],
        "Romance": ["Titanic", "The Notebook", "La La Land"],
        "Drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"]
    }
    return fallback.get(genre, [])

def recommend(user_id, genre):
    algo = train_model()
    user_id = int(user_id)
    seen_items = df[df['user'] == user_id]['item'].tolist()
    unseen_items = [movie for movie in get_trending_movies_by_genre(genre) if movie not in seen_items]
    predictions = [(movie, algo.predict(user_id, movie).est) for movie in unseen_items]
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    genres = ["Sci-Fi", "Crime", "Romance", "Drama"]
    if request.method == "POST":
        user_id = request.form['user_id']
        genre = request.form['genre']
        if user_id.isdigit():
            recommendations = recommend(user_id, genre)
    return render_template("index.html", recommendations=recommendations, genres=genres)

if __name__ == "__main__":
    app.run(debug=True)
