# API-true-recommend
# Run on command line
## Load library
```
pip install -r requirements.txt
```

## Train model and save model

```
python tool\train_model_true_dataset.py   
```

## Run model for testting
```
run_model_true_dataset.py
```
## Run API

```
cd src
python app.py
```

## Run test API

```
cd src
python test_app.py
```

# Run on docker

## Run docker
```
docker build -t true-api .
docker run -p 9000:9000 true-api
```


## Check IP API
```
ipconfig
```


# Read API Docs
```
http://localhost:9000/docs
```


## How does it work
  This API app uses the Matrix Factorization algorithm. This algorithm is used by Netflix to recommend movies.To know how it work we need to know ratings table on movies data base.

  
![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/0e74190c-513d-4100-87ee-f24e9bbe09e8)

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/389ae082-d16b-4431-a782-7e806dab17bd)

  From the image, you will see that the table shows the column as the user and the row as the movie name. The values in the table are ratings from user_input (0-5 Star).

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/74e04ee8-c3ed-452d-9376-7a9e53596268)

  The values in this table come from the multiplication of two matrix features. The first feature is the score that movies have for these features, and the second feature is how much users like a movie's features.

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/144f66ae-ff16-4cab-bf7a-6c2f58753e73)

  If we know these two matrix features, we can predict ratings for unseen movies(white box).

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/41f86b26-3a5e-4098-9203-70446ff5cfe4)

  We can find the two matrix features by using machine learning algorithms for tuning parameters and checking model performance using a loss function. For example, if the tuning parameters are less than the set point, we will increase the matrix features as shown in the image above.


## How to feed input and get output
### Train test model 
![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/c57e9b7f-4b96-44f8-b48b-edb42525655d)

  We can prepare the data by using the train-test split algorithm.(80:20)

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/100b7e81-e337-49a7-bc33-a98efaeae643)


  From the data, we can train the model and test it as shown in this box diagram. 

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/0a243da6-7496-4567-ab12-f499110f03ea)

  Finally, test the model performance using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). If the values are close to 0, the model will be better.

### Using model
![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/3a06fd12-88d3-4c0f-aaf4-f54a84d6fc6f)

  To input data, set the user_id and movieId for the watched movies. Feed this data to the model, and you will receive predicted rating scores
  
## How to improve in the future
  - Use global libraries or custom libraries to avoid bugs or unsupported libraries.
  - Update the API to train data for existing users watching new movies or for new users.
  - Set up an automatic training pipeline.
  - Integrate with other recommendation algorithms to provide a hybrid recommendation system.
  

