import tkinter as tk
from tkinter import font, Label, Frame, Text
import subprocess, os, sys, pygame
from ctypes import windll
import functionsstuff as cmc

os.chdir(os.path.dirname(sys.argv[0]))

def resource_path(relative_path):
    try:
        # PyInstaller erstellt die exe-Datei im sys._MEIPASS-Verzeichnis
        base_path = sys._MEIPASS
    except Exception:
        # Wenn nicht im PyInstaller-Modus, verwende den relativen Pfad
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def button1_clicked():
    print("Remaster Modus aktiviert")
    cmc.play_sound("sound_b.wav")
    cmc.rename_directories("AI", "AI_Temp")
    cmc.rename_directories("AI_Container", "AI")
    cmc.rename_directories("addon", "Addon_Temp")
    cmc.rename_directories("Addon_Container", "addon")
    cmc.rename_directories("Sod", "Sod_Temp")
    cmc.rename_directories("Sod_Container", "Sod")
    cmc.rename_directories("Textures", "Texture_Temp")
    cmc.rename_directories("Texture_Container", "Textures")
    check_for_dom_file()
    check_for_rom_file()
    check_text_file()
    check_tech_file()
    button1.place_forget()
    button2.place(x=64, y=244)
    update_output_text("Remaster Modus aktiviert", "green")
    cmc.create_mshell_copy()

def button2_clicked():
    print("Classic Modus aktiviert")
    cmc.play_sound("sound_b.wav")
    cmc.rename_directories("AI", "AI_Container")
    cmc.rename_directories("AI_Temp", "AI")
    cmc.rename_directories("addon", "Addon_Container")
    cmc.rename_directories("Addon_Temp", "addon")
    cmc.rename_directories("Sod", "Sod_Container")
    cmc.rename_directories("Sod_Temp", "Sod")
    cmc.rename_directories("Textures", "Texture_Container")
    cmc.rename_directories("Texture_Temp", "Textures")
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    button9.place_forget()
    button10.place_forget()
    button1.place(x=64, y=244)
    update_output_text("Classic Modus aktiviert", "green")
    cmc.replace_mshell_with_copy()

def check_for_dom_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    dom_file_path = os.path.join(addon_path, "races.odf")
    with open(dom_file_path, "r") as file:
        content = file.read()
        if "borg" in content:
            button3.place(x=528, y=244)
            button4.place_forget()
            buttonc.place_forget()
            print("Borg")
        elif "dominion" in content:
            button4.place(x=528, y=244)
            button3.place_forget()
            buttonc.place_forget()
            print("Dom")
        elif "cardassian" in content:
            buttonc.place(x=528, y=244)
            button3.place_forget()
            button4.place_forget()
            print("Card")

def button3_clicked():
    button3.place_forget()
    print("Dom")
    cmc.play_sound("sound_b.wav")
    button3func()
    button4.place(x=528, y=244)  

def button3func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    races_path = os.path.join(addon_path, "races.odf")
    if current_dir:
        races_path = races_path
        with open(races_path, "r") as file:
            content = file.read()
            # if "dominion" in content:
            #     cmc.update_label_map("dominion", "borg")
            #     new_content = content.replace("dominion", "borg")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("AThe Dominion is on the march again", "green")
            #     if not button3.winfo_ismapped():
            #         button3.place_forget()
            #         button4.place(x=528, y=244)
            if "borg" in content:
                cmc.update_label_map("borg", "dominion")
                new_content = content.replace("borg", "dominion")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Dominion is on the march again", "green")
                if not button3.winfo_ismapped():
                    button3.place_forget()
                    button4.place(x=528, y=244)
            # elif "cardassian" in content:
            #     update_label_map("cardassian", "dominion")
            #     new_content = content.replace("cardassian", "dominion")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("CThe Dominion is on the march again", "green")
            #     if not button3.winfo_ismapped():
            #         button3.place_forget()
            #         button4.place(x=528, y=244)

def button4_clicked():
    button4.place_forget()
    print("Borg")
    cmc.play_sound("sound_b.wav")
    button4func()
    buttonc.place(x=528, y=244)                

def button4func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    races_path = os.path.join(addon_path, "races.odf")
    if current_dir:
        races_path = races_path
        with open(races_path, "r") as file:
            content = file.read()
            if "dominion" in content:
                cmc.update_label_map("dominion", "cardassian")
                new_content = content.replace("dominion", "cardassian")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Cardassian Civil War arises", "green")
                if not button4.winfo_ismapped():
                    button4.place_forget()
                    buttonc.place(x=528, y=244)
            # elif "borg" in content:
            #     update_label_map("borg", "cardassian")
            #     new_content = content.replace("borg", "cardassian")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("BBThe Cardassian Civil War arises", "green")
            #     if not button4.winfo_ismapped():
            #         button4.place_forget()
            #         buttonc.place(x=528, y=244)
            # elif "cardassian" in content:
            #     update_label_map("domnion", "cardassian")
            #     new_content = content.replace("domnion", "cardassian")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("CCThe Cardassian Civil War arises", "green")
            #     if not button4.winfo_ismapped():
            #         button4.place_forget()
            #         buttonc.place(x=528, y=244)

def buttonc_clicked():
    buttonc.place_forget()
    print("Card")
    cmc.play_sound("sound_b.wav")
    buttoncfunc()
    button3.place(x=528, y=244)

def buttoncfunc():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    races_path = os.path.join(addon_path, "races.odf")
    if current_dir:
        races_path = races_path
        with open(races_path, "r") as file:
            content = file.read()
            # if "dominion" in content:
            #     update_label_map("dominion", "borg")
            #     new_content = content.replace("dominion", "borg")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("AAAThe Borg invasion has begun", "green")
            #     if not buttonc.winfo_ismapped():
            #         buttonc.place_forget()
            #         button3.place(x=528, y=244)
            # elif "borg" in content:
            #     update_label_map("borg", "cardassian")
            #     new_content = content.replace("borg", "cardassian")
            #     with open(races_path, "w") as new_file:
            #         new_file.write(new_content)
            #         update_output_text("BBBThe Borg invasion has begun", "green")
            #     if not buttonc.winfo_ismapped():
            #         buttonc.place_forget()
            #         button3.place(x=528, y=244)
            if "cardassian" in content:
                cmc.update_label_map("cardassian", "borg")
                new_content = content.replace("cardassian", "borg")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Borg invasion has begun", "green")
                if not buttonc.winfo_ismapped():
                    buttonc.place_forget()
                    button3.place(x=528, y=244)

def button5_clicked():
    button5.place_forget()
    print("New Missions")
    cmc.play_sound("sound_b.wav")
  #  update_output_text("Standard Missions activated", "green")
    button5func()
    button6.place(x=1456, y=244)

def button5func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mshell_path = os.path.join(current_dir, "mshell.set")
    if current_dir:
        #mshell_path = current_dir + "/mshell.set"
        mshell_path = mshell_path
        with open(mshell_path, "r") as file:
            content = file.read()
            if "fed1a" in content:
                cmc.update_label_map("fed1a", "fed1")
                cmc.update_label_map("fed2a", "fed2")
                cmc.update_label_map("fed3a", "fed3")
                cmc.update_label_map("fed5a", "fed5")
                new_content = content.replace("fed1a", "fed1")
                new_content = new_content.replace("fed2a", "fed2")
                new_content = new_content.replace("fed3a", "fed3")
                new_content = new_content.replace("fed5a", "fed5")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standard Missions activated", "green")
                if not button5.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button5.place_forget()  # Falls sichtbar, ausblenden
                    button6.place(x=1456, y=244)  # Falls nicht sichtbar, platzieren
            elif "fed1" in content:
                cmc.update_label_map("fed1", "fed1a")
                cmc.update_label_map("fed2", "fed2a")
                cmc.update_label_map("fed3", "fed3a")
                cmc.update_label_map("fed5", "fed5a")
                new_content = content.replace("fed1", "fed1a")
                new_content = new_content.replace("fed2", "fed2a")
                new_content = new_content.replace("fed3", "fed3a")
                new_content = new_content.replace("fed5", "fed5a")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("New Missions activated", "green")
                if not button5.winfo_ismapped():
                    button5.place_forget()
                    button6.place(x=1456, y=244)

def button6_clicked():
    button6.place_forget()
    print("Original Missions")
    cmc.play_sound("sound_b.wav")
   # update_output_text("New Missions activated", "green")
    button6func()
    button5.place(x=1456, y=244)

def button6func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mshell_path = os.path.join(current_dir, "mshell.set")
    if current_dir:
        mshell_path = mshell_path
        with open(mshell_path, "r") as file:
            content = file.read()
            if "fed1a" in content:
                cmc.update_label_map("fed1a", "fed1")
                cmc.update_label_map("fed2a", "fed2")
                cmc.update_label_map("fed3a", "fed3")
                cmc.update_label_map("fed5a", "fed5")
                new_content = content.replace("fed1a", "fed1")
                new_content = new_content.replace("fed2a", "fed2")
                new_content = new_content.replace("fed3a", "fed3")
                new_content = new_content.replace("fed5a", "fed5")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standard Missions activated", "green")
                if not button6.winfo_ismapped():
                    button6.place_forget()
                    button5.place(x=1456, y=244)
            elif "fed1" in content:
                cmc.update_label_map("fed1", "fed1a")
                cmc.update_label_map("fed2", "fed2a")
                cmc.update_label_map("fed3", "fed3a")
                cmc.update_label_map("fed5", "fed5a")
                new_content = content.replace("fed1", "fed1a")
                new_content = new_content.replace("fed2", "fed2a")
                new_content = new_content.replace("fed3", "fed3a")
                new_content = new_content.replace("fed5", "fed5a")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("New Missions activated", "green")
                if not button6.winfo_ismapped():
                    button6.place_forget()
                    button5.place(x=1456, y=244)

def button7_clicked():
    button7.place_forget()
    print("Typhon Pact")
    cmc.play_sound("sound_b.wav")
    button7func()
    button8.place(x=992, y=244)  

def button7func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    races_path = os.path.join(addon_path, "races.odf")
    if current_dir:
        races_path = races_path
        with open(races_path, "r") as file:
            content = file.read()
            if "typhon" in content:
                cmc.update_label_map("typhon", "rom")
                new_content = content.replace("typhon", "rom")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Romulans strive for supremacy", "green")
                if not button7.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button7.place_forget()  # Falls sichtbar, ausblenden
                    button8.place(x=992, y=244) # Falls nicht sichtbar, platzieren
            elif "rom" in content:
                cmc.update_label_map("rom", "typhon")
                new_content = content.replace("rom", "typhon")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Typhon Pact has been formed", "green")
                if not button7.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button7.place_forget()  # Falls sichtbar, ausblenden
                    button8.place(x=992, y=244) # Falls nicht sichtbar, platzieren

def button8_clicked():
    button8.place_forget()
    print("Rom")
    cmc.play_sound("sound_b.wav")
    button8func()
    button7.place(x=992, y=244) 

def button8func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    races_path = os.path.join(addon_path, "races.odf")
    if current_dir:
        races_path = races_path
        with open(races_path, "r") as file:
            content = file.read()
            if "typhon" in content:
                cmc.update_label_map("typhon", "rom")
                new_content = content.replace("typhon", "rom")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Romulans strive for supremacy", "green")
                if not button8.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button8.place_forget()  # Falls sichtbar, ausblenden
                    button7.place(x=992, y=244) # Falls nicht sichtbar, platzieren
            elif "rom" in content:
                cmc.update_label_map("rom", "typhon")
                new_content = content.replace("rom", "typhon")
                with open(races_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("The Typhon Pact has been formed", "green")
                if not button8.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button8.place_forget()  # Falls sichtbar, ausblenden
                    button7.place(x=992, y=244) # Falls nicht sichtbar, platzieren


def button9_clicked():
    button9.place_forget()
    print("Extended Techtree")
    cmc.play_sound("sound_b.wav")
    #rename_directories("AI", "AI_Container")
  #  update_output_text("Standard Missions activated", "green")
    button9func()
    button10.place(x=704, y=683)

def button9func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    tech_path = os.path.join(addon_path, "techlvl.odf")
    if current_dir:
        tech_path = tech_path
        with open(tech_path, "r") as file:
            content = file.read()
            if "tech1rem" in content:
                cmc.update_label_map("tech1rem", "tech1")
                new_content = content.replace("tech1rem", "tech1")
                cmc.rename_directories(os.path.join(current_dir, "AI/AIPs"), os.path.join(current_dir, "AI/AIPs_R"))
                cmc.rename_directories(os.path.join(current_dir, "AI/AIPs_O"), os.path.join(current_dir, "AI/AIPs"))              
                with open(tech_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standard Techtree activated", "green")
                if not button9.winfo_ismapped():  # Überprüfen, ob der Button sichtbar ist
                    button9.place_forget()  # Falls sichtbar, ausblenden
                    button10.place(x=704, y=683)  # Falls nicht sichtbar, platzieren
            elif "tech1" in content:
                cmc.update_label_map("tech1", "tech1rem")
                new_content = content.replace("tech1", "tech1rem")
                cmc.rename_directories(os.path.join(current_dir, "AI/AIPs"), os.path.join(current_dir, "AI/AIPs_O"))
                cmc.rename_directories(os.path.join(current_dir, "AI/AIPs_R"), os.path.join(current_dir, "AI/AIPs"))
                with open(tech_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Extended Techtree activated", "green")
                if not button9.winfo_ismapped():
                    button9.place_forget()
                    button10.place(x=704, y=683)

def button10_clicked():
    button10.place_forget()
    print("Standard Techtree")
    cmc.play_sound("sound_b.wav")
   # update_output_text("New Missions activated", "green")
    button10func()
    button9.place(x=704, y=683)

def button10func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    tech_path = os.path.join(addon_path, "techlvl.odf")
    if current_dir:
        tech_path = tech_path
        with open(tech_path, "r") as file:
            content = file.read()
            if "tech1rem" in content:
                cmc.update_label_map("tech1rem", "tech1")
                new_content = content.replace("tech1rem", "tech1")
                cmc.rename_directories("AI\\AIPs", "AI\\AIPs_R") 
                cmc.rename_directories("AI\\AIPs_O", "AI\\AIPs")
                with open(tech_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standard Techtree activated", "green")
                if not button10.winfo_ismapped():
                    button10.place_forget()
                    button9.place(x=704, y=683)
            elif "tech1" in content:
                cmc.update_label_map("tech1", "tech1rem")
                new_content = content.replace("tech1", "tech1rem")
                cmc.rename_directories("AI\\AIPs", "AI\\AIPs_O") 
                cmc.rename_directories("AI\\AIPs_R", "AI\\AIPs")
                with open(tech_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Extended Techtree activated", "green")
                if not button10.winfo_ismapped():
                    button10.place_forget()
                    button9.place(x=704, y=683)

def check_for_rom_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    dom_file_path = os.path.join(addon_path, "races.odf")
    with open(dom_file_path, "r") as file:
        content = file.read()
        if "rom" in content:
            button7.place(x=992, y=244)
            button8.place_forget()
            print("Rom")
        elif "typhon" in content:
            button8.place(x=992, y=244)
            button7.place_forget()
            print("Typhon")

def check_tech_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_path = os.path.join(current_dir, "addon")
    tech_path = os.path.join(addon_path, "techlvl.odf")
    
    # Überprüfen, ob im Classic-Modus
    if os.path.exists(os.path.join(current_dir, "Addon_Container")):
        button9.place_forget()
        button10.place_forget()
        return
    
    if os.path.isfile(tech_path):
        with open(tech_path, "r") as file:
            content = file.read()
            if "tech1rem" in content:
                button10.place(x=704, y=683)
                print("Extended Techtree")
            elif "tech1" in content:
                button9.place(x=704, y=683)
                print("Standard Techtree")

def show_start_button():
    start_button.place(x=1024, y=877)


def show_map_button():
    map_button.place(x=686, y=877)

def check_addon_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    addon_temp_path = os.path.join(current_dir, "Addon_Temp")
    addon_container_path = os.path.join(current_dir, "Addon_Container")
    start_button.place(x=998, y=900)
    map_button.place(x=715, y=900)
    if os.path.exists(addon_temp_path):
        button2.place(x=64, y=244)
        update_output_text("Remaster Modus aktiviert", "green")
        check_for_dom_file()
        check_for_rom_file()
        check_tech_file()
    elif os.path.exists(addon_container_path):
        button1.place(x=64, y=244)
        update_output_text("Classic Modus aktiviert", "green")
    else:
        update_output_text("Addon Verzeichnisse nicht gefunden", "red")

def check_text_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mshell_path = os.path.join(current_dir, "mshell.set")
    
    # Überprüfen, ob im Classic-Modus
    if os.path.exists(os.path.join(current_dir, "Addon_Container")):
        button5.place_forget()
        button6.place_forget()
        return
    
    if os.path.isfile(mshell_path):
        with open(mshell_path, "r") as file:
            content = file.read()
            if "fed1a" in content:
                button6.place(x=1456, y=244)
                print("New Missions")
            elif "fed1" in content:
                button5.place(x=1456, y=244)
                print("Original Missions")

def on_hover(button, highlight_image):
    button.config(image=highlight_image)
    cmc.play_sound("sound_a.wav")

def on_leave(button, original_image):
    button.config(image=original_image)

def open_start_button():
    print("Launch")
    exe_directory = os.path.dirname(os.path.abspath(__file__))
    if exe_directory:
        # Starte die Exe in einem eigenen Prozess
        start_button.place_forget()
        subprocess.Popen([exe_directory + "/Armada.exe"], cwd=exe_directory)
        root.destroy()

def open_map_button():
    print("Launch Editor")
    exe_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    shortcut_path = os.path.join(exe_directory, "ArmadaEditor.lnk")
    if os.path.exists(shortcut_path):
        # Starte die Exe in einem eigenen Prozess
        map_button.place_forget()
        os.startfile(shortcut_path)
       # subprocess.Popen([shortcut_path], cwd=exe_directory, shell=True)
        root.destroy()
    else:
        #print("keine Verknüpfung")
       # print(exe_directory)
       # print(shortcut_path)
        print("Aktuelles Arbeitsverzeichnis:", os.getcwd())

def update_output_text(text, color):
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text + "\n", color)
    output_text.tag_configure(color, foreground=color)
    output_text.config(state=tk.DISABLED)

# Tkinter-Fenster erstellen
root = tk.Tk()
root.title("Star Trek Armada Game Setup")
root.resizable(width=False, height=False)

pygame.init()
pygame.mixer.init()

cmc.play_music()


# Bild für das Taskleistensymbol
icon_path = resource_path("icon32.ico")
# Icon in der Taskleiste setzenIst fertig, Release ist Weihnachten.
windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
root.iconbitmap(default=icon_path)

# Hintergrundbild laden
background_image_path = resource_path("background.png")
background_image = tk.PhotoImage(file=background_image_path)

# Hintergrundbild als Hintergrund des Fensters setzen
root.geometry(f"{background_image.width()}x{background_image.height()}")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Button 1 erstellen | Classic Modus
image_A_path = resource_path("image_A.png")
image_A = tk.PhotoImage(file=image_A_path)
highlight_A_path = resource_path("highlight_A.png")
highlight_A = tk.PhotoImage(file=highlight_A_path)
button1 = tk.Button(root, image=image_A, command=button1_clicked, borderwidth=0, highlightthickness=0, relief="flat")
button1.bind("<Enter>", lambda event: on_hover(button1, highlight_A))
button1.bind("<Leave>", lambda event: on_leave(button1, image_A))

# Button 2 erstellen | Remaster Mode
image_B_path = resource_path("image_B.png")
image_B = tk.PhotoImage(file=image_B_path)
highlight_B_path = resource_path("highlight_B.png")
highlight_B = tk.PhotoImage(file=highlight_B_path)
button2 = tk.Button(root, image=image_B, command=button2_clicked, borderwidth=0, highlightthickness=0, relief="flat")
button2.bind("<Enter>", lambda event: on_hover(button2, highlight_B))
button2.bind("<Leave>", lambda event: on_leave(button2, image_B))

# Button 3 erstellen | Borg
image_C_path = resource_path("image_C.png")
image_C = tk.PhotoImage(file=image_C_path)
highlight_C_path = resource_path("highlight_C.png")
highlight_C = tk.PhotoImage(file=highlight_C_path)
button3 = tk.Button(root, image=image_C, command=button3_clicked, borderwidth=0, highlightthickness=0)
button3.bind("<Enter>", lambda event: on_hover(button3, highlight_C))
button3.bind("<Leave>", lambda event: on_leave(button3, image_C))

# Button 4 erstellen | Dominion
image_D_path = resource_path("image_D.png")
image_D = tk.PhotoImage(file=image_D_path)
highlight_D_path = resource_path("highlight_D.png")
highlight_D = tk.PhotoImage(file=highlight_D_path)
button4 = tk.Button(root, image=image_D, command=button4_clicked, borderwidth=0, highlightthickness=0)
button4.bind("<Enter>", lambda event: on_hover(button4, highlight_D))
button4.bind("<Leave>", lambda event: on_leave(button4, image_D))

# Button 5 erstellen | Standard Missions
image_E_path = resource_path("image_E.png")
image_E = tk.PhotoImage(file=image_E_path)
highlight_E_path = resource_path("highlight_E.png")
highlight_E = tk.PhotoImage(file=highlight_E_path)
button5 = tk.Button(root, image=image_E, command=button5_clicked, borderwidth=0, highlightthickness=0)
button5.bind("<Enter>", lambda event: on_hover(button5, highlight_E))
button5.bind("<Leave>", lambda event: on_leave(button5, image_E))

# Button 6 erstellen | New Missions
image_F_path = resource_path("image_F.png")
image_F = tk.PhotoImage(file=image_F_path)
highlight_F_path = resource_path("highlight_F.png")
highlight_F = tk.PhotoImage(file=highlight_F_path)
button6 = tk.Button(root, image=image_F, command=button6_clicked, borderwidth=0, highlightthickness=0)
button6.bind("<Enter>", lambda event: on_hover(button6, highlight_F))
button6.bind("<Leave>", lambda event: on_leave(button6, image_F))

# Button 7 erstellen | Romulan
image_G_path = resource_path("image_G.png")
image_G = tk.PhotoImage(file=image_G_path)
highlight_G_path = resource_path("highlight_G.png")
highlight_G = tk.PhotoImage(file=highlight_G_path)
button7 = tk.Button(root, image=image_G, command=button7_clicked, borderwidth=0, highlightthickness=0)
button7.bind("<Enter>", lambda event: on_hover(button7, highlight_G))
button7.bind("<Leave>", lambda event: on_leave(button7, image_G))

# Button C erstellen | Cardassian
image_I_path = resource_path("image_I.png")
image_I = tk.PhotoImage(file=image_I_path)
highlight_I_path = resource_path("highlight_I.png")
highlight_I = tk.PhotoImage(file=highlight_I_path)
buttonc = tk.Button(root, image=image_G, command=buttonc_clicked, borderwidth=0, highlightthickness=0)
buttonc.bind("<Enter>", lambda event: on_hover(buttonc, highlight_I))
buttonc.bind("<Leave>", lambda event: on_leave(buttonc, image_I))

# Button 8 erstellen | Typhon Pact
image_H_path = resource_path("image_H.png")
image_H = tk.PhotoImage(file=image_H_path)
highlight_H_path = resource_path("highlight_H.png")
highlight_H = tk.PhotoImage(file=highlight_H_path)
button8 = tk.Button(root, image=image_H, command=button8_clicked, borderwidth=0, highlightthickness=0)
button8.bind("<Enter>", lambda event: on_hover(button8, highlight_H))
button8.bind("<Leave>", lambda event: on_leave(button8, image_H))

# Button 9 erstellen | Standard Techtree
image_T_path = resource_path("image_TechS.png")
image_T = tk.PhotoImage(file=image_T_path)
highlight_T_path = resource_path("highlight_TechS.png")
highlight_T = tk.PhotoImage(file=highlight_T_path)
button9 = tk.Button(root, image=image_I, command=button9_clicked, borderwidth=0, highlightthickness=0)
button9.bind("<Enter>", lambda event: on_hover(button9, highlight_T))
button9.bind("<Leave>", lambda event: on_leave(button9, image_T))

# Button 10 erstellen | Standard Missions
image_J_path = resource_path("image_TechE.png")
image_J = tk.PhotoImage(file=image_J_path)
highlight_J_path = resource_path("highlight_TechE.png")
highlight_J = tk.PhotoImage(file=highlight_J_path)
button10 = tk.Button(root, image=image_J, command=button10_clicked, borderwidth=0, highlightthickness=0)
button10.bind("<Enter>", lambda event: on_hover(button10, highlight_J))
button10.bind("<Leave>", lambda event: on_leave(button10, image_J))

# Button Start erstellen | Launch
image_S_path = resource_path("image_S.png")
image_S = tk.PhotoImage(file=image_S_path)
highlight_S_path = resource_path("highlight_S.png")
highlight_S = tk.PhotoImage(file=highlight_S_path)
start_button = tk.Button(root, image=image_S, command=open_start_button, borderwidth=0, highlightthickness=0)
start_button.bind("<Enter>", lambda event: on_hover(start_button, highlight_S))
start_button.bind("<Leave>", lambda event: on_leave(start_button, image_S))

# Button Map erstellen | Map Editor
image_M_path = resource_path("image_M.png")
image_M = tk.PhotoImage(file=image_M_path)
highlight_M_path = resource_path("highlight_M.png")
highlight_M = tk.PhotoImage(file=highlight_M_path)
map_button = tk.Button(root, image=image_M, command=open_map_button, borderwidth=0, highlightthickness=0)
map_button.bind("<Enter>", lambda event: on_hover(map_button, highlight_M))
map_button.bind("<Leave>", lambda event: on_leave(map_button, image_M))

# Lade die Schriftart
custom_font = font.Font(family="FederationDS9Title", size=16)  # Ändern Sie die Schriftgröße hier

# Ausgabe-Fenster erstellen
output_image_path = resource_path("image_M.png")
output_image = tk.PhotoImage(file=output_image_path)
output_frame = Frame(root, width=512, height=128, bd=0, highlightthickness=0)
output_frame.place(x=500, y=60)
output_frame.grid_propagate(False)
output_label = Label(output_frame, image=output_image, borderwidth=0)
output_label.pack(fill="both", expand=True)

# Berechnen Sie die erforderliche Höhe des Textfelds basierend auf der Schriftgröße und der Anzahl der Zeilen
num_lines = 1  # Anzahl der Zeilen im Textfeld
line_height = custom_font.metrics("linespace")
text_height = line_height
output_text = Text(output_label, wrap="word", font=custom_font, foreground="green", height=num_lines)
output_text.pack(fill="both", expand=True)

# Überprüfe das Addon-Verzeichnis und zeige den entsprechenden Button an
check_addon_directory()
check_text_file()
# Tkinter Eventloop starten
root.mainloop()