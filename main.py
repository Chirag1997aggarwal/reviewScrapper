from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
from typing import Optional

from reviewExtractor import reviewExtractor

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
def index(request: Request):
	'''landing page call'''
	return templates.TemplateResponse("index.html", {"request": request})

@app.post('/searchReview')
async def searchReview(productName:str=Form(...)):
	'''
	This API recieves an search keyword from user.
	And extract the details releated to that keyword with the help of reviewExtractor.
	'''
	print(productName)
	data = reviewExtractor(productName.replace(' ', ''))
	return {'details':data}
