# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:16:43 2020

@author: quiet
"""

import operator

MOVE_UP = "U"
MOVE_DOWN = "D"
MOVE_RIGHT = "R"
MOVE_LEFT = "L"
MOVE_HORIZONTAL = "H"
MOVE_VERTICAL = "V"
X_COORDINATE_INDEX = 0
Y_COORDINATE_INDEX = 1

class wirepath():
    

    
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
            
            #Change this code to: add wirepiece(next_instruction)
                if( direction == self.MOVE_UP ):
                    self.move_to_next_position((0,distance))
                elif( direction == self.MOVE_DOWN ):
                    self.move_to_next_position((0,-distance))
                elif( direction == self.MOVE_RIGHT ):
                    self.move_to_next_position((distance,0))
                elif( direction == self.MOVE_LEFT ):
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

class wirepiece():
    
    move_to = None
    start_position = (None, None)
    end_position = (None, None)
    
    horizontal_or_vertical = None
    direction = None
    distance = 0
    
    def __init__(self, current_position, move_to):
        self.move_to = move_to
        self.set_direction_indicator()
        self.set_direction_tuple()
        self.set_distance()
        self.start_position = current_position
        self.set_end_position()
    
    def set_direction_indicator(self):
        self.direction_indicator = self.move_to[0]
        
    def set_direction_tuple(self):
        if( self.get_direction_indicator() == self.MOVE_UP ):
            self.direction_tuple = (0,self.distance)
        elif( self.get_direction_indicator() == self.MOVE_DOWN ):
            self.direction_tuple = (0,-self.distance)
        elif(self.get_direction_indicator()== self.MOVE_RIGHT ):
            self.direction_tuple = (self.distance, 0)
        elif(self.get_direction_indicator() == self.MOVE_LEFT ):
            self.direction_tuple = (-self.distance, 0)
    
    def set_end_position(self):
        self.new_position = tuple(map(operator.add,
                                 self.get_start_position(),
                                 self.direction_tuple))
    def set_distance(self):
        self.distance = int(self.move_to[1:])
        pass
    
    def get_direction_indicator(self):
        return(self.direction_indicator)
    
    def get_horizontal_or_vertical(self):
        
        try:
            if(self.get_direction_indicator() == MOVE_LEFT or 
               self.get_direction_indicator() == MOVE_RIGHT ):
                return(MOVE_HORIZONTAL)
            elif(self.get_direction_indicator() == MOVE_UP or 
                 self.get_direction_indicator() == MOVE_DOWN ):
                return(MOVE_VERTICAL)
            else:
                raise IndexError("Invalid move direction.")
        except IndexError:
            raise
    
    def get_distance(self):
        return(self.distance)
        
    def get_start_position(self):
        return(self.start_position)
    
    def get_end_position(self):
        return(self.end_position)
    
        
    