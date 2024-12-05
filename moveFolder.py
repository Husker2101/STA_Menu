import shutil
import os

def rename_folder(directories):
    """
    Bennen die Ordner der Reihenfolge nach um.
    :param directories: Eine Liste von Paaren, wobei jedes Paar den alten und den neuen Ordnernamen enthält.
    """
    # Verzeichnis des Skripts ermitteln
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des Skripts

    # Durchgehen der Ordnerpaare und Umbenennen
    for old_name, new_name in directories:
        old_path = os.path.join(current_dir, old_name)  # Alter Ordnerpfad
        new_path = os.path.join(current_dir, new_name)  # Neuer Ordnerpfad

        # Überprüfen, ob der Quellordner existiert
        if not os.path.isdir(old_path):
            print(f"Der Ordner '{old_path}' existiert nicht.")
            continue

        try:
            # Umbenennen des Ordners (Verzeichnis)
            shutil.move(old_path, new_path)
            print(f"'{old_name}' wurde erfolgreich in '{new_name}' umbenannt.")
        except Exception as e:
            print(f"Fehler beim Umbenennen von '{old_name}': {e}")
