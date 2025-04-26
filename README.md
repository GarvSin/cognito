# 🧠 Cognito

An ultra-lightweight, production-ready image classification API powered by **FastAPI** and **TensorFlow's MobileNetV2** model.  
Currently hosted on **Render.com** for seamless, scalable deployment.

## 🚀 Introduction

The Cognito is designed to predict the type of fruit in an uploaded image with high confidence, using a state-of-the-art pretrained MobileNetV2 model.  
It’s crafted for blazing-fast responses, lightweight compute, and a developer experience you’ll love.

Whether you're building a consumer app, a smart agriculture platform, or a grocery inventory solution — this API gives you instant intelligence out of the box.

---

## 📦 Features

- **Upload and Predict:** Upload an image, and get back the fruit name and a confidence score.
- **MobileNetV2 Backbone:** Utilizes a highly efficient deep learning model trained on ImageNet.
- **Cross-Origin Ready:** Fully CORS enabled — integrate effortlessly into web and mobile apps.
- **Cloud Deployed:** Hosted on [Render.com](https://render.com) for high availability and scalability.
- **Error Resilient:** Graceful handling of invalid input with clear error responses.

---

## 🛠️ Technology Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Model:** [TensorFlow Keras MobileNetV2](https://keras.io/api/applications/mobilenet_v2/)
- **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
- **Deployment:** [Render.com](https://render.com/)
- **Middleware:** Full CORS (Cross-Origin Resource Sharing) support

---

## 📸 API Usage

### Endpoint

```
POST /predict
```

### Request

- **Content-Type:** `multipart/form-data`
- **Body:** Upload an image file (`.jpg`, `.jpeg`, `.png`)

### Example using `curl`

```bash
curl -X 'POST' \
  'https://<your-app-url>.onrender.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/image.jpg'
```

### Successful Response

```json
{
  "fruit": "banana",
  "confidence": 0.987654321
}
```

- **fruit:** Predicted fruit/object name.
- **confidence:** Model's confidence score (0–1 range).

---

## ⚠️ Error Handling

If an invalid file is uploaded or prediction fails, you'll receive:

```json
{
  "error": "Detailed error message"
}
```

With an HTTP `400 Bad Request` status code.

---

## 🌎 CORS Configuration

- **Allowed Origins:** `*`
- **Allowed Methods:** `GET, POST, PUT, DELETE, OPTIONS`
- **Allowed Headers:** `*`

> Built-in CORS middleware ensures you can access this API from **any frontend framework** (React, Vue, Angular, Flutter, etc.).

---

## 🔥 Local Development

### Prerequisites

- Python 3.8+
- Pipenv or Virtualenv recommended

### Setup

```bash
git clone https://github.com/your-repo/fruit-classification-api.git
cd fruit-classification-api
pip install -r requirements.txt
uvicorn app:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

You can also test it via the auto-generated interactive docs at:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Roadmap (Coming Soon)

- Dockerized Deployment
- Multi-fruit Detection
- Support for Custom Models
- Upload via URL
- Swagger Documentation Enhancements

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
