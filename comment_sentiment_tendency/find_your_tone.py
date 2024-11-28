import pickle

from numpy import vectorize
import pandas as pd
from textblob import TextBlob

# Load pre-trained model
with open("ctweet_prediction_model.pickle", "rb") as f:
    model = pickle.load(f)

def load_vectorizer():
    with open("count_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return vectorizer

# Function to predict sentiment of a sentence
def predict_sentiment(sentence):
    vectorize = load_vectorizer()
    transformed_sentence = vectorize.transform([sentence])
    polarity = model.predict(transformed_sentence)
    # polarity = TextBlob(sentence).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Negative"


# Function to save data to CSV file
def save_to_csv(data, filename="sentiment_data.csv"):
    df = pd.DataFrame(data, columns=["Sentence", "Sentiment"])
    df.to_csv(filename, mode="a", index=False, header=False)


# Main function
def main():
    while True:
        # Take input from user
        sentence = input("Enter a Comment (press 'q' to quit): ")

        # Quit if user enters 'q'
        if sentence.lower() == "q":
            break

        # Predict sentiment
        sentiment = predict_sentiment(sentence)

        # Save data to CSV file
        data = [(sentence, sentiment)]
        save_to_csv(data)

        # Print sentiment
        print("Sentiment:", sentiment)


if __name__ == "__main__":
    main()
