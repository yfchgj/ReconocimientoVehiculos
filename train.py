from ultralytics import YOLO

def main():
    # Cargar el modelo YOLOv8
    model = YOLO('yolov8s.pt')  # Modelo más ligero (small)
    
    # Entrenar el modelo con 50 épocas
    model.train(data='data.yaml', epochs=50, imgsz=640)
    
    print("Entrenamiento completado.")

if __name__ == '__main__':
    main()
