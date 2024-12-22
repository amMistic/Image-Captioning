from PIL import Image
import io

# Load Image
def load_image(file):
    try:
        image = Image.open(io.BytesIO(file)).convert('RGB')
        return image
    except Exception as e:
        raise ValueError("Invalide Image Data") from e
