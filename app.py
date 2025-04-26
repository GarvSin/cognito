from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
import tensorflow as tf

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pretrained model (MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Decode predictions
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    try:
        # Open the image
        image = Image.open(io.BytesIO(contents)).convert('RGB')
        image = image.resize((224, 224))  # MobileNetV2 expects 224x224
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        # Predict
        preds = model.predict(image_array)
        decoded = decode_predictions(preds, top=1)[0][0]

        fruit_name = decoded[1]  # Name of the object
        confidence = float(decoded[2])  # Confidence score

        return JSONResponse(content={
            "fruit": fruit_name,
            "confidence": confidence
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
