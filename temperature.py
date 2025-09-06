class temperature:
    # Атрибут класса
    scale_units = {"C": "Celsius", "F": "Fahrenheit"}

    def __init__(self, degrees, scale="C"):
        # Атрибуты экземпляра
        self.degrees = degrees
        self.scale = scale

    # Обычный метод экземпляра
    def convert_to(self, target_scale):
        if self.scale == target_scale:
            return self.degrees
        if self.scale == "C" and target_scale == "F":
            return (self.degrees * 9/5) +32
        if self.scale == "F" and target_scale == "C":
            return (self.degrees - 32) * 5/9
my_temp = temperature(60)
print(my_temp.convert_to("F"))