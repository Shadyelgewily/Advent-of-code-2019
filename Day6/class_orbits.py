# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:51:51 2020

@author: quiet
"""

import networkx as nx

class orbits():
    
    def __init__(self, filename):
        self.direct_orbits = self.read_direct_orbits_from_input(filename)
        self.create_digraph_from_direct_orbits()

    def read_direct_orbits_from_input(self, filename):
        input_file = open(filename, "r")
        direct_orbits_unprocessed = input_file.read().splitlines()
        input_file.close()
        
        direct_orbits = [tuple(x.split(')') ) for x in direct_orbits_unprocessed]
        return(direct_orbits)
    
    def create_digraph_from_direct_orbits(self):
        self.orbit_graph = nx.DiGraph()
        self.orbit_graph.add_edges_from(self.direct_orbits)
    
    #For each node, count all children nodes
    def count_all_orbits(self):
        self.n_orbits = 0
        for node in self.orbit_graph.nodes:
            self.n_orbits += len(nx.descendants(self.orbit_graph, node))
        return(self.n_orbits)
    
    def find_shortest_path_part2(self):
        self.find_orbited_objects_you_and_santa()
        self.nodes_shortest_path = nx.shortest_path(self.orbit_graph.to_undirected(), 
                                                     self.obj_orbited_by_you, 
                                                     self.obj_orbited_by_santa)
        self.N_edges_shortest_path = len(self.nodes_shortest_path) - 1
    
    def find_orbited_objects_you_and_santa(self):
        obj_orbited_by_you = [ obj[0] if obj[1] == 'YOU' else None for obj in self.direct_orbits]
        self.obj_orbited_by_you = list(filter(None.__ne__, obj_orbited_by_you))[0] 
        
        obj_orbited_by_santa = [ obj[0] if obj[1] == 'SAN' else None for obj in self.direct_orbits]
        self.obj_orbited_by_santa = list(filter(None.__ne__, obj_orbited_by_santa))[0]
    