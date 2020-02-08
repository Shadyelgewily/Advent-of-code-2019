# -*- coding: utf-8 -*-

import Day1
from Day2.intcode_program import intcode_program
from Day2.read_gravity_assist_program import read_gravity_assist_program

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