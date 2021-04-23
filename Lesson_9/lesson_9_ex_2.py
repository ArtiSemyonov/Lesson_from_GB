class Road:
    WEB_THICKNESS = 5
    WEIGHT_OF_ASPHALT_PER_SQUARE_METER = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        return self._width * self._length * self.WEIGHT_OF_ASPHALT_PER_SQUARE_METER * self.WEB_THICKNESS


road = Road(5000, 20)
print(f'{road.mass_calculation() / 1000} тонн')
