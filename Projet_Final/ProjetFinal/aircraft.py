
Cd0 = 0.015

class Aircraft:
    def __init__(self, name, wing_area, wing_span, Range ):
        self.name = name  # Surface de l'aire en m^2
        self.S = wing_area  # Surface de l'aire en m^2
        self.wing_span = wing_span  # Envergure de l'aile en m
        self.Range = Range


