from fastapi import FastAPI, UploadFile, Request, Response, status, File, Form
import uvicorn
import pickle
import pandas as pd
app = FastAPI()
wedo_model_ocr = None


@app.on_event("startup")
def startup_event():
    # ---------- Config ----------
    print('Initial model API')
    
    global matrix_fact
    global data_items_known
    global data_movies
    global data_ratings

    # load model from disk
    model_file  = 'tool/matrix_factorization_model_0v1.sav'
    matrix_fact = pickle.load(open(model_file, 'rb'))

    
    # load ratings.csv from disk
    data_file = 'models/data_items_known.sav'
    data_items_known = pickle.load(open(data_file, 'rb'))

     # load movies.csv from disk
    movies_file = 'database/movies.csv'
    data_movies = pd.read_csv(movies_file)

    # load ratings.csv from disk
    ratings_file = 'database/ratings.csv'
    data_ratings = pd.read_csv(ratings_file)


    print('Load model completed')

@app.get("/recommendations", status_code=200)
async def recommendations(req: Request, res: Response,
                         user_id: int,
                         returnMetadata: bool = False ):
    
    global matrix_fact
    global data_items_known

    item_id_dict = []

    #recommend for user_id
    if user_id >= data_items_known["user_id"].min() and user_id <= data_items_known["user_id"].max():
        items_known = data_items_known.query("user_id == @user_id")["item_id"]
        matrix_fact_data = matrix_fact.recommend(user=user_id, items_known=items_known)
        matrix_fact_data_item_id = matrix_fact_data[["item_id"]]

    else:
        return {"status": "fail, not have user_id"}

    if returnMetadata:
        df_Metadata= matrix_fact_data.join(data_movies,on='item_id')
        df_Metadata = df_Metadata[["item_id","title","genres"]]
        df_Metadata = df_Metadata.rename(columns={"item_id":"id"})
        df_Metadata['genres'] = df_Metadata['genres'].str.split('|')
        df_Metadata["id"] = df_Metadata["id"].astype(int)
        df_Metadata = df_Metadata.astype(str).to_dict('records')

        return {"items": [df_Metadata]}
    
    elif (user_id):
         #setting for return
        matrix_fact_data_item_id = matrix_fact_data[["item_id"]].rename(columns={"item_id":"id"})
        item_id_dict = matrix_fact_data_item_id.astype(int).astype(str).to_dict('records')
        
        return {"items":[item_id_dict]}
    

@app.get("/features", status_code=200)   
async def features(req: Request, res: Response,
                    user_id: int ): 
        
        global data_ratings

        histories = data_ratings.query("userId == @user_id")["movieId"]
        histories = histories.to_list()
    
        return {"features": {"histories": histories}}
     
if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info")