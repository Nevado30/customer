from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import web

app = FastAPI()

# Static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Routers
app.include_router(web.router)


# Test
@app.get("/ping")
def ping():
    return {"status": "ok"}
