import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression, Ridge


def LREC(dataset, reg=1.0, user_list=None):
    
    if user_list == None:
        user_list = range(dataset.shape[0])
        
    X = dataset.T
    Y = X*2 - 1
   
    W = []

    for index in user_list:
        if 1 in Y.T[index] and -1 in Y.T[index]:
            rdg = Ridge(alpha=reg).fit(X, Y.T[index])
            
            W.append(rdg.coef_)
        else:
            W.append(np.zeros(dataset.shape[0]))
    
        
    if user_list == range(dataset.shape[0]):     
        W = np.array(W)

        pred = np.dot(W.T, dataset[user_list])

    else:
        W = np.array(W)
        pred = np.dot(W, dataset)
        
     
    train_replace = pred.min() - 1
    for index, u in enumerate(user_list):
        user_ratings = dataset[u]
        liked_movies = np.where(user_ratings == 1)[0]
            
        for i in liked_movies:
            pred[index][i] = train_replace
        
    return pred

def get_recommendations(dataset):
	rec_num = 25

	rating_matrix = np.array(dataset)
	pred_rating = LREC(rating_matrix, reg=250, user_list=[len(dataset) - 1])

	rec_movies = np.argpartition(pred_rating[0],-rec_num)[-rec_num:]

	return rec_movies





