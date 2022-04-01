from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import shutil
import datetime
from button import My_Button
import webbrowser


def open_file():
    file = fd.askopenfilename(title="Choose a file of any type", filetypes=[("All files", "*.*")])
    os.startfile(os.path.abspath(file))


def copy_file():
    file_to_copy = fd.askopenfilename(title="Choose a file to copy", filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title="What is the target folder?")

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title="File copied!", message="File has been successfully copied")
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there! File not copied.")


def delete_file():
    file = fd.askopenfilename(title="Choose a file to delete", filetypes=[("All files", "*.*")])
    os.remove(os.path.abspath(file))
    mb.showinfo(title="File delete", message="File has been deleted!")


def rename_file():
    file = fd.askopenfilename(title="Choose a file to rename", filetypes=[("All files", "*.*")])
    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file to")
    rename_wn.geometry("250x70")
    rename_wn.resizable(0, 0)

    Label(rename_wn, text="What is the new name for the file?",
          font=button_font).place(x=0, y=0)

    new_name = Entry(rename_wn, width=40, font=button_font)
    new_name.place(x=0, y=0)
    new_file_name = os.path.join(os.path.dirname(file), new_name.get() + os.path.splitext(file)[1])

    os.rename(file, new_file_name)
    mb.showinfo(title="File rename", message="File has been successfully renamed")


def open_folder():
    folder = fd.askdirectory(title="Select folder to open")
    os.startfile(folder)


def delete_folder():
    folder_to_delete = fd.askdirectory(title="Choose a folder to delete")
    mb.showinfo("Folder deleted", "The folder has been successfully deleted")


def move_folder():
    folder_to_move = fd.askdirectory(title="Select the folder you wish to move")
    mb.showinfo(message="You just selected the folder to move, "
                        "now please select the desired destination "
                        "where you want to move the folder to")
    destination = fd.askdirectory(title="Where to move the folder to")

    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo("Folder moved", "The folder has been successfully moved")
    except:
        mb.showerror("Error", "We could not move your folder. Please ensure the destination exists")


def list_files_in_folder():
    i = 0

    folder = fd.askdirectory(title="Select the folder you wish to show")
    files = os.listdir(os.path.abspath(folder))

    list_files_wn = Toplevel(root)
    list_files_wn.title(f"Files in {folder}")
    list_files_wn.geometry("500x500")
    list_files_wn.resizable(0, 0)

    listbox = Listbox(list_files_wn, selectbackground="SteelBlue", font=button_font)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    while i < len(files):
        listbox.insert(END, files[i])
        i += 1


# Mod Management Interface

def set_time():
    # Getting unique date stamp - 'Hour, Minute, Seconds - Day, Month, Year'
    set_time = datetime.datetime.now()
    current_time = set_time.strftime("%H%M%S-%a%d%b%y")
    return current_time


def backup_mods_folder():
    current_time = set_time()
    try:
        # Create folder
        parent_dir = "C:/MMM/Backups/"
        path = os.path.join(parent_dir, current_time)
        os.mkdir(path)

        # Copy mod folder contents over
        mod_folder = mod_folder_location
        destination = f"C:/MMM/Backups/{current_time}"
        files = os.listdir(mod_folder)
        for filename in files:
            shutil.copy2(os.path.join(mod_folder, filename), destination)
        mb.showinfo(title="Backed Up", message=f"Folder successfully backup up with folder name {current_time}.")
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def list_current_mods():
    i = 0
    folder = mod_folder_location
    files = os.listdir(os.path.abspath(folder))

    list_files_wn = Toplevel(root)
    list_files_wn.title(f"Files in {folder}")
    list_files_wn.geometry("500x500")
    list_files_wn.resizable(0, 0)

    listbox = Listbox(list_files_wn, fg=button_text_colour, font=(button_font, 10), bg=background)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    while i < len(files):
        listbox.insert(END, files[i])
        i += 1


def clear_current_mods():
    check = mb.askokcancel(title="Are you sure?", message="Are you sure you want to clear?")
    if check:
        dir = mod_folder_location
        for file in os.scandir(dir):
            os.remove(file.path)
        mb.showinfo(title="CLEARED!", message="Mods CLEARED!")
    else:
        pass


def show_backups():
    backups_folder = "c:/MMM/Backups"
    os.startfile(backups_folder)


def open_mods_folder():
    # mods_folder = "C:/Users/james/AppData/Roaming/.minecraft/mods"
    os.startfile(mod_folder_location)


def restore_backup():
    folder_to_restore = fd.askdirectory(title="Select the backup folder you wish to restore",
                                        initialdir="c:/MMM/Backups")
    try:
        # Copy mod folder contents over
        destination = mod_folder_location
        files = os.listdir(folder_to_restore)
        for filename in files:
            shutil.copy2(os.path.join(folder_to_restore, filename), destination)
        mb.showinfo(title="Success!", message="Backup successfully restored!")
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def forge_options(choice):
    choice = clicked.get()
    try:
        os.startfile(os.path.abspath(f"c:/MMM/Forge/{choice}.jar"))
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def extra_mods():
    def add_list():
        l_two = []
        mod_list = []
        selected = listbox.curselection()
        for item in selected:
            l_two.append(item)
        for i in l_two:
            mod_list.append(temp[i])
        try:
            # Copy mod folder contents over
            destination = mod_folder_location
            # files = os.listdir(mod_folder)
            for filename in mod_list:
                shutil.copy2(os.path.join(folder, filename), destination)

        except:
            mb.showerror(title="Error!", message="Well something has gone wrong there!")

    i = 0
    temp = []
    folder = fd.askdirectory(title="Select the folder you wish to show", initialdir="c:/MMM/")
    files = os.listdir(os.path.abspath(folder))

    list_files_wn = Toplevel(root)
    list_files_wn.title(f"Files in {folder}")
    list_files_wn.geometry("500x500")
    list_files_wn.resizable(0, 0)

    listbox = Listbox(list_files_wn, selectmode="multiple", selectbackground=button_text_colour, bg=background,
                      fg=button_text_colour, font=button_font)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    while i < len(files):
        listbox.insert(END, files[i])
        temp.append(files[i])
        i += 1

    Button(list_files_wn, text="Add Mod(s)", command=add_list, width=15, font=button_font).place(x=330, y=5)
    Button(list_files_wn, text="EXIT", width=15, font=button_font, command=list_files_wn.destroy).place(x=330,y=125)


def list_mods(mod_choice):
    def add_list():
        l_two = []
        mod_list = []
        selected = listbox.curselection()
        for item in selected:
            l_two.append(item)
        for i in l_two:
            mod_list.append(temp[i])
        try:
            # Create folder
            current_time = set_time()
            parent_dir = "C:/MMM/Modpacks/"
            path = os.path.join(parent_dir, current_time)
            os.mkdir(path)

            # Copy mod folder contents over
            destination = f"C:/MMM/Modpacks/{current_time}"
            # files = os.listdir(mod_folder)
            for filename in mod_list:
                shutil.copy2(os.path.join(folder, filename), destination)

            def get_name():
                show = new_name.get()
                os.rename(f"c:/MMM/Modpacks/{current_time}/", f"c:/MMM/Modpacks/{show}/")
                mb.showinfo(title="Modpack Renamed", message=f"Your Modpack has been successfully renamed {show}.")
                list_files_wn.destroy()

            new_name = Entry(list_files_wn, width=15, font=button_font)
            new_name.place(x=330, y=48)
            Button(list_files_wn, text="Name Modpack", command=get_name, width=15, font=button_font).place(x=330, y=85)

        except:
            mb.showerror(title="Error!", message="Well something has gone wrong there!")

    i = 0
    temp = []
    mod_choice = clicked_mod.get()
    try:
        folder = (f"C:/MMM/{mod_choice}/")
        files = os.listdir(os.path.abspath(folder))
        Label(root, text=mod_choice, font=("Helvetica", 15, "bold"), borderwidth=2, highlightthickness=2, relief="groove",
                                bg=background, fg=button_text_colour, wraplength=250).grid(column=2, row=8, pady=10)

        list_files_wn = Toplevel(root)
        list_files_wn.title(f"Files in {folder}")
        list_files_wn.geometry("500x500")
        list_files_wn.resizable(0, 0)

        listbox = Listbox(list_files_wn, selectmode="multiple", selectbackground=button_text_colour, bg=background,
                          fg=button_text_colour, font=button_font)
        listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
        scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.config(yscrollcommand=scrollbar.set)

        while i < len(files):
            listbox.insert(END, files[i])
            temp.append(files[i])
            i += 1

        Button(list_files_wn, text="Create Modpack", command=add_list, width=15, font=button_font).place(x=330, y=5)
        Button(list_files_wn, text="EXIT", width=15, font=button_font, command=list_files_wn.destroy).place(x=330,y=125)

    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def open_curse_forge():
    webbrowser.open('https://www.curseforge.com/minecraft/mc-mods', new=1)


def open_skindex():
    webbrowser.open('https://www.minecraftskins.com/', new=1)


def open_shaders():
    shaders_folders = "C:/MMM/Shaders"
    try:
        os.startfile(shaders_folders)
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def open_skins():
    skins_folder = "C:/MMM/Skins"
    try:
        os.startfile(skins_folder)
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def launch():
    try:
        os.startfile(os.path.abspath(launcher_location))
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def fabric():
    try:
        os.startfile(os.path.abspath(fabric_location))
    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def open_modpack():

    folder = mod_folder_location
    current_mods = os.listdir(os.path.abspath(folder))
    temp_hold = []
    for a in current_mods:
        temp_hold.append(a)

    if temp_hold == []:
        try:
            # Copy mod folder contents over
            folder_to_restore = fd.askdirectory(title="Select the Modpack you wish to restore",
                                                initialdir="c:/MMM/Modpacks")
            destination = mod_folder_location
            files = os.listdir(folder_to_restore)
            for filename in files:
                shutil.copy2(os.path.join(folder_to_restore, filename), destination)
            mb.showinfo(title="Success!", message="Modpack successfully installed!")
        except:
            mb.showerror(title="Error!", message="Well something has gone wrong there!")
    else:
        mb.showerror(title="Error", message="Mods still in folder. Please clear first! Don't forget to backup (if you need to).")


def add_optifine(opti_choice):
    opti_choice = clicked_mod2.get()
    copy_optifine = mb.askyesno("Optifine", message=f"Copy over Optifine for version {opti_choice}?", icon="warning")
    if copy_optifine:
        try:
            parent_dir = "C:/MMM/Optifine/"
            mod_folder = mod_folder_location
            filename = f"Optifine{opti_choice}.jar"
            shutil.copy2(os.path.join(parent_dir, filename), mod_folder)
            mb.showinfo(title="Backed Up", message=f"Successfully copied over Optifine for {opti_choice}.")
        except:
            mb.showerror(title="Error!", message="Well something has gone wrong there!")


# Defining variables
title = "Minecraft Mod Manager"
background = "#eaac8b"
button_font = ("Helvetica", 13,)
# button_background = "#ff97b7"
button_text_colour = "#1d3557"
button_background = "#e56b6f"
launcher_location = "C:/Users/james/curseforge/minecraft/install/minecraft.exe"
mod_folder_location = "C:/Users/james/AppData/Roaming/.minecraft/mods"
fabric_location = "C:/MMM/Fabric/fabric-installer-0.10.2.exe"

# Root Window Setup
root = Tk()
root.title(title)
root.geometry("596x470")
root.resizable(0, 0)
root.config(bg=background)
img = PhotoImage(file="lbg2.png")
background_label = Label(root, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# Dropdown menu options
options = [
    "1.18.2",
    "1.18.1",
    "1.17.1",
    "1.16.5",
    "1.16.4",
    "1.16.3",
    "1.15.2",
    "1.14.4",
    "1.14.2",
    "1.13.2",
    "1.12.2",
    "1.9",
    "1.7.2",
    "1.6.4",
    "Fabric"
]

options2 = [
    "1.18.1",
    "1.17",
    "1.16.5",
    "1.15",
    "1.14",
    "1.13",
    "1.12.2"
]

options3 = [
    "1.18.2",
    "1.18.1",
    "1.17.1",
    "1.16.5",
    "1.16.4",
    "1.16.3",
    "1.15.2",
    "1.14.4",
    "1.14.2",
    "1.13.2",
    "1.12.2",
    "1.9",
    "1.7.2",
]

# Forge Dropdown
clicked = StringVar()
clicked.set("FORGE")
drop = OptionMenu(root, clicked, *options, command=forge_options)
drop.config(width=24, bg=button_text_colour, fg="white", highlightthickness=0)
drop.grid(column=1, row=1)
Label(root, text="File Manager", font=("Helvetica", 15, "bold"), highlightthickness=2, borderwidth=2, relief="groove",
      bg=background, fg=button_text_colour, wraplength=250).grid(column=2, row=1, pady=10)

# Fabric Button
Button(root, text='Fabric', width=20, bg=button_text_colour, fg="white",
       command=open_file).grid(column=3, row=1, padx=4, pady=2)

#File Explorer Buttons
btn1 = My_Button(root, "Open File", open_file, border=0)
btn1.grid(column=1, row=2, padx=4, pady=2)
btn2 = My_Button(root, "Copy a file", copy_file)
btn2.grid(column=2, row=2, padx=4, pady=2)
btn3 = My_Button(root, "Rename a file", rename_file)
btn3.grid(column=3, row=2, padx=4, pady=2)
btn4 = My_Button(root, "Delete a file", delete_file)
btn4.grid(column=1, row=3, padx=4, pady=2)
btn5 = My_Button(root, "Open a folder", open_folder)
btn5.grid(column=2, row=3, padx=4, pady=2)
btn6 = My_Button(root, "Delete a folder", delete_folder)
btn6.grid(column=3, row=3, padx=4, pady=2)
btn7 = My_Button(root, "Move a folder", move_folder)
btn7.grid(column=1, row=4, padx=4, pady=2)
btn8 = My_Button(root, "EXIT", root.destroy)
btn8.grid(column=2, row=4, padx=4, pady=2)
btn8.config(fg="white")
btn9 = My_Button(root, "List files in folder", list_files_in_folder)
btn9.grid(column=3, row=4, padx=4, pady=2)

# Mod control Buttons
Label(root, text="Mod Control", font=("Helvetica", 15, "bold"), highlightthickness=2, borderwidth=2, relief="groove",
      bg=background, fg=button_text_colour, wraplength=250).grid(column=2, row=5, pady=10)
mod1 = My_Button(root, "List Current Mods", list_current_mods)
mod1.grid(column=1, row=6, padx=4, pady=2)
mod2 = My_Button(root, "BACKUP Mods", backup_mods_folder)
mod2.grid(column=2, row=6, padx=4, pady=2)
mod3 = My_Button(root, "CLEAR Current Mods", clear_current_mods)
mod3.grid(column=3, row=6, padx=4, pady=2)
mod4 = My_Button(root, "Open Mods Folder", open_mods_folder)
mod4.grid(column=1, row=7, padx=4, pady=2)
mod5 = My_Button(root, "Show Backups", show_backups)
mod5.grid(column=2, row=7, padx=4, pady=2)
mod6 = My_Button(root, "Restore Backup", restore_backup)
mod6.grid(column=3, row=7, padx=4, pady=2)

#Craft Modpack Dropdown
clicked_mod = StringVar()
clicked_mod.set("Craft Modpack")
drop_mod = OptionMenu(root, clicked_mod, *options, command=list_mods)
drop_mod.config(width=24, bg=button_text_colour, fg="white", highlightthickness=0)
drop_mod.grid(column=1, row=8, pady=4)
current_version = Label(root, text="1.18", font=("Helvetica", 15, "bold"), highlightthickness=2, borderwidth=2, relief="groove",
      bg=background, fg=button_text_colour, wraplength=250).grid(column=2, row=8, pady=10)

# OPTIFINE Dropdown
clicked_mod2 = StringVar()
clicked_mod2.set("Optifine Version")
drop_mod2 = OptionMenu(root, clicked_mod2, *options3, command=add_optifine)
drop_mod2.config(width=24, bg=button_text_colour, fg="white", highlightthickness=0)
drop_mod2.grid(column=3, row=8, pady=4)

#Lower Buttons
mod7 = My_Button(root, "Open CurseForge", open_curse_forge)
mod7.grid(column=1, row=9, padx=4, pady=2)
mod8 = My_Button(root, "LOAD Mod Pack", open_modpack)
mod8.grid(column=2, row=9, padx=4, pady=2)
mod9 = My_Button(root, "Skindex", open_skindex)
mod9.grid(column=3, row=9, padx=4, pady=2)
mod10 = My_Button(root, "Shaders", open_shaders)
mod10.grid(column=1, row=10, padx=4, pady=2)
mod11 = My_Button(root, "ADD Mod(s)", extra_mods)
mod11.grid(column=2, row=10, padx=4, pady=2)
mod12 = My_Button(root, "Skins", open_skins)
mod12.grid(column=3, row=10, padx=4, pady=2)

#Minecraft launcher
launcher = My_Button(root, "LAUNCH MINECRAFT", launch)
launcher.config(width=64, bg=button_text_colour, fg="white")
launcher.grid(column=1, row=11, columnspan=3, padx=4, pady=12)

# Finalizing the window
root.update()
root.mainloop()
