import os, shutil, pygame
from pygame import mixer

def update_label_map(old_label, new_label):
  #  second_button.place_forget()
   # show_second_buttons()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    label_map_path = current_dir + "/label.map"
    with open(label_map_path, "r") as file:
        lines = file.readlines()
    with open(label_map_path, "w") as file:
        for line in lines:
            if new_label in line:
                line = line.replace(old_label + ".bzn", new_label + ".bzn")
                if old_label == "fed1a":
                    line = line.replace("{Titel1}", "{Premonitions}")
                elif old_label == "fed2a":
                    line = line.replace("{Titel2}", "{Paradise Revisited}")
                elif old_label == "fed3a":
                    line = line.replace("{Titel3}", "{Dark Omens}")
                elif old_label == "fed5a":
                    line = line.replace("{Titel4}", "{Vendetta}")
            elif old_label in line:
                line = line.replace(old_label + ".bzn", new_label + ".bzn")
                if old_label == "fed1":
                    line = line.replace("{Premonitions}", "{Titel1}")
                elif old_label == "fed2":
                    line = line.replace("{Paradise Revisited}", "{Titel2}")
                elif old_label == "fed3":
                    line = line.replace("{Dark Omens}", "{Titel3}")
                elif old_label == "fed5":
                    line = line.replace("{Vendetta}", "{Titel4}")
            file.write(line)

def create_mshell_copy():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mshell_path = os.path.join(current_dir, "mshell.set")
    mshell_copy_path = os.path.join(current_dir, "mshell_copy.set")
    label_path = os.path.join(current_dir, "label.map")
    label_copy_path = os.path.join(current_dir, "label_copy.map")

    # Kopie von mshell.set erstellen
    try:
        shutil.copy2(mshell_path, mshell_copy_path)
        shutil.copy2(label_path, label_copy_path)
        print("Kopie von mshell.set erstellt")
    except Exception as e:
        print(f"Fehler beim Erstellen der Kopie: {e}") 

def replace_mshell_with_copy():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mshell_path = os.path.join(current_dir, "mshell.set")
    mshell_copy_path = os.path.join(current_dir, "mshell_copy.set")
    label_path = os.path.join(current_dir, "label.map")
    label_copy_path = os.path.join(current_dir, "label_copy.map")

    # mshell.set löschen und durch Kopie ersetzen
    if os.path.exists(mshell_path):
        os.remove(mshell_path)
        os.remove(label_path)
        shutil.copy2(mshell_copy_path, mshell_path)
        shutil.copy2(label_copy_path, label_path)
        print("mshell.set gelöscht und durch Kopie ersetzt")
    else:
        print("mshell.set nicht gefunden")

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

def play_sound(sound_path):
    pygame.mixer.Sound(sound_path).play()

def play_music():
    #mixer.init()
    sound_folder = "sounds/effects"
    music_file = "Shellsd0.WAV"
    music_path = os.path.join(sound_folder, music_file)
    mixer.music.load(music_path)
    mixer.music.play()