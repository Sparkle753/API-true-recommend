from fastapi import FastAPI, UploadFile, Request, Response, status, File, Form
import uvicorn
import pickle

app = FastAPI()
wedo_model_ocr = None


@app.on_event("startup")
def startup_event():
    # ---------- Config ----------
    print('Initial model API')
    
    global matrix_fact
    global data_user_id

    # load model from disk
    model_file  = 'tool/matrix_factorization_model_0v1.sav'
    matrix_fact = pickle.load(open(model_file, 'rb'))

    
    # load data from disk
    data_file = 'models/data_test_load_model.sav'
    data_user_id= pickle.load(open(data_file, 'rb'))

    print('Load model completed')

@app.get("/recommendations", status_code=200)
async def recommendations(req: Request, res: Response,
                         user_id: int,
                         returnMetadata: bool = False ):
    
    global matrix_fact
    global data_user_id

    item_id_dict = []

    #recommend for user_id
    if user_id > 0:
        items_known = data_user_id.query("user_id == @user_id")["item_id"]
        matrix_fact_data = matrix_fact.recommend(user=user_id, items_known=items_known)

        #setting for return
        matrix_fact_data_item_id = matrix_fact_data[["item_id"]].rename(columns={"item_id":"id"})
        item_id_dict = matrix_fact_data_item_id.astype(int).astype(str).to_dict('records')

    if returnMetadata and (user_id > 0):
        return{"items": "full"}
    
    elif (user_id > 0):
        return {"items":[item_id_dict]}
            
if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info")