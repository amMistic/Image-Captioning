from fastapi import FastAPI, UploadFile
from fastapi import File, HTTPException

from .model import load_model, generate_caption
from .config import settings
from .utils import load_image


#
app = FastAPI()

# Load the Blip model, globally
model, processor = load_model(settings.blip_model)

# root
@app.get('/')
async def root():
    return {"message" : "Generate Caption for your image on 'localhost/docs'"}

@app.post('/generate')
async def caption(image: UploadFile = File(...), text: str = None):
    try:
        if image.content_type not in ["image/jpeg", "image.png"]:
            raise HTTPException(status_code=400, detail="Invalid Image Format")
        
        loaded_image = load_image(await image.read())
        caption = generate_caption(model, processor,loaded_image, text)
        return {'caption' : caption}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Interna Server Error")
    finally:
        await image.close()
