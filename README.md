# RECOMMENDATION-SYSTEM

COMPANY : CODTECH IT SOLUTIONS

NAME : Althi vinodh kumar

INTERN ID : CT04DN428

DOMAIN: MACHINE LEARNING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

##

Project Title: Personalized Movie Recommendation System Using Flask and SVD
Project Description:
This project is a web-based movie recommendation system built using the Flask web framework and a collaborative filtering algorithm (SVD from the Surprise library). It aims to provide personalized movie suggestions based on user preferences and past ratings. By allowing users to input their ID and select a genre, the system delivers predicted movie ratings and recommends the most suitable unwatched movies within the chosen category.

Key Features
User-Friendly Interface:
The application features a simple and intuitive front-end built with HTML and styled using CSS. Users can enter their User ID and select a genre from a dropdown menu. The recommendations are then displayed in visually appealing cards that show the movie title and its predicted rating.

Collaborative Filtering Algorithm (SVD):
At the heart of the system lies a collaborative filtering model using the Singular Value Decomposition (SVD) algorithm from the Surprise library. This approach leverages historical rating data from multiple users to predict how a given user would rate movies they haven't seen yet.

Genre-Based Filtering:
The system focuses on genre-based personalization. When a user selects a genre, the system filters a set of trending movies from that genre (hardcoded for demonstration), and uses the SVD model to predict ratings for those the user hasn’t seen. This hybrid approach combines collaborative filtering (via SVD) with content filtering (via genre selection).

Minimal Dataset with Expandable Design:
The sample dataset includes a small number of users, movies, ratings, and genres. However, the architecture of the system is modular and ready for scaling — it can be easily adapted to larger, real-world datasets by loading external CSV files or integrating a database.

Modular Code Structure:
The application is logically organized:

Model training function (train_model) initializes and trains the SVD algorithm.

Recommendation function (recommend) generates predictions for unseen movies in the selected genre.

Genre handling function (get_trending_movies_by_genre) returns a fallback list of popular titles.

Flask route (/) handles both GET and POST requests and renders the output via a Jinja2 HTML template.

Responsive and Aesthetic Design:
The UI is styled with a clean CSS file. A background image, smooth buttons, input fields, and card-based recommendation display offer a modern look. The use of a semi-transparent container improves readability on top of the background image.

Technology Stack
Backend: Python, Flask

Machine Learning: Surprise (SVD Algorithm)

Frontend: HTML, CSS (with background image support)

Data Handling: pandas

Use Case
This system is perfect for demonstrating how recommender systems work on a small scale. It is ideal for:

Educational purposes (showcasing SVD and Flask integration),

Proof-of-concept projects,

Starting point for building a more robust recommendation engine using real-world datasets like MovieLens or IMDb.

Future Improvements
Database Integration: Replace hardcoded data with a real database like SQLite or PostgreSQL.

User Authentication: Allow users to register and log in, saving their preferences and interaction history.

Dynamic Genre and Movie Data: Fetch real-time data using APIs like TMDB or IMDb.

Advanced Recommendation Models: Experiment with deep learning models like Neural Collaborative Filtering or Autoencoders.

Improved UI/UX: Add animations, user profiles, filtering/sorting options, and mobile responsiveness.

Conclusion
This movie recommendation system showcases how machine learning can be integrated into a web application to deliver personalized content. With its modular design, clean interface, and efficient recommendation logic, it provides a solid foundation for developers and data science enthusiasts looking to build more advanced recommender systems.
##

# OUTPUT

![Image](https://github.com/user-attachments/assets/5c04152a-66c1-43fb-a4df-7be46a8dc352)
![Image](https://github.com/user-attachments/assets/03251c1d-4edf-464a-b028-0e9bae8d491a)

