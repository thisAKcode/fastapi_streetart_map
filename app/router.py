from fastapi import APIRouter, Request, HTTPException, Path, Depends
from config import get_db
from sqlalchemy.orm import Session
from schemas import ItemSchema, RequestItem, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import crud

router = APIRouter()

router.mount("/templates", StaticFiles(directory="templates", html = True), name="templates")
favicon_path = 'favicon.ico'
templates = Jinja2Templates(directory="templates")

@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

# read sqlalchemy relationship chapter m to 1 https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-one

@router.post('/create_item')#, response_model = ItemSchema)
async def create(request:Request, 
                dataset_id:int,
                id:str,
                _data:str,
                geometry:bytes,
                db:Session=Depends(get_db)): # doesn't work wit RequestItem as first arg.
    _art_item = ItemSchema
    _art_item.dataset_id = dataset_id
    _art_item.id = id 
    _art_item._data = _data 
    _art_item.geometry = geometry 
    # figure out whether you need attribute title or not 
    # crud.create_art_item(db, dataset_id, art_item = request.parameter)
    crud.create_art_item(db, dataset_id, art_item = _art_item)
    return Response(code=200, status="Ok", message="ArtItem created succesfully").dict(exclude_none=True)

@router.get('/')
async def get(request:Request, db:Session=Depends(get_db)):
    _loaded = crud.get_all_art_items(db,0,100)
    # return Response(code=200, status="Ok", message="Success Fetch all data", result=_art_item).dict(exclude_none=True)
    context = {"request": request, "_items": _loaded}
    return templates.TemplateResponse("homepage.html", context)

@router.get('/{id}')
async def get_by_id(id:int,db:Session = Depends(get_db)):
    _art_item = crud.get_art_item_by_id(db, id)
    return Response(code=200, status="Ok", message="Success get data", result=_art_item).dict(exclude_none=True)


@router.post('/update')
async def update_art_item(request:Request,
                        dataset_id:int,
                        id:str,
                        _data:str,
                        geometry:bytes,
                        db:Session=Depends(get_db)):
    _art_item = ItemSchema
    _art_item.id = request.parameter.id,
    _art_item.dataset_id = request.parameter.dataset_id
    _art_item._data = request.parameter._data 
    _art_item.geometry = request.parameter.geometry 
    crud.update_art_item(
            db,
            dataset_id,
            art_item = _art_item)
    return Response(code=200, status="Ok",
                    message="Success update data",
                    result=_art_item).dict(exclude_none=True)
'''

@router.delete('/{id}')
async def delete(request:RequestItem, db:Session=Depends(get_db)):
    _art_item = crud.remove_art_item(db,art_item_id = request.parameter.id)
    return Response(code=200, status="Ok",
                    message="Success update data",
                        result=_art_item).dict(exclude_none=True)


'''
