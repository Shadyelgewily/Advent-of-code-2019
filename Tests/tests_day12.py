import unittest
import numpy as np

from class_solar_system import Solar_system

class TestSuite(unittest.TestCase):
    def test_gravity(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.apply_gravity_to_system()
        velocities_t1 = [ solar_system.moons[i].velocity for i in range(0,4)]
        expected_output = [np.array([3, -1, -1]), np.array([1,3,3]),
                           np.array([-3, 1, -3]), np.array([-1, -3, 1])]

        self.assertTrue(np.array_equal(velocities_t1, expected_output))

    def test_velocity(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.apply_gravity_to_system()
        solar_system.apply_velocity_to_system()
        positions_t1 = [ solar_system.moons[i].position for i in range(0,4)]
        expected_output = [np.array([2, -1, 1]), np.array([3,-7,-4]),
                           np.array([1, -7, 5]), np.array([2, 2, 0])]

        self.assertTrue(np.array_equal(positions_t1, expected_output))

    def test_simulate_motion_position(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.simulate_motion(10)

        positions_t10 = [ solar_system.moons[i].position for i in range(0,4)]
        expected_output = [np.array([2, 1, -3]), np.array([1,-8,0]),
                           np.array([3, -6, 1]), np.array([2, 0, 4])]

        self.assertTrue(np.array_equal(positions_t10, expected_output))

    def test_potential_energy(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.simulate_motion(10)

        potential_energies = [ solar_system.moons[i].potential_energy for i in range(0,4)]
        expected_output = [6,9,10,6]

        self.assertListEqual(potential_energies, expected_output)

    def test_kinetic_energy(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.simulate_motion(10)

        kinetic_energies = [ solar_system.moons[i].kinetic_energy for i in range(0,4)]
        expected_output = [6,5,8,3]

        self.assertListEqual(kinetic_energies, expected_output)

    def test_total_energy_in_system(self):
        solar_system = Solar_system("../Input/day12_part1_example.txt")
        solar_system.simulate_motion(10)

        total_energy = solar_system.get_total_energy_in_system()
        expected_output = 179

        self.assertEqual(total_energy, expected_output)

if (__name__ == "__main__"):
    unittest.main()