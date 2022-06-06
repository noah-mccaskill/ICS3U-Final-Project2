#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This will display the "space aliens" program on EdgeBadge

import ugame
import stage


def game_scene():
    # this function is for the main game game_scene
    
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    # set background to image 0 in the image Bank
    # and the side (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites 
    # most likely I will render the background once per game scene 
    game.render_block()
    
    # repeat forever, game loop
    while True:
        pass # temporary placeholder
    
if __name__ == "__main__":
    game_scene()
