import os
import shutil
from sklearn.model_selection import train_test_split

# Configuración
base_path = "data"  # Carpeta donde están las imágenes organizadas por clases
output_path = "yolo_dataset"  # Carpeta destino del dataset estructurado
clases = ["Auto", "Bus", "Camión", "Minibús", "Motocicleta", "Mototaxi"]
split_ratios = {"train": 0.7, "val": 0.2, "test": 0.1}  # División del dataset

# Crear carpetas para train, val y test
for split in split_ratios.keys():
    for folder in ["images", "labels"]:
        os.makedirs(os.path.join(output_path, split, folder), exist_ok=True)

# Procesar cada clase
for class_id, clase in enumerate(clases):
    clase_path = os.path.join(base_path, clase)
    if os.path.exists(clase_path):
        # Obtener todas las imágenes de la clase
        images = [os.path.join(clase_path, f) for f in os.listdir(clase_path) if f.endswith(('.jpg', '.png'))]
        # Dividir en train, val y test
        train_images, test_images = train_test_split(images, test_size=1 - split_ratios["train"])
        val_images, test_images = train_test_split(test_images, test_size=split_ratios["test"] / (split_ratios["val"] + split_ratios["test"]))

        # Mover imágenes y generar etiquetas
        for split, split_images in zip(["train", "val", "test"], [train_images, val_images, test_images]):
            for image_path in split_images:
                # Copiar la imagen a la carpeta correspondiente
                image_name = os.path.basename(image_path)
                dest_image_path = os.path.join(output_path, split, "images", image_name)
                shutil.copy(image_path, dest_image_path)

                # Crear la etiqueta correspondiente
                label_name = os.path.splitext(image_name)[0] + ".txt"
                dest_label_path = os.path.join(output_path, split, "labels", label_name)
                with open(dest_label_path, "w") as label_file:
                    # Etiqueta de ejemplo (ajustar según tu dataset real)
                    label_file.write(f"{class_id} 0.5 0.5 0.5 0.5\n")

                print(f"Procesado: {image_path} -> {dest_image_path}")
    else:
        print(f"No existe la carpeta: {clase_path}")