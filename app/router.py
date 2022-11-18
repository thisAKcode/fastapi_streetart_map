from fastapi import APIRouter, Request, HTTPException, Path, Depends
from config import get_db
from sqlalchemy.orm import Session
from schemas import ArtItemSchema, RequestArtItem, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import crud

app = APIRouter()

app.mount("/templates", StaticFiles(directory="templates", html = True), name="templates")
favicon_path = 'favicon.ico'
templates = Jinja2Templates(directory="templates")

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.post('/create')
async def create(request:RequestArtItem, db:Session=Depends(get_db)):
    crud.create_art_item(db, art_item = request.parameter)
    return Response(code=200, status="Ok", message="ArtItem created succesfully").dict(exclude_none=True)

@app.get('/')
async def get(request:Request, db:Session=Depends(get_db)):

    _art_item = crud.get_art_item(db,0,100)
    # return Response(code=200, status="Ok", message="Success Fetch all data", result=_art_item).dict(exclude_none=True)
    context = {"request": request, "_items": _art_item}
    return templates.TemplateResponse("homepage.html", context)
@app.get('/{id}')
async def get_by_id(id:int,db:Session = Depends(get_db)):
    _art_item = crud.get_art_item_by_id(db, id)
    return Response(code=200, status="Ok", message="Success get data", result=_art_item).dict(exclude_none=True)


@app.post('/update')
async def update_art_item(request:RequestArtItem, db:Session=Depends(get_db)):
    _art_item = crud.update_art_item(db,art_item_id = request.parameter.id,
            title = request.parameter.title,
            description=request.parameter.description,
            lat=request.parameter.lat,
            lon=request.parameter.lon,
            image_one =request.parameter.image_one,
            image_two =request.parameter.image_two
            )
    return Response(code=200, status="Ok",
                    message="Success update data",
                    result=_art_item).dict(exclude_none=True)


@app.delete('/{id}')
async def delete(request:RequestArtItem, db:Session=Depends(get_db)):
    _art_item = crud.remove_art_item(db,art_item_id = request.parameter.id)
    return Response(code=200, status="Ok",
                    message="Success update data",
                        result=_art_item).dict(exclude_none=True)

