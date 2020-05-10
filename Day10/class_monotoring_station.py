# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:02:24 2020

@author: quiet
"""

import itertools
import numpy as np
import math

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
        self.best_location = self.asteroid_locations[ np.argmax(self.N_visible_asteroids)]
        self.N_visible_at_best_location = np.max(self.N_visible_asteroids)
    
    #unique normalized direction vectors are visible
    def count_visible_asteroids_from_all(self):
        self.N_visible_asteroids = [ len(np.unique(self.direction_vectors[i],axis=0)) 
                                     for i in range(self.N_total_asteroids) ]
    
    def find_all_normalized_direction_vectors(self):
        asteroid_combos = list(itertools.permutations(self.asteroid_locations, 2))
        self.direction_vectors = np.array( [ self.calc_normalized_direction_from_to(from_a, to_a) 
                                    for from_a, to_a in asteroid_combos])
        self.direction_vectors = self.direction_vectors.reshape(self.N_total_asteroids,
                                                           self.N_total_asteroids-1,2)
        
    def calc_normalized_direction_from_to(self, from_asteroid, to_asteroid):
        direction = (to_asteroid[0] - from_asteroid[0], to_asteroid[1] - from_asteroid[1]) 
        #to avoid issues with float comparisons
        return( np.round( self.normalize_vector(direction), 3) )
    
    def normalize_vector(self, v):
        norm = np.linalg.norm(v)
        if norm == 0: 
           return v
        return v / norm;
    