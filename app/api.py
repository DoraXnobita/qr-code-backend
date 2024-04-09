import uvicorn
from fastapi import FastAPI
import pyqrcode 
import random
from PIL import Image
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    link_to_generate: str
    file_save_name: str

@app.post("/items")
async def qr_code_generator(item_list:Item):
    print(item_list)
    link_to_generate = item_list.link_to_generate
    qr_code = pyqrcode.create(str(link_to_generate))
    file_save_name = item_list.file_save_name
    file_name = file_save_name+str(random.randint(0,100000)*random.randint(17,65))+".png"
    qr_code.png( file_name, scale=5 )
    print("QR Code saved as "+file_name)
    img = Image.open(file_name)
    print(img.show())
