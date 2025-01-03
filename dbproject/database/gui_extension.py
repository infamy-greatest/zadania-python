from create_folders import *
from populate_data import *
from time import sleep
import psutil
from tkinter import *
from tkinter.ttk import *
from multiprocessing import Process


def update_log(text):
    global info_label
    if info_label:
        info_label.destroy()
    info_label = Label(window, text=text)
    info_label.pack()


def start_populating_data():
    global info_label
    button.destroy()

    sleep(1)
    update_log("Creating all of the necessary folders...")
    window.update_idletasks()
    sleep(1)
    create_all_folders()
    sleep(1)
    update_log("All folders have been created.")
    window.update_idletasks()
    sleep(1)
    update_log("Populating folders with dummy data...")
    window.update_idletasks()

    populating_thread = Process(target=populate_folders_with_data)
    populating_thread.start()

    check_process(populating_thread)


def check_process(process):
    if process.is_alive():
        window.after(100, check_process, process)
    else:
        update_log("Folders have been populated with data.")
        window.update_idletasks()


if __name__ == '__main__':
    with open("progress.txt", "r") as file:
        lines = file.readlines()
        lines[0] = f"{0}\n"
        lines[1] = f"{0}\n"
    with open("progress.txt", "w") as file:
        file.writelines(lines)
    window = Tk()
    info_label = None
    window.title("Populating database GUI extension")
    icon = PhotoImage(file='python.png')
    window.iconphoto(True, icon)
    hdd = psutil.disk_usage('/')
    freedisk = round(hdd.free / (2 ** 30), 2)
    totaldisk = round(hdd.total / (2 ** 30), 2)
    label1 = Label(window, text="Creating and populating the database requires 20.6GB minimum disk space.")
    label2 = Label(window, text=f"Currently you have {freedisk}GB free disk space out of {totaldisk}GB total.")
    label1.pack(pady=(15, 0), padx=80)
    label2.pack()

    bar = Progressbar(window, orient=HORIZONTAL, length=200, mode="determinate", maximum=10000)
    bar.pack(pady=(20, 3))

    progress_label = Label(window, text="0/10000", font=("Arial", 10))
    progress_label.pack(pady=(5, 0))

    button = Button(window, text="Proceed", command=start_populating_data)
    button.pack(pady=(0,3))
    window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))


    def read_first_line():
        try:
            with open("progress.txt", "r") as file:
                lines = file.readlines()
                if len(lines) > 0:
                    return int(lines[0].strip())
        except (FileNotFoundError, ValueError):
            pass
        return 0


    def update_progress_bar():
        current_value = read_first_line()
        bar['value'] = current_value
        progress_label.config(text=f"{current_value}/10000")
        if current_value < 10000:
            window.after(500, update_progress_bar)
        else:
            progress_label.config(text="10000/10000 - Complete!")


    update_progress_bar()

    second_line_label = Label(window, text="CPU speed: N/A", font=("Arial", 10))
    second_line_label.pack(pady=(3, 0))


    def read_second_line():
        try:
            with open("progress.txt", "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    return int(lines[1].strip())
        except (FileNotFoundError, ValueError):
            pass
        return None

    second_line_value_previous = 0
    def update_second_line_label():
        global second_line_value_previous
        second_line_value = read_second_line()
        value_diff = second_line_value - second_line_value_previous
        second_line_value_previous = second_line_value
        if second_line_value is not None:
            second_line_label.config(text=f"CPU speed: {round(((value_diff * 2.06) / 2), 2)}Mb/s")
        else:
            second_line_label.config(text="CPU speed: N/A")
        window.after(2000, update_second_line_label)


    update_second_line_label()



    window.mainloop()
