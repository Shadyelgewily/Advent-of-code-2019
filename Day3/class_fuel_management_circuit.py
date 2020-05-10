import operator
import numpy

#To do: think (and implement) check if is_coordinate_on_vertical etc.
#is move vertical
#find direction between positions
#should be part of wire class and not of the circuit class
#define INDEX_CONSTANTS X_AXIS = 0, INDEX_Y_AXIS=0
#Make class 'Wirepiece' because we don't want to work with start position1, end position1 etc. all the time
class fuel_management_circuit():

    
    def __init__(self):
        self.wires = []
        self.intersections = []
    
    def add_wire(self, wire):
        self.wires.append(wire)
        pass
    
    #There are three cases:
    #a: The lines are both horizontal or both vertical and they have different y, or different x (no intersections)
    #b: The lines are both horizontal and have the same y (multiple interections), or the vertical case (x the same)
    #The (x,y) that they share are all intersections
    #c: One is verticla and the other is horizontal, there is exactly 1 intersection. The question is, does that
    #intersection take place within the "bounding box"?
    #Solve the c case first, then a and then b.
    def find_intersections(self, wire1, wire2):
        #(0,0) crosses with (0,0) but this one does not count
        positions_wire1 = [(0,0), (5,0), (5,2)]
        start_positions_wire1 = positions_wire1[0:-1]
        end_positions_wire1 = positions_wire1[1:]
        
        positions_wire2 = [(0,0), (7,0), (7,2)]
        start_positions_wire2 = positions_wire2[0:-1]
        end_positions_wire2 = positions_wire2[1:]
        
        #Step 1 find which coordinate has changed
        #Step 2 determine the distance
        #Create a list with all coordinates from start to end, using step 1 and 2
        #Do this for the current positions for each wire
        #Check whether there are any shared elements, if so, add this intersection
        
        #for each wire, pop the first two elements (first is start, second is end)
        #(or with a class wirepiece this would be a single wirepiece)
        #then  find intersection between wirepieces with all that comes to it
        #and add it to the intersection list
        #continue while loop until wire stacks are empty
        #then check for each of the intersections the manhattan distance
        #return the minimum 
        
        pass
    
    def find_direction_between_positions(self, start_position, end_position):
        return(tuple(map(operator.sub, end_position, start_position)))
    
    def is_move_horizontal(self, direction):
        return( direction[0] != 0 and direction[1] == 0 )
        
    def is_move_vertical(self, direction):
        return( direction[0] == 0 and direction[1] != 0 )
    
    def are_moves_perpendicular( self, direction_wire1, direction_wire2 ):
        if( ( self.is_move_horizontal(direction_wire1) and
            self.is_move_vertical(direction_wire2) ) or
            ( self.is_move_horizontal(direction_wire2) and
            self.is_move_vertical(direction_wire1) ) ):
            return True
        else:
            return False
        
    def are_wirepieces_parallel(self, wirepiece1, wirepiece2):
        if( wirepiece1.direction )
        pass
    
    def are_wirepieces_overlapping(self): 
        pass
    
    def find_intersection_if_perpendicular_directions(self, 
                                                      start_position_vertical_wirepiece,
                                                      start_position_horizontal_wirepiece):
        return( (start_position_vertical_wirepiece[0], start_position_horizontal_wirepiece[1]))


    def is_valid_perpendicular_intersection(self, intersection, 
                                            start_position_vertical_wirepiece, end_position_vertical_wirepiece,
                                            start_position_horizontal_wirepiece, end_position_horizontal_wirepiece):
        
        is_on_horizontal_wirepiece = self.is_coordinate_on_wirepiece( intersection,
                                                                      start_position_horizontal_wirepiece,
                                                                      end_position_horizontal_wirepiece)
        is_on_vertical_wirepiece = self.is_coordinate_on_wirepiece( intersection,
                                                                    start_position_vertical_wirepiece,
                                                                    end_position_vertical_wirepiece)
        
        return(is_on_horizontal_wirepiece and is_on_vertical_wirepiece)
    
    def is_coordinate_on_wirepiece(self, coordinate, 
                                            start_position_wirepiece, end_position_wirepiece):
        direction_wirepiece = self.find_direction_between_positions(start_position_wirepiece, end_position_wirepiece)
    
        if(self.is_move_horizontal(direction_wirepiece) ):
            is_on_wirepiece = self.is_coordinate_on_horizontal_wirepiece(coordinate, 
                                                                         start_position_wirepiece, 
                                                                         end_position_wirepiece)
        elif(self.is_move_vertical(direction_wirepiece) ):
            is_on_wirepiece = self.is_coordinate_on_vertical_wirepiece(coordinate, 
                                                                       start_position_wirepiece, 
                                                                       end_position_wirepiece)        
        
        return(is_on_wirepiece)

    #Todo: is_coordinate_on_horizontal/vertical_wirepiece violate the DNRY principle
    def is_coordinate_on_horizontal_wirepiece(self, coordinate, start_position_wire, end_position_wire ):
        min_x = min( start_position_wire[0], end_position_wire[0] )
        max_x = max( start_position_wire[0], end_position_wire[0] )
        
        if( min_x <= coordinate[0] <= max_x and 
           coordinate[1] == start_position_wire[1] and 
           coordinate[1] == end_position_wire[1] ):
            return True
        
        return False
    
    def is_coordinate_on_vertical_wirepiece(self, coordinate, start_position_wire, end_position_wire ):
        min_y = min( start_position_wire[1], end_position_wire[1] )
        max_y = max( start_position_wire[1], end_position_wire[1] )
        
        if( min_y <= coordinate[1] <= max_y and 
           coordinate[0] == start_position_wire[0] and 
           coordinate[0] == end_position_wire[0] ):
            return True
        
        return False

    #To do: there are actually four cases where they can be parallel and not overlapping
    #vertical lines: next to eachother, or same x coordinate but disjoint
    #horizontal lines: above eachother, or same y coordinate but disjoint
    def find_intersection_if_parallel_directions(self):
        return None
    
    def find_intersections_if_overlapping_directions(self, start_position_wirepiece1,
                                                     end_position_wirepiece1,
                                                     start_position_wirepiece2,
                                                     end_position_wirepiece2):
        overlapping_wirepiece = self.get_overlapping_part_wirepieces(start_position_wirepiece1,
                                                                     end_position_wirepiece1,
                                                                     start_position_wirepiece2,
                                                                     end_position_wirepiece2)
        direction_overlap = self.find_direction_between_positions(overlapping_wirepiece[0],
                                                                  overlapping_wirepiece[1])
        
        if(self.is_move_horizontal(direction_overlap)):
            intersections_x = list( range(overlapping_wirepiece[0][0], overlapping_wirepiece[1][0] + 1 ) )
            intersections_y = [overlapping_wirepiece[0][1]]
            intersections = list( zip( intersections_x, intersections_y * len(intersections_x)) )
        elif(self.is_move_vertical(direction_overlap)):
            intersections_x = [overlapping_wirepiece[0][0]]
            intersections_y = list( range(overlapping_wirepiece[0][1], overlapping_wirepiece[1][1] + 1) )
            intersections = list( zip( intersections_x * len(intersections_y), intersections_y))

        return intersections
        
    def get_overlapping_part_wirepieces(self, start_position_wirepiece1,
                                        end_position_wirepiece1,
                                        start_position_wirepiece2,
                                        end_position_wirepiece2):
        min_x_wirepiece1 = min(start_position_wirepiece1[0], end_position_wirepiece1[0] )
        max_x_wirepiece1 = max(start_position_wirepiece1[0], end_position_wirepiece1[0] )
        min_y_wirepiece1 = min(start_position_wirepiece1[1], end_position_wirepiece1[1] )
        max_y_wirepiece1 = max(start_position_wirepiece1[1], end_position_wirepiece1[1] )
        
        min_x_wirepiece2 = min(start_position_wirepiece2[0], end_position_wirepiece2[0] )
        max_x_wirepiece2 = max(start_position_wirepiece2[0], end_position_wirepiece2[0] )
        min_y_wirepiece2 = min(start_position_wirepiece2[1], end_position_wirepiece2[1] )
        max_y_wirepiece2 = max(start_position_wirepiece2[1], end_position_wirepiece2[1] )
        
        overlapping_wirepiece_point1_x = max(min_x_wirepiece1, min_x_wirepiece2 )
        overlapping_wirepiece_point1_y = max(min_y_wirepiece1, min_y_wirepiece2 )
        overlapping_wirepiece_point2_x = min(max_x_wirepiece1, max_x_wirepiece2 )
        overlapping_wirepiece_point2_y = min(max_y_wirepiece1, max_y_wirepiece2 )
        return( [(overlapping_wirepiece_point1_x, overlapping_wirepiece_point1_y),
                (overlapping_wirepiece_point2_x, overlapping_wirepiece_point2_y)] )
    
    def calc_manhattan_distance(self, point1, point2 ):
        distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        return(distance)
    
    