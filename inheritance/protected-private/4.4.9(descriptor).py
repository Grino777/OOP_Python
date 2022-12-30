class AircraftDescriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = Aircraft.validator(instance, self.name, value)


class Aircraft:
    model = AircraftDescriptor()
    mass = AircraftDescriptor()
    speed = AircraftDescriptor()
    top = AircraftDescriptor()
    
    def __init__(self, model, mass, speed, top):
        self.model = model
        self.mass = mass
        self.speed = speed
        self.top = top

    def validator(self, key, value):
        if key == '_model':
            if type(value) is str:
                return value
        elif key in ['_mass', '_speed', '_top']:
            if type(value) in (int, float) and value > 0:
                return value
        elif key == '_weapons':
            if type(value) == dict:
                return value
        elif key == '_chairs':
            if type(value) == int:
                return value
        raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    chairs = AircraftDescriptor()

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs


class WarPlane(Aircraft):
    weapons = AircraftDescriptor()

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

for i in planes:
    print(i.__dict__)
