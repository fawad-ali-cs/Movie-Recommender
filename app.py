from flask import Flask, render_template, request
import json

import time
import pandas as pd
import numpy as np
#from recommender_system import *
from recommender_system import *

app = Flask(__name__)

f = open('data/titles.json')
json_file = json.load(f)

links = open('data/links.json')
links_data = json.load(links)

rating_df = pd.read_csv('data/like_rating.csv')
rating_df.columns = rating_df.columns.astype('int')

@app.route('/')
def home():   
   return render_template('index.html', data=json_file)

@app.route('/instructions')
def instructions():
   return render_template('instructions.html')

@app.route('/algorithm')
def algorithm_description():
   return render_template('algorithm.html')


@app.route('/recommender_system', methods=['GET', 'POST'])
def recommender_system():

   req = request.get_json()
   user_ratings = np.zeros(rating_df.shape[1])
   movie_index = []

   for title in req:
      ind = json_file.index(title)

      movie_index.append(ind)
      user_ratings[ind] = 1

   rating_df_copy = rating_df.copy()
   rating_df_copy.loc[len(rating_df)] = user_ratings


   rec_list = get_recommendations(rating_df_copy)

   rec_movies = []
   rec_links = []

   for item in rec_list:
      rec_movies.append(json_file[item])
      rec_links.append(links_data[item])


   movie_list = {"movies":rec_movies, "links":rec_links}
   return movie_list 
 


if __name__ == '__main__':
   app.run()