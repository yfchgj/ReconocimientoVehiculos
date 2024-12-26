import os

# Ruta a las carpetas de cada clase
clases = ["Auto", "Bus", "Camión", "Minibús", "Motocicleta", "Mototaxi"]
base_path = "data"

# Renombrar imágenes
for clase in clases:
    clase_path = os.path.join(base_path, clase)
    if os.path.exists(clase_path):
        for idx, file in enumerate(os.listdir(clase_path)):
            if file.endswith(('.jpg', '.png', '.jpeg')):
                old_file_path = os.path.join(clase_path, file)
                new_file_name = f"{clase}_{idx}.jpg"
                new_file_path = os.path.join(clase_path, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renombrado: {old_file_path} -> {new_file_path}")
    else:
        print(f"No existe la carpeta: {clase_path}")