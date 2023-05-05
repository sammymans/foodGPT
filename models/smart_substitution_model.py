import pandas as pd
import numpy as np
import gensim
from gensim.models import Word2Vec, KeyedVectors
from typing import List
import pickle
from sklearn.neighbors import BallTree

df_recipe = pd.read_pickle('data/complete_recipe_dataset.pkl')
df_recipe = df_recipe[['name', 'ids']].copy()

model = KeyedVectors.load('ingredient_similarities.model')

with open('data/testing_shelf.pkl', 'rb') as f:
    user_shelf = pickle.load(f)
shelf_tree = BallTree(model[user_shelf])

def score_recipe(recipe, shelf):
    dist, _ = shelf_tree.query(model[recipe], k=1)
    score = 1 - (0.1 * np.average(dist))
    if score < 0:
        return 0
    return score

df_recipe['score'] = df_recipe['ids'].apply(score_recipe, shelf=user_shelf)