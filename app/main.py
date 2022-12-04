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
    item_count = db.query(model.Item).count()
    if item_count == 0:
        insert_items(DUMMY_DATA)

@app.get("/map/", response_class=HTMLResponse)
async def _map(
    request:Request,
    db:Session = Depends(get_db)
    ):
    locations1 = db.query(model.Item).all() # []
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
        locations = db.query(model.Item).all()
        locs = [jsonable_encoder(_item) for _item in locations]
        return json.dumps({"data": locs}, indent = 4)

app.include_router(router.app, tags=["art"])
