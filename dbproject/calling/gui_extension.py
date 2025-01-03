from tkinter import *
from main import *

def show_function():
    global distance_label, multiplier_label, basecost_label, finalcost_label, time_label
    if distance_label:
        distance_label.destroy()
    if multiplier_label:
        multiplier_label.destroy()
    if basecost_label:
        basecost_label.destroy()
    if finalcost_label:
        finalcost_label.destroy()
    if time_label:
        time_label.destroy()

    start_time = time()
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()

    if value1 in ['Enter your area code', ''] or \
            value2 in ['Enter your target area code', ''] or \
            value3 in ['Enter the phone number', '']:
        distance_label = Label(window, text="Please replace placeholder text")
        distance_label.pack()
        return
    value1 = int(value1)
    value2 = int(value2)
    value3 = value3

    distance = phone_codes_to_distance(value1, value2)
    multiplier = distance_to_cost_multiplier(distance)
    base_cost = base_cost_determination(value3)
    final_cost = round((base_cost * multiplier), 2)

    end_time = time()
    calculation_time = f"{round(((end_time - start_time) * 1000), 2)}ms"

    distance_label = Label(window,text=f"distance between countries: {distance}km")
    multiplier_label = Label(window, text=f"resulting cost multiplier: {multiplier}")
    basecost_label = Label(window, text=f"base calling cost: {base_cost}")
    finalcost_label = Label(window, text=f"final cost: {final_cost}")
    time_label = Label(window, text=f"this calculation took: {calculation_time}")

    distance_label.pack()
    multiplier_label.pack()
    basecost_label.pack()
    finalcost_label.pack()
    time_label.pack()

window = Tk()


window.title("Calling GUI extension")
icon = PhotoImage(file='python.png')
window.iconphoto(True, icon)


def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

label1 = Label(window, text="Enter all of the data:", font=("Helvetica", 10, "bold"))
label1.pack(pady=(15, 0), padx=15)

entry1 = Entry(window, width=30)
entry1.pack(pady=5, padx=180)
set_placeholder(entry1, "Enter your area code")

entry2 = Entry(window, width=30)
entry2.pack(pady=5, padx=65)
set_placeholder(entry2, "Enter your target area code")

entry3 = Entry(window, width=30)
entry3.pack(pady=5, padx=65)
set_placeholder(entry3, "Enter the phone number")

distance_label = None
multiplier_label = None
basecost_label = None
finalcost_label = None
time_label = None

button = Button(window, text="Send data", command=show_function)
button.pack()

label2 = Label(window, text="Outcome:", font=("Helvetica", 10, "bold"))
label2.pack(pady=(20, 0), padx=15)

window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))
window.mainloop()