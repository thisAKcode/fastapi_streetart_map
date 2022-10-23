import model
import router
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config import engine


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>startpage</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>some items</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()

app.include_router(router.router, prefix='/art_item', tags=["art_item"])
