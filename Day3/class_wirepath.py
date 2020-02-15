# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:16:43 2020

@author: quiet
"""

import operator

class wirepath():
    
    INSTRUCTION_UP = "U"
    INSTRUCTION_DOWN = "D"
    INSTRUCTION_RIGHT = "R"
    INSTRUCTION_LEFT = "L"
    
    def __init__(self, wire_input_sequence):
        self.wire_input_sequence = wire_input_sequence
        self.wire_position_sequence = []
        self.add_wire_position((0,0))
        self.process_wire_input_sequence()
    
    #To do: use list comprehension, because we know the length of tehe wire_position length
    def add_wire_position(self, position):
       self.wire_position_sequence.append(position)
       
    def process_wire_input_sequence(self):
        wire_input_sequence = self.wire_input_sequence.copy() #deepcopy?
        
        while( self.has_next_wirepath_position(wire_input_sequence) ):
            try:
                next_instruction = wire_input_sequence.pop(0)
                direction = next_instruction[0]
                distance = int(next_instruction[1:])
            
                if( direction == self.INSTRUCTION_UP ):
                    self.move_to_next_position((0,distance))
                elif( direction == self.INSTRUCTION_DOWN ):
                    self.move_to_next_position((0,-distance))
                elif( direction == self.INSTRUCTION_RIGHT ):
                    self.move_to_next_position((distance,0))
                elif( direction == self.INSTRUCTION_LEFT ):
                    self.move_to_next_position((-distance,0))
                else:
                    raise IndexError()
            except IndexError:
                raise;

    def move_to_next_position(self, direction_tuple):
        position = tuple(map(operator.add, self.get_wire_position(), direction_tuple))
        self.add_wire_position(position)
        
    def has_next_wirepath_position(self, wire_input_sequence):
        return( len( wire_input_sequence) > 0 )
        
    def get_wire_position(self):
        return(self.wire_position_sequence[-1])
        
    def get_wire_position_sequence(self):
        return(self.wire_position_sequence)
