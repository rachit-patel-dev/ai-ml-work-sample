# Personalized Movie Recommendations

## Description
This model employs the K Nearest Neighbours (KNN) algorithm to offer personalized movie suggestions by analyzing the preferences of similar users. Predicting how a target user would rate unseen films based on shared behaviors provides accurate and relevant recommendations. Continuously refining its suggestions through user feedback ensures a tailored and engaging cinematic experience. This model is trained on a MovieLens dataset.

## How it works
The algorithm uses collaborative filtering, specifically K Nearest Neighbours (KNN), to recommend movies to users. It identifies users who have similar preferences and recommends movies that these similar users have enjoyed but the target user hasn't seen yet. This approach relies on the assumption that users who have similar tastes in movies will likely enjoy similar films.

## Usage
To use this model for personalized movie recommendations, input the preferences or ratings of the target user. The algorithm will then analyze these preferences and suggest a list of movies that the user might enjoy based on the preferences of similar users.

## Training
The model is trained on a Movie Lens dataset, which contains ratings provided by users for various movies. The KNN algorithm learns from this data to identify patterns in user preferences and make accurate movie recommendations.
