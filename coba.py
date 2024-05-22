from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["uts"]
collection = db["label"]

model = YOLO("model/restcount.pt")

def save_to_mongodb(predictions):
    if predictions.boxes is not None and len(predictions.boxes) > 0:
        for pred in predictions.boxes[0]:
            class_index = int(pred.cls[0])
            class_name = model.names[class_index]
            # Simpan class_name ke dalam MongoDB
            collection.insert_one({'label': class_name})


data = 'D:\Kuliah\Semester 6\Kepstun\RestCount\data\jalan.mp4'

# Prediksi dengan model YOLO dan simpan ke MongoDB
for frame in model.predict(source=data, show=True, conf=0.5, stream=True):
    save_to_mongodb(frame)

# Tutup koneksi MongoDB
client.close()