import os, shutil

def rename_directories(old_name, new_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    old_path = os.path.join(current_dir, old_name)
    new_path = os.path.join(current_dir, new_name)

    try:
        shutil.move(old_path, new_path)
        #update_output_text(f"{old_name} umbenannt zu {new_name}", "green")
    except Exception as e:
        #update_output_text(f"Fehler beim Umbenennen: {e}", "red")
        pass

def button1_clicked():
    rename_directories("A", "A4")
    rename_directories("A1", "A")
