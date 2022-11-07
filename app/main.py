import model
import router
import json
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from config import SessionLocal, engine, get_db
from populate_db import insert_items, data_loader, DUMMY_DATA


model.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:8000/map/"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# populate_db if records are not already there.
@app.on_event("startup")
async def startup_populate_db():
    db = SessionLocal()
    item_count = db.query(model.ArtItem).count()
    if item_count == 0:
        insert_items(DUMMY_DATA)

@app.get("/map/", response_class=HTMLResponse)
async def _map(
    request:Request,
    db:Session = Depends(get_db)
    ):
    locations1 = db.query(model.ArtItem).all() # []
    context = {'request': request, 'locs':locations1}
    return templates.TemplateResponse("map.html", context) 

@app.post("/map/")
async def pass_item():
    return 'abc'

@app.get("/map2/", response_class=HTMLResponse)
async def _map(
    request:Request,
    db:Session = Depends(get_db)
    ):
    locations1 = db.query(model.ArtItem).all() # []
    print(type(locations1[0]))
    #locs = json.dumps({"message": "fine"}, indent = 4)
    json_object = json.dumps({"message": "fine"}, indent = 4)
    return json_object

app.include_router(router.app, tags=["art"])
