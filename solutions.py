# -*- coding: utf-8 -*-

import Day1
from Day2.intcode_program import intcode_program
from Day2.read_gravity_assist_program import read_gravity_assist_program
from Day4.class_password_generator import password_generator
from Day6.class_orbits import orbits
from Day8.class_image_decoder import image_decoder
from Day10.class_monotoring_station import monotoring_station

masses_of_modules = Day1.read_masses_of_modules("Input/day1.txt" )
answer_1a = Day1.calculate_fuel(masses_of_modules)
answer_1b = Day1.calculate_fuel_partb(masses_of_modules)

#Day 2a
broken_gravity_assist_program_input = read_gravity_assist_program("Input/day2.txt")
restored_gravity_assist_program = intcode_program(broken_gravity_assist_program_input)
restored_gravity_assist_program.restore_gravity_assist_program()

answer_2a = restored_gravity_assist_program.get_intcode_program_answer()

#Day 2b
intcode_program_input = read_gravity_assist_program("Input/day2.txt")
intcode_program_instance = intcode_program(intcode_program_input)

answer_2b = intcode_program_instance.find_noun_and_verb_that_produces_output(19690720)

#To do: add solution for day 3

#Day 4
valid_passwords = password_generator('137683-596253')
valid_passwords.get_N_valid_passwords()

#Day 6
orbits_obj = orbits('Input/day6_part1.txt')
orbits_obj.count_all_orbits()
orbits_obj.find_shortest_path_part2()
orbits_obj.N_edges_shortest_path

#Day 8
image = image_decoder('Input/day8_part1.txt', 25, 6 )
image.display_decoded_image()

#Day 10
station_finder = monotoring_station('Input/day10_part1.txt' )
station_finder.find_best_station_location()
print(station_finder.N_visible_at_best_location)