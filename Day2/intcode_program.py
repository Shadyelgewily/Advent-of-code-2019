# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:19:46 2020

@author: quiet
"""

import numpy
import itertools
#I think the aim of the game is to replace the values at addresses 1 and 2 by
#integers in [0,99] and then checking which noun and verb lead to the answer in position 0
#So we need a new function find_noun_and_verb_that_produces_output()
#intcode_after_computer_caught_fire ==> memory_initial_state
class intcode_program():
    OPCODE_SUM = 1
    OPCODE_MULTIPLY = 2
    OPCODE_QUIT = 99
    STEP_PARAMETER1 = 1
    STEP_PARAMETER2 = 2
    STEP_INSTRUCTION_RESULT = 3
    STEP_NEXT_INSTRUCTION_POINTER = 4

    VALID_OPCODES = [OPCODE_SUM, OPCODE_MULTIPLY, OPCODE_QUIT]
    VALID_NOUNS = range(0,100)
    VALID_VERBS = range(0,100)
    
    initial_memory_state = None
    current_memory_state = None
    instruction_pointer = None
    current_opcode = None
    
    def __init__(self, initial_memory_state):
        self.initial_memory_state = initial_memory_state
        self.reset_memory_to_initial_state()
                        
    def restore_gravity_assist_program(self):
        
        self.replace_value_at_memory_address(1, 12)
        self.replace_value_at_memory_address(2, 2)
        self.execute_intcode_program()
        
        return(self.get_current_memory_state())
        
    def find_noun_and_verb_that_produces_output(self, desired_answer):
        #make sure to reset memory at each iteration to initial state
        
        valid_nouns_and_verbs = list(itertools.product( self.VALID_NOUNS, self.VALID_VERBS ))
        
        for index, noun_and_verb in enumerate( valid_nouns_and_verbs):
            noun, verb = noun_and_verb
            
            self.reset_memory_to_initial_state()
            self.replace_value_at_memory_address(1, noun)
            self.replace_value_at_memory_address(2, verb)
            self.execute_intcode_program()
            answer = self.get_intcode_program_answer()
            
            if( answer == desired_answer ):
                return( 100 * noun + verb )
                
    def execute_intcode_program(self):
        
        while( self.is_not_intcode_program_finished() ):
            instruction_parameters = self.get_parameters_for_next_instruction()
            result_address = self.get_address_to_store_next_instruction_result()
            
            instruction = self.get_current_instruction()
            self.replace_value_at_memory_address(result_address, 
                                                 instruction(instruction_parameters))
            
            self.set_next_instruction_pointer_and_opcode_value()
        return(True)
    
    def get_parameters_for_next_instruction(self):
        address_parameter1 = self.get_address_of_instruction_parameter(
                            self.instruction_pointer + self.STEP_PARAMETER1)
        address_parameter2 = self.get_address_of_instruction_parameter(
                            self.instruction_pointer + self.STEP_PARAMETER2)
        parameter_values = (self.get_intcode_value_from_address(address_parameter1),
                        self.get_intcode_value_from_address(address_parameter2))
        return(parameter_values)
    
    def get_address_of_instruction_parameter(self, memory_address):
        try:
            if(memory_address > len(self.current_memory_state)):
                raise IndexError()
            return(self.current_memory_state[memory_address])
        except IndexError:
            raise

    def get_intcode_value_from_address(self, memory_address):
        try:
            if(memory_address > len(self.current_memory_state)):
                raise IndexError()
            return(self.current_memory_state[memory_address])
        except IndexError:
            raise
            
    def get_address_to_store_next_instruction_result(self):
        result_address = self.get_intcode_value_from_address(
                            self.instruction_pointer + 
                            self.STEP_INSTRUCTION_RESULT)
        return(result_address)
    
    def get_current_instruction(self):
        try:
            if(self.current_opcode == self.OPCODE_SUM):
                return(sum)
            elif(self.current_opcode == self.OPCODE_MULTIPLY):
                return(numpy.prod)
            else:
                raise ValueError('Current instruction is neither sum nor multiply.')
        except ValueError:
            raise
    
    def replace_value_at_memory_address(self, memory_address, value):
        try:
            self.current_memory_state[memory_address] = value
            return(True)
        except IndexError:
            raise
    
    def reset_memory_to_initial_state(self):
        self.current_memory_state = self.initial_memory_state.copy()
        self.set_first_instruction_pointer_and_opcode_value()
    
    def set_first_instruction_pointer_and_opcode_value(self):
        self.set_first_instruction_pointer()
        self.set_opcode_value_from_instruction_pointer()
        return(True)
        
    def set_first_instruction_pointer(self):
        #To do: split up in two methods
        self.instruction_pointer = 0
        return(True)
    
    def set_opcode_value_from_instruction_pointer(self):
        try:
            opcode = self.current_memory_state[self.instruction_pointer]
            if(self.is_opcode_invalid(opcode)):
                raise ValueError('Opcode ' + str(opcode) + ' is invalid.')
            self.current_opcode = opcode
        except ValueError:
            raise
        return(True)
        
    def set_next_instruction_pointer_and_opcode_value(self):
        self.set_next_instruction_pointer()
        self.set_opcode_value_from_instruction_pointer()
        return(True)
        
    def set_next_instruction_pointer(self):
        try:
            if( self.instruction_pointer + self.STEP_NEXT_INSTRUCTION_POINTER > len(self.current_memory_state) ):
                raise IndexError('There is no next instruction pointer.')
            self.instruction_pointer += self.STEP_NEXT_INSTRUCTION_POINTER
        except IndexError:
            raise
        return(True)
        
    def is_not_intcode_program_finished(self):
        return( self.current_opcode != self.OPCODE_QUIT )
        
    def is_opcode_invalid(self, opcode):
        return( opcode not in self.VALID_OPCODES)
        
    def get_current_memory_state(self):
        return(self.current_memory_state)
        
    def get_intcode_program_answer(self):
        memory_state = self.get_current_memory_state()
        return(memory_state[0])
    
    def get_opcode(self):
        return(self.current_opcode)