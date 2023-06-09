from fastapi import FastAPI, Form, Request 
from fastapi.templating import Jinja2Templates
from JoshAllenPassPredictor import pass_predictor
from starlette.staticfiles import StaticFiles 

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/allen-prediction")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/allen-prediction")
async def allen_prediction(request: Request, week: int = Form(...)):
    recieved = pass_predictor(week, "https://www.nfl.com/players/josh-allen-4/stats/")
    if recieved == "Player has a bye week":
        predicted_yards = "Player has a bye week"
        mse = "na"
        mae = "na"
        rmse = "na"
        r2 = "na"
    else: 
        mse = recieved[0]
        mae = recieved[1]
        rmse = recieved[2]
        r2 = recieved[3]
        predicted_yards = recieved[4]
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "week": week, 
        "predicted_yards": predicted_yards,
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "r2": r2})


@app.get("/mahomes-prediction")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/mahomes-prediction")
async def allen_prediction(request: Request, week: int = Form(...)):
    recieved = pass_predictor(week, "https://www.nfl.com/players/patrick-mahomes/stats/")
    if recieved == "Player has a bye week":
        predicted_yards = "Player has a bye week"
        mse = "na"
        mae = "na"
        rmse = "na"
        r2 = "na"
    else: 
        mse = recieved[0]
        mae = recieved[1]
        rmse = recieved[2]
        r2 = recieved[3]
        predicted_yards = recieved[4]
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "week": week, 
        "predicted_yards": predicted_yards,
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "r2": r2})


@app.get("/jackson-prediction")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/jackson-prediction")
async def allen_prediction(request: Request, week: int = Form(...)):
    recieved = pass_predictor(week, "https://www.nfl.com/players/lamar-jackson/stats/")
    if recieved == "Player has a bye week":
        predicted_yards = "Player has a bye week"
        mse = "na"
        mae = "na"
        rmse = "na"
        r2 = "na"
    else: 
        mse = recieved[0]
        mae = recieved[1]
        rmse = recieved[2]
        r2 = recieved[3]
        predicted_yards = recieved[4]
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "week": week, 
        "predicted_yards": predicted_yards,
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "r2": r2})


@app.get("/alternate-player")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/jackson-prediction")
async def allen_prediction(request: Request, week: int = Form(...), link: str = Form(...)):
    recieved = pass_predictor(week, link)
    if recieved == "Player has a bye week":
        predicted_yards = "Player has a bye week"
        mse = "na"
        mae = "na"
        rmse = "na"
        r2 = "na"
    else: 
        mse = recieved[0]
        mae = recieved[1]
        rmse = recieved[2]
        r2 = recieved[3]
        predicted_yards = recieved[4]
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "week": week, 
        "predicted_yards": predicted_yards,
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "r2": r2})

