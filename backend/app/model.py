from transformers import BlipProcessor, BlipForConditionalGeneration

def load_model(model_name):
    try:
        # load model, Image to text captioning
        processor = BlipProcessor.from_pretrained(model_name)
        model = BlipForConditionalGeneration.from_pretrained(model_name)
        return model, processor
    except Exception as e:
        raise f"Error: {e}"


def generate_caption(model, processor, image, text=None):
    try:
        # Prepare the inputs for captioning
        if text is not None:
            # Conditional image captioning
            inputs = processor(image, text, return_tensors="pt")
        else:
            # Unconditional image captioning
            inputs = processor(image, return_tensors="pt")

        # Generate the caption
        out = model.generate(**inputs, max_new_tokens=200)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        return caption
    except Exception as e:
        raise f"Error: {e}"