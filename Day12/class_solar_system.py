
from class_moon import Moon
import itertools
import numpy as np

class Solar_system():

    def __init__(self, filename):
        self.time = 0
        self.moons = []
        self.create_moons_from_puzzle_input(filename)
        pass;

    def simulate_motion(self, up_to_timestep):
        for i in range(0,up_to_timestep):
            self.apply_gravity_to_system()
            self.apply_velocity_to_system()

    def simulate_motion_efficient(self):
        #velocity: for each moon, and each coordinate calculate how many moons are +1 and -1, then take sum
        #cumsum?
        #Compare the total energy in the system
        #try it with a system of differential equations

    def create_moons_from_puzzle_input(self, filename):
        moons_positions = self.read_and_clean_moons_from_puzzle_input(filename)
        [self.create_moon(self.moon_position_to_int(moon)) for moon in moons_positions]

        pass;

    def read_and_clean_moons_from_puzzle_input(self, filename):
        file_object = open(filename, "r")
        moons_positions = [line.rstrip('\n') for line in file_object]
        file_object.close()
        moons_positions = [ moon.translate(moon.maketrans('', '', '<>xyz=')).split(", ") for moon in moons_positions]
        return(moons_positions)

    def moon_position_to_int(self, moon_position):
        return np.array(list(map(int, moon_position)))

    def create_moon(self,moon_position):
        self._moons.append(Moon(moon_position))

    def apply_gravity_to_system(self):
        moons_combinations = list(itertools.combinations(self.moons, 2))
        [ self.apply_gravity_to_two_moons(two_moons) for two_moons in moons_combinations ]
        pass;

    def apply_gravity_to_two_moons(self, two_moons):
        velocity_direction_moon0 = np.sign(two_moons[1].position - two_moons[0].position )
        velocity_direction_moon1 = -1*velocity_direction_moon0

        two_moons[0].velocity = two_moons[0].velocity + velocity_direction_moon0
        two_moons[1].velocity = two_moons[1].velocity + velocity_direction_moon1
        pass;

    def apply_velocity_to_system(self):
        self.moons = [ self.apply_velocity_to_moon(moon) for moon in self.moons]

    def apply_velocity_to_moon(self, moon):
        moon.position = moon.position + moon.velocity
        return moon

    def get_total_energy_in_system(self):
        return sum([moon.kinetic_energy * moon.potential_energy for moon in self.moons])

    def update_time(self):
        self.time = self.time + 1

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def moons(self):
        return self._moons

    @moons.setter
    def moons(self, value):
        self._moons = value
