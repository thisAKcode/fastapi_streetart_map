import model
import router
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from config import SessionLocal, engine, get_db
from populate_db import insert_items, data_loader, DUMMY_DATA


model.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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

app.include_router(router.app, tags=["art"])
