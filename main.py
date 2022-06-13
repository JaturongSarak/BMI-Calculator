class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # kg.
        self.height = height  # cm.

    def bmi(self, weight, height):
        return weight / ((height / 100) ** 2)

    def chart(self, bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Healthy'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

print('BMI Calculator')
weight = input('Weight (kg.) : ')
height = input('Height (cm.) : ')
Robot = BMICalculator(float(weight), float(height))
bmi = Robot.bmi(Robot.weight, Robot.height)
chart = Robot.chart(bmi)
print(bmi)
print(chart)