from ultralytics import YOLO

if __name__ == '__main__':
    # Cargar el modelo entrenado
    model = YOLO('runs/detect/train13/weights/best.pt')

    # Validar el modelo
    metrics = model.val()

    # Mostrar las métricas
    print(metrics)
