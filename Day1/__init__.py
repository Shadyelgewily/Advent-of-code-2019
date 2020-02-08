# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:40:05 2020

@author: quiet
"""

import math
import numbers

def calculate_fuel(masses_of_modules):
    
    masses_of_modules = make_list_if_single_number(masses_of_modules)
    
    fuel_requirement = [ max(math.floor(mass / 3) -2, 0) for mass in masses_of_modules ]
    
    return(sum(fuel_requirement))

def calculate_fuel_partb(masses_of_modules):
    
    masses_of_modules = make_list_if_single_number(masses_of_modules)
        
    total_fuel = 0
    module_fuels = [0] * len(masses_of_modules)
    module_fuels_incl_fuel_on_fuel = [0] * len(masses_of_modules)
    for i, mass in enumerate(masses_of_modules):
        module_fuels[i] = calculate_fuel(mass)
        
        additional_fuels = []
        fuel_on_fuel = calculate_fuel(module_fuels[i] )
        while( fuel_on_fuel > 0 ):
            additional_fuels.append(fuel_on_fuel)
            fuel_on_fuel = calculate_fuel(additional_fuels[-1])
            
        module_fuels_incl_fuel_on_fuel[i] = module_fuels[i] + sum(additional_fuels)
    
    total_fuel = sum(module_fuels_incl_fuel_on_fuel)
    
    return(total_fuel)


def make_list_if_single_number(masses_of_modules):
    if( isinstance(masses_of_modules, numbers.Number) ):
        return([masses_of_modules])
    else:
        return(masses_of_modules)
    
def read_masses_of_modules(filename):
    f = open(filename, "r")
    masses_of_modules = []
    for line in f:
        masses_of_modules.append(int(line))
    
    return(masses_of_modules)
    
