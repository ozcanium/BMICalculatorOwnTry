from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,  height=300)
window.config(padx=40, pady=40)



def bmi_calculate():
    height = height_entry.get()
    weight = weight_entry.get()

    if height == '' or weight == '':
     result_label.config(text="Please write your height and weight !")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="please write valid number")


def write_result(bmi):
    result_string = f"Your BMI is : {round(bmi, 2)}. You are "
    if 16 <= bmi < 18:
        result_string += "Thin. Eat more."
    elif 18 <= bmi < 25:
        result_string += "Normal. Stay like this. "
    elif 25 <= bmi < 30:
        result_string += "Fat. Do cardio."
    return result_string



weight_label = Label(text="Enter your weight")
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

height_label = Label(text="Enter your height")
height_label.pack()

height_entry = Entry()
height_entry.pack()

button_calculator = Button(text="Calculate", command=bmi_calculate)
button_calculator.pack()

result_label = Label()
result_label.pack()


window.mainloop()