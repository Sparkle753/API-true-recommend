# API-true-recommend

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

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/3a06fd12-88d3-4c0f-aaf4-f54a84d6fc6f)

  To input data, set the user_id and movieId for the watched movies. Feed this data to the model, and you will receive predicted rating scores
  
## How to improve in the future
  - Use global libraries or custom libraries to avoid bugs or unsupported libraries.
  - Update the API to train data for existing users watching new movies or for new users.
  - Set up an automatic training pipeline.
  - Integrate with other recommendation algorithms to provide a hybrid recommendation system.
  

