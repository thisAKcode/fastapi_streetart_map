import model
import router
import json
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config import SessionLocal, engine, get_db
from populate_db import insert_items, DUMMY_DATA
from crud import get_all_art_items, create_art_item

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

# populate_db if db_missing
@app.on_event("startup")
async def startup_populate_db():
    db = SessionLocal()
    item_count = 0
    try:
        item_count = db.query(model.Item).count()
    except:
        item_count == 0
    if item_count == 0:
        insert_items(DUMMY_DATA)

@app.get("/map/", response_class=HTMLResponse)
async def _map(
    request:Request,
    db:Session = Depends(get_db)
    ):
    locations1 = db.query(model.Item).all()
    # pass a list of dicts since templateResponse accept it as argument
    # each item  <class 'str'> representation of json object:
    #  {"type": "Feature", "geometry":.... }
    
    locs_all = [(jsonable_encoder(_item)['_data']) 
                for _item in locations1] 
    # ! TODO since several datasets may be stored the returning by groups is better
    # but works for now
    context = {'request': request, 
               'locs':locs_all}
    return templates.TemplateResponse("map.html", context) 


@app.get("/map2/", response_class=HTMLResponse)
async def _map(
    request:Request,
    db:Session = Depends(get_db)
    ):  
        locations = get_all_art_items(db)
        print(locations[0].dataset.name)
        locs = [json.loads(_item._data) for _item in locations]
        return json.dumps({"data": locs}, indent = 4)
app.include_router(router.app, tags=["art"])
