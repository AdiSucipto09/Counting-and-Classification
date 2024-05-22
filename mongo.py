from pymongo import MongoClient
import csv

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['uts']
collection = db['label']

def save_to_csv_from_mongodb(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['label'])  # Menambahkan field kecamatan
        # Dapatkan data dari MongoDB dan simpan ke dalam file CSV
        for item in collection.find({}, {"label": 1, "_id": 0}):
            writer.writerow([item['label']])
            
csv_file = 'detected_objects.csv'
            
# Simpan data dari MongoDB ke dalam file CSV
save_to_csv_from_mongodb(csv_file)