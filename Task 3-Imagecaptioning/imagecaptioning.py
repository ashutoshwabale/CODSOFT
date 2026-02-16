from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load pre-trained image captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load image
image_path = "Sample.jpg"   # put your image path here
image = Image.open(image_path).convert("RGB")

# Preprocess image
inputs = processor(image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)

# Decode and print caption
caption = processor.decode(output[0], skip_special_tokens=True)
print("Generated Caption:", caption)
