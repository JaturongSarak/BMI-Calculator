class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # kg.
        self.height = height  # cm.

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def chart(self):
        bmi = self.bmi()
        if bmi >= 30:
            return 'Obese'
        elif 30 > bmi >= 25:
            return 'Overweight'
        elif 25 > bmi >= 18.5:
            return 'Healthy'
        else:
            return 'Underweight'


Robot = BMICalculator(weight=80, height=170)
print(Robot.bmi())
print(Robot.chart())
