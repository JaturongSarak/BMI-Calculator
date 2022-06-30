class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # kg.
        self.height = height  # cm.

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def chart(self):
        bmi = self.bmi()
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Healthy'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


import tkinter

App = tkinter.Tk()
App.title('BMI Calculator')

weight_label = tkinter.Label(App, text='Weight (kg.)')
height_label = tkinter.Label(App, text='Height (cm.)')
result_label = tkinter.Label(App, text='BMI')
bmi_label = tkinter.Label(App, text='')
chart_label = tkinter.Label(App, text='')

weight_entry = tkinter.Entry(App)
height_entry = tkinter.Entry(App)


def start():
    Robot = BMICalculator(float(weight_entry.get()), float(height_entry.get()))
    bmi = Robot.bmi()
    chart = Robot.chart()
    bmi_label.config(text=bmi)
    chart_label.config(text=chart)

calculator_button = tkinter.Button(App, text='Calculate', command=start)

weight_label.grid(column=0, row=0, padx=10, pady=5)
height_label.grid(column=0, row=1, padx=10, pady=5)
result_label.grid(column=0, row=2, padx=10, pady=5)
bmi_label.grid(column=1, row=2, padx=10, pady=5)
chart_label.grid(column=2, row=2, padx=10, pady=5)

weight_entry.grid(column=1, row=0, padx=10, pady=5)
height_entry.grid(column=1, row=1, padx=10, pady=5)

calculator_button.grid(column=2, row=0, padx=10, pady=5, ipadx=5)

App.mainloop()