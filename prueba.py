from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO('runs/detect/train13/weights/best.pt')

# Realizar predicción en una imagen
results = model.predict('trafico1.jpg', save=True)

# Acceder al primer resultado y mostrarlo
results[0].show()  # Mostrar los resultados para la primera imagen