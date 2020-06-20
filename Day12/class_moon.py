import numpy as np

class Moon():

    def __init__(self, moon_position):
        self.position = moon_position
        self.velocity = [0,0,0]
        self.potential_energy = 0
        self.kinetic_energy = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self.potential_energy = int(np.sum(np.abs(self.position)))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value
        self.kinetic_energy = int(np.sum(np.abs(self.velocity)))

    @property
    def potential_energy(self):
        return self._potential_energy

    @potential_energy.setter
    def potential_energy(self, value):
        self._potential_energy = value

    @property
    def kinetic_energy(self):
        return self._kinetic_energy

    @kinetic_energy.setter
    def kinetic_energy(self, value):
        self._kinetic_energy = value
