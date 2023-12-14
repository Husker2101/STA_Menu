import tkinter as tk
from tkinter import PhotoImage, filedialog
import subprocess, os


# def select_directory():
#     global exe_directory
#     exe_directory = filedialog.askdirectory()
#     if exe_directory:
#         check_text_file(exe_directory + "/mshell.set")
#         update_output_text(exe_directory, "green")
#         select_button.place_forget()

def select_directory():
    global exe_directory
    exe_directory = filedialog.askdirectory()
    if exe_directory:
        mshell_path = exe_directory + "/mshell.set"
        #print(mshell_path)
        if os.path.isfile(mshell_path):
            check_text_file(mshell_path)
            update_output_text(exe_directory, "green")
            select_button.place_forget()
        else:
            print("Datei 'mshell.set' nicht gefunden:", mshell_path)
            update_output_text("Falsches Verzeichnis: 'mshell.set' nicht gefunden", "red")
            select_directory()

def check_text_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            #print("Inhalt der Datei:", content)
            if "fed1a" in content:
                background_label.config(image=background_image_2)
                show_first_buttons()
                print("fed1a")
            elif "fed1" in content:
                background_label.config(image=background_image_1)
                show_first_buttons()
                print("fed1")

def show_first_buttons():
    first_button.place(x=673, y=900)
    #first_button.grid(row=2, column=0, pady=(0, 20))
   # second_button.grid(row=2, column=1, pady=(0, 20))

def show_third_buttons():
    third_button.place(x=673, y=900)
    #first_button.grid(row=2, column=0, pady=(0, 20))
   # second_button.grid(row=2, column=1, pady=(0, 20))

def show_second_buttons():
    second_button.place(x=993, y=900)

def open_first_button():
    if exe_directory:
        mshell_path = exe_directory + "/mshell.set"
        with open(mshell_path, "r") as file:
            content = file.read()
            if "fed1a" in content:
                update_label_map("fed1a", "fed1")
                update_label_map("fed2a", "fed2")
                update_label_map("fed3a", "fed3")
                update_label_map("fed5a", "fed5")
                new_content = content.replace("fed1a", "fed1")
                new_content = new_content.replace("fed2a", "fed2")
                new_content = new_content.replace("fed3a", "fed3")
                new_content = new_content.replace("fed5a", "fed5")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standardmissonen gewählt", "green")
                background_label.config(image=background_image_1)
            elif "fed1" in content:
                update_label_map("fed1", "fed1a")
                update_label_map("fed2", "fed2a")
                update_label_map("fed3", "fed3a")
                update_label_map("fed5", "fed5a")
                new_content = content.replace("fed1", "fed1a")
                new_content = new_content.replace("fed2", "fed2a")
                new_content = new_content.replace("fed3", "fed3a")
                new_content = new_content.replace("fed5", "fed5a")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Neue Missionen gewählt", "green")
                background_label.config(image=background_image_2)
        first_button.place_forget()
    show_third_buttons()
    print("Alpha")

def open_third_button():
    if exe_directory:
        mshell_path = exe_directory + "/mshell.set"
        with open(mshell_path, "r") as file:
            content = file.read()
            if "fed1a" in content:
                update_label_map("fed1a", "fed1")
                update_label_map("fed2a", "fed2")
                update_label_map("fed3a", "fed3")
                update_label_map("fed5a", "fed5")
                new_content = content.replace("fed1a", "fed1")
                new_content = new_content.replace("fed2a", "fed2")
                new_content = new_content.replace("fed3a", "fed3")
                new_content = new_content.replace("fed5a", "fed5")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Standardmissonen gewählt", "green")
                background_label.config(image=background_image_1)
            elif "fed1" in content:
                update_label_map("fed1", "fed1a")
                update_label_map("fed2", "fed2a")
                update_label_map("fed3", "fed3a")
                update_label_map("fed5", "fed5a")
                new_content = content.replace("fed1", "fed1a")
                new_content = new_content.replace("fed2", "fed2a")
                new_content = new_content.replace("fed3", "fed3a")
                new_content = new_content.replace("fed5", "fed5a")
                with open(mshell_path, "w") as new_file:
                    new_file.write(new_content)
                    update_output_text("Neue Missionen gewählt", "green")
                background_label.config(image=background_image_2)
        third_button.place_forget()
        show_first_buttons()
        print("Beta")

def update_label_map(old_label, new_label):
    second_button.place_forget()
    show_second_buttons()
    label_map_path = exe_directory + "/label.map"
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

def open_second_button():
    print("Zweiter Knopf wurde gedrückt")
    if exe_directory:
        # Starte die Exe in einem eigenen Prozess
        first_button.place_forget()
        subprocess.Popen([exe_directory + "/Armada.exe"], cwd=exe_directory)
        root.destroy()

def update_output_text(text, color):
    output_text.config(state=tk.NORMAL)
    #output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text +"\n", color)
    output_text.tag_configure(color, foreground=color)
    output_text.config(state=tk.DISABLED)

# def pulse_animation():
#     global pulse_factor
#     pulse_factor = 1.8 if pulse_factor == 1.0 else 1.0
#     first_button_image_scaled = first_button_image.subsample(int(pulse_factor), int(pulse_factor))
#     second_button_image_scaled = second_button_image.subsample(int(pulse_factor), int(pulse_factor))
#     select_button_image_scaled = select_button_image.subsample(int(pulse_factor), int(pulse_factor))
#     first_button.config(image=first_button_image_scaled)
#     second_button.config(image=second_button_image_scaled)
#     select_button.config(image=select_button_image_scaled)
#     root.after(200, pulse_animation)

root = tk.Tk()
root.title("Menü mit Knöpfen und Hintergrund")
root.resizable(width=False, height=False)

# Platzhalter-Widget erstellen
#placeholder = tk.Frame(root, width=512, height=1054)
#placeholder.grid(row=0, column=0, pady=(0, 20))

# Hintergrundbild laden
background_image = PhotoImage(file="background.png")
background_image_1 = PhotoImage(file="background1.png")
background_image_2 = PhotoImage(file="background2.png")

# Hintergrundbild als Hintergrund des Fensters setzen
root.geometry(f"{background_image.width()}x{background_image.height()}")
#root.configure(background="white")  # Hintergrundfarbe setzen
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ausgabefenster erstellen
output_image = PhotoImage(file="Output.png")

output_frame = tk.Frame(root, width=512, height=128)
output_frame.place(x=610, y=458)
output_frame.grid_propagate(False)  # Deaktiviere automatisches Ändern der Größe
output_label = tk.Label(output_frame, image=output_image, borderwidth=0)
output_label.pack(fill=tk.BOTH, expand=True)

output_text = tk.Text(output_label, wrap=tk.WORD, font=("Arial", 12), foreground="green", height=4)
output_text.pack(fill=tk.BOTH, expand=True)

# Menü erstellen
#menu_bar = Menu(root)
#root.config(menu=menu_bar)

# Knöpfe-Menü
#buttons_menu = Menu(menu_bar, tearoff=0)
#menu_bar.add_cascade(label="Knöpfe", menu=buttons_menu)
#buttons_menu.add_command(label="Erster Knopf", command=open_first_button)
#buttons_menu.add_command(label="Zweiter Knopf")  # Noch nicht implementiert

# Buttons
first_button_image = PhotoImage(file="Button1.png")
first_button = tk.Button(root, image=first_button_image, command=open_first_button, borderwidth=0, highlightthickness=0)
second_button_image = PhotoImage(file="Button2.png")
second_button = tk.Button(root, image=second_button_image, command=open_second_button, borderwidth=0, highlightthickness=0)
third_button_image = PhotoImage(file="Button3.png")
third_button = tk.Button(root, image=third_button_image, command=open_third_button, borderwidth=0, highlightthickness=0)
select_button_image = PhotoImage(file="select.png")
select_button = tk.Button(root, text="Verzeichnis wählen", image=select_button_image, command=select_directory, borderwidth=0, highlightthickness=0)
select_button.place(x=351, y=900)
# Haupt-Eventloop starten
root.mainloop()