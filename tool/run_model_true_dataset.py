from matrix_factorization import BaselineModel, KernelMF, train_update_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error,mean_absolute_error
import numpy as np
import math
import pickle

# load model from disk
model_file  = 'models/matrix_factorization_model_0v1.sav'
matrix_fact = pickle.load(open(model_file, 'rb'))

# load data from disk
data_file = 'models/data_items_known.sav'
data_items_known = pickle.load(open(data_file, 'rb'))

## test model
# # # Get recommendations

user = 10
items_known = data_items_known.query("user_id == @user")["item_id"]
matrix_fact_data = matrix_fact.recommend(user=user, items_known=items_known)
matrix_fact_data_item_id = matrix_fact_data[["item_id"]]
print(data_items_known)


#data_test_load_model.to_csv('out.csv', index=False)  