# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:02:24 2020

@author: quiet
"""

import itertools
import numpy as np
import pandas as pd

class monotoring_station():
    
    def __init__(self, filename):
        
        self.read_asteroid_map(filename)
        self.set_asteroid_locations()
        self.N_total_asteroids = len(self.asteroid_locations)
        self.find_all_normalized_direction_vectors()
        self.count_visible_asteroids_from_all()
    
    def read_asteroid_map(self, filename):
        asteroid_map = [line.rstrip('\n') for line in open(filename, "r")]
        self.asteroid_map = np.array([ list(line) for line in asteroid_map ])
    
    def set_asteroid_locations(self):
        asteroid_loc_x, asteroid_loc_y = np.nonzero(self.asteroid_map == '#' )
        self.asteroid_locations = list(zip(asteroid_loc_y, asteroid_loc_x))
        
    def find_best_station_location(self):
        self.best_station_index = np.argmax(self.N_visible_asteroids)
        self.best_station_location = self.asteroid_locations[self.best_station_index]
        self.N_visible_at_best_location = np.max(self.N_visible_asteroids)
        self.set_asteroid_directions_from_station()
        
    #unique normalized direction vectors are visible
    def count_visible_asteroids_from_all(self):
        self.N_visible_asteroids = [ len(np.unique(self.normalized_direction_vectors[i],axis=0)) 
                                     for i in range(self.N_total_asteroids) ]
    
    def find_all_normalized_direction_vectors(self):
        asteroid_combos = list(itertools.permutations(self.asteroid_locations, 2))
        self.direction_vectors = np.array( [ self.calc_direction_from_to(from_a, to_a) 
                                    for from_a, to_a in asteroid_combos])
        self.direction_vectors = self.direction_vectors.reshape(self.N_total_asteroids,
                                                           self.N_total_asteroids-1,2)
        self.normalized_direction_vectors = np.apply_along_axis(self.normalize_vector, 2, 
                                                                self.direction_vectors)
        
    def calc_direction_from_to(self, from_asteroid, to_asteroid):
        direction = (to_asteroid[0] - from_asteroid[0], to_asteroid[1] - from_asteroid[1]) 

        return(direction)
    
    def normalize_vector(self, v):
        norm = self.calc_distance_from_origin(v)
        if norm == 0: 
           return v
        #to avoid issues with float comparisons, we round off
        return np.round( v / norm, 3 );
    
    def calc_distance_from_origin(self, v):
        return(np.linalg.norm(v))
        
    def find_vaporize_order(self):
        #Maybe something with itertools groupby, because we can group by angle and sort on distance
        pass
    
    def calc_angles_from_station(self):
        angles = [ self.calc_angle_12oclock(v) for v in self.asteroid_directions_from_station]
        self.asteroid_angles_from_station = angles
    
    def calc_distances_from_station(self):
        distances = [ self.calc_distance_from_origin(v) for v in self.asteroid_directions_from_station ]
        self.asteroid_distances_from_station = distances
    
    #Refactoring needed
    def set_df_laser_instructions(self):
        other_asteroid_coordinates = np.array([self.calc_position_from_dir_to_station(d) 
                                        for d in self.asteroid_directions_from_station])
        self.calc_angles_from_station()
        self.calc_distances_from_station()
        
        self.df_laser_instructions = pd.DataFrame()
        self.df_laser_instructions['direction_vector' ] = [str(d) for d in self.asteroid_directions_from_station]
        self.df_laser_instructions['x_coordinate'] = other_asteroid_coordinates[:,0]
        self.df_laser_instructions['y_coordinate'] = other_asteroid_coordinates[:,1]
        
        self.df_laser_instructions['angle'] = self.asteroid_angles_from_station
        self.df_laser_instructions['distance'] = self.asteroid_distances_from_station
        self.df_laser_instructions.sort_values(['angle', 'distance' ], inplace=True)
        self.add_angle_occurence_to_laser_instructions()
        self.df_laser_instructions.sort_values(['ith_occurrence', 'angle'], inplace=True) 
        
    def calc_angle_12oclock(self, v):
        #Station is at origin, Up is +, right is +
        angle = np.arctan2(v[0], -v[1]) * 180 / np.pi
        angle = angle if angle >= 0 else 360 + angle
        return( np.round(angle,5) )
    
    def add_angle_occurence_to_laser_instructions(self):
        angles = self.df_laser_instructions['angle']
        counter = enumerate(angles)
        ith_occurrence = [np.sum(angles[:(i+1)] == elem) for i, elem in counter]
        self.df_laser_instructions['ith_occurrence' ] = ith_occurrence
        
    def set_asteroid_directions_from_station(self):
        self.asteroid_directions_from_station = self.direction_vectors[self.best_station_index] 
    
    #Something goes wrong here
    def calc_position_from_dir_to_station(self, direction):
        return( self.best_station_location + direction)
        
    def calc_answer_part2(self):
        asteroid_answer_part2 = self.df_laser_instructions.iloc[199]
        return(asteroid_answer_part2['x_coordinate'] * 100 + asteroid_answer_part2['y_coordinate']  )