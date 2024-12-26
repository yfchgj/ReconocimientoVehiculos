from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO('runs/detect/train13/weights/best.pt')

# Realizar predicción en un video
results = model.predict('video.mp4', save=True)
print("Video procesado y guardado en: runs/detect/predict/")