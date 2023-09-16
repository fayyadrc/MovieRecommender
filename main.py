import pandas as pd
import numpy as np
import random

df = pd.read_csv('movies.csv')
df = df.sample(frac=1, random_state=42)

movie_iterator = iter(df.iterrows())

def get_next_movie():
    try:
        _, movie = next(movie_iterator)
        return movie
    except StopIteration:
        return None

current_movie = get_next_movie()

while current_movie is not None:

    print("Movie:")
    print(current_movie[['Title', 'Year', 'Genre', 'Duration', 'Origin', 'Director', 'IMDB rating', 'IMDB link']])
    
    # Ask the user for input
    user_input = input("Type 'Next' for the next random movie or 'Exit' to quit: ").strip().lower()
    
    if user_input == 'exit':
        break
    elif user_input != 'next':
        print("Invalid input. Please type 'Next' or 'Exit'.")
        continue
    
    
    current_movie = get_next_movie()

print("End of movie list.")