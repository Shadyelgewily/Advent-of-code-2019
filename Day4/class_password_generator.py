# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:02:49 2020

@author: quiet
"""

import numpy as np
import itertools

class password_generator():
    LENGTH_PASSWORD = 6;

    def __init__(self, puzzle_input):
        self.MIN_PASSWORD = [int(x) for x in puzzle_input.split('-')][0]
        self.MAX_PASSWORD = [int(x) for x in puzzle_input.split('-')][1]
        
        self.generate_valid_passwords()
        
    def generate_valid_passwords(self):
        passwords_range = range(self.MIN_PASSWORD, self.MAX_PASSWORD+1)
        
        passwords_checked = [ p if self.is_password_meets_all_conditions(p) else None for p in passwords_range]
        self.valid_passwords = list(filter(None.__ne__, passwords_checked)) 
        
    def is_password_meets_all_conditions(self, password):
        if( self.is_password_in_range(password) and 
            self.is_nondecreasing_left_to_right(password) and 
            self.is_exactly_two_adjacent_digits_same(password)):
            return True
        else:
            return False
    
    def is_password_in_range(self, password):
        condition_min = (password >= self.MIN_PASSWORD)
        condition_max = (password <= self.MAX_PASSWORD)
        
        if(condition_min and condition_max):
            return True
        else:
            return False
    
    def is_exactly_two_adjacent_digits_same(self, password):
        sequences_of_same_digit =  [''.join(g) for _, g in itertools.groupby(str(password))]
        lengths_sequences = np.array([len(i) for i in sequences_of_same_digit])
        return(bool(np.any(lengths_sequences == 2)))
        
    def is_atleast_two_adjacent_digits_same(self, password):
        password = self.password_int_to_list(password)
        password_diffs = self.calc_diffs_adjacent_digits(password)
        
        if( 0 in password_diffs ):
            return True
        else:
            return False
    
    def is_nondecreasing_left_to_right(self, password):
        password = self.password_int_to_list(password)
        password_diffs = self.calc_diffs_adjacent_digits(password)
        
        if(np.any(password_diffs < 0 )):
            return False
        else:
            return True
        
    def password_int_to_list(self, password):
        return([int(x) for x in list(str(password))])
         
    def calc_diffs_adjacent_digits(self, password):
        return( np.array( [ password[i] - password[i-1] for i in range(1,len(password)) ]) )
        
    def get_valid_passwords(self):
        return self.valid_passwords
    
    def get_N_valid_passwords(self):
        return len(self.valid_passwords)
