from fastapi import FastAPI, UploadFile
from fastapi import File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .model import load_model, generate_caption
from .config import settings
from .utils import load_image

#
app = FastAPI()

# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Replace with the origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Load the Blip model, globally
model, processor = load_model(settings.blip_model)

# root
@app.get('/')
async def root():
    return {"message" : "Generate Caption for your image on 'localhost/docs'"}

@app.post('/generate')
async def caption(image: UploadFile = File(...), text: str = None):
    try:
        if image.content_type not in ["image/jpeg", "image/png", 'image/jpg']:
            raise HTTPException(status_code=400, detail="Invalid Image Format")
        
        loaded_image = load_image(await image.read())
        caption = generate_caption(model, processor,loaded_image, text)
        return {'caption' : caption}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Interna Server Error" + str(e))
    finally:
        await image.close()
