# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:03:27 2020

@author: quiet
"""

import numpy as np
from collections import Counter
from PIL import Image

class image_decoder():
    
    def __init__(self, filename, image_width_px, image_height_px):
        self.load_encoded_image(filename);
        self.image_width_px = image_width_px
        self.image_height_px = image_height_px
        self.set_image_N_layers()
        self.layerize_encoded_image()
        self.find_layer_with_most_zeros()
        self.find_answer_to_part1()
        
    def load_encoded_image(self, filename):
        image_input =  open(filename, "r").read().rstrip('\n')
        self.encoded_image = [ int(d) for d in image_input ]
        return;
    
    def set_image_N_layers(self):
        self.image_N_layers = int( len(self.encoded_image) /
                                  ( self.image_width_px * self.image_height_px )
                                 )
        return;
        
    def layerize_encoded_image(self):
        self.encoded_image = np.array(self.encoded_image).reshape(
                self.image_N_layers, self.image_height_px, self.image_width_px )
        return;
        
    def find_layer_with_most_zeros(self):
        N_zeros_by_layer = np.count_nonzero(self.encoded_image == 0, axis=(1,2))
        self.layer_with_least_zeros = np.argmin(N_zeros_by_layer)
        return;
    
    def find_answer_to_part1(self):
        relevant_layer = self.encoded_image[self.layer_with_least_zeros,::]
        
        N_ones_in_layer = np.count_nonzero(relevant_layer == 1)
        N_twos_in_layer = np.count_nonzero(relevant_layer == 2)
        self.answer_part1 = N_ones_in_layer * N_twos_in_layer
        
    def decode_image(self):
        self.decoded_image = np.apply_along_axis(self.find_color_of_pixel, 0, self.encoded_image)
        return;
    
    def display_decoded_image(self):
        self.decode_image()
        decoded_image = Image.new('1', (self.image_width_px, self.image_height_px))
        image_pixels = decoded_image.load()
        for i in range(decoded_image.size[1]):
            for j in range(decoded_image.size[0]):
                image_pixels[j, i] = (self.decoded_image[i][j],)
        decoded_image.show()
        
    def find_color_of_pixel(self, pixel_layers ):
        pixels_without_transparant = list(filter( lambda x: x != 2, pixel_layers ))
        return(pixels_without_transparant[0])
    