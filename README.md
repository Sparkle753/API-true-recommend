# API-true-recommend

○ How does it work
  This API app uses the Matrix Factorization algorithm. This algorithm is used by Netflix to recommend movies.To know how it work we need to know ratings table on movies data base.
  
![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/0e74190c-513d-4100-87ee-f24e9bbe09e8)

ratings table

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/389ae082-d16b-4431-a782-7e806dab17bd)

user_input (0-5 Star)

From the image, you will see that the table shows the column as the user and the row as the movie name. The values in the table are ratings from user_input (0-5 Star).

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/74e04ee8-c3ed-452d-9376-7a9e53596268)

multiplication of two matrix features


The values in this table come from the multiplication of two matrix features. The first feature is how much users like a movie's features, and the second feature is the score that movies have for these features.
 

○ How to feed input and get output

![image](https://github.com/Sparkle753/API-true-recommend/assets/66368427/3a06fd12-88d3-4c0f-aaf4-f54a84d6fc6f)

  To input data, set the user_id and movieId for the watched movies. Feed this data to the model, and you will receive predicted rating scores
  
○ How to improve in the future
