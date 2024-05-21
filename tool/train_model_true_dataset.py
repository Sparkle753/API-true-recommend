from matrix_factorization import BaselineModel, KernelMF, train_update_test_split

import pandas as pd
from sklearn.metrics import mean_squared_error,mean_absolute_error
import numpy as np
import math
import pickle

# Read movie data 
movie_data = pd.read_csv("tool/dataset/ratings.csv",usecols=[0, 1, 2])

# Rename 
movie_data = movie_data.rename(columns={"userId": "user_id", "movieId": "item_id"})
movie_data = movie_data.dropna()

# Prepare data for online learning
X = movie_data[["user_id", "item_id"]]
y = movie_data["rating"]


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
mae = mean_absolute_error(y_test_update, pred)
print(f"\nTest RMSE: {rmse:.4f}")
print(f"Test MASE: {mae:.4f}")

# # # Get recommendations
user = 50
items_known = X_train_initial.query("user_id == @user")["item_id"]
matrix_fact_data = matrix_fact.recommend(user=user, items_known=items_known)
print(matrix_fact_data)

# save the model to disk
model_file = 'models/matrix_factorization_model_0v1.sav'
pickle.dump(matrix_fact, open(model_file, 'wb'))

data_file = 'models/items_known.sav'
pickle.dump(X, open(data_file, 'wb'))