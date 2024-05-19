from matrix_factorization import BaselineModel, KernelMF, train_update_test_split

import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
import math


# Read movie data 
movie_data = pd.read_csv("tool/dataset/ratings.csv",usecols=[0, 1, 2])

# Rename 
movie_data = movie_data.rename(columns={"userId": "user_id", "movieId": "item_id"})

movie_data = movie_data.dropna()
#print(movie_data)
# set data value to int
#movie_data = movie_data.astype(np.int8)


X = movie_data[["user_id", "item_id"]]
y = movie_data["rating"]

# Prepare data for online learning
(
    X_train_initial,
    y_train_initial,
    X_train_update,
    y_train_update,
    X_test_update,
    y_test_update,
) = train_update_test_split(movie_data, frac_new_users=0.2)


# # # Initial training
matrix_fact = KernelMF(n_epochs=20, n_factors=100, verbose=1, lr=0.001, reg=0.005)
matrix_fact.fit(X_train_initial, y_train_initial)

# # # Update model with new users
matrix_fact.update_users(
    X_train_update, y_train_update, lr=0.001, n_epochs=20, verbose=1
)
pred = matrix_fact.predict(X_test_update)
rmse = mean_squared_error(y_test_update, pred, squared=False)
print(f"\nTest RMSE: {rmse:.4f}")

# # # Get recommendations
user = 100
items_known = X_train_initial.query("user_id == @user")["item_id"]
print(matrix_fact.recommend(user=user, items_known=items_known))
