from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO('runs/detect/train13/weights/best.pt')

# Usar la cámara para predicciones en tiempo real con stream=True
results = model.predict(source=0, stream=True)  # Activar stream para evitar acumulación en RAM

# Iterar sobre los resultados generados (si es necesario)
for result in results:
    print(result)