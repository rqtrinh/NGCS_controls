#import necessary libraries
import pygame
from pygame.locals import *
import json, os

#definition to instantiate variables in a json format
data = {}
data['Controls'] = []
data['Controls'].append({
    'UP' : 0,
    'DOWN' : 0,
    'LEFT' : 0,
    'RIGHT' : 0
})

#definition to initialize the controller
def Initialize_Controller():
    global button_keys, analog_keys, joysticks #set global variables
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()

    button_keys = {"x": 0, "circle": 1, "square": 2, "triangle": 3, "share": 4, "PS": 5, "options": 6, "left_stick_click": 7, 
        "right_stick_click": 8, "L1": 9, "R1": 10, "up_arrow": 11, "down_arrow": 12, "left_arrow": 13, "right_arrow": 14, "touchpad": 15}
    analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }

#defintion for inputs
def Inputs(mode, manual, running):
    global button_keys, analog_keys #set global variables
    for event in pygame.event.get():
        #check for mode
        #if mode is keyboard
        if mode == True:
            #handle keyboard press
            if event.type == KEYDOWN:
                if event.key == K_w:
                    data['Controls'][0]['UP'] = 1    
                if event.key == K_s:
                    data['Controls'][0]['DOWN'] = 1 
                if event.key == K_a:
                    data['Controls'][0]['LEFT'] = 1 
                if event.key == K_d:
                    data['Controls'][0]['RIGHT'] = 1 
                #to quit manual control
                if event.key == K_q:
                    running = False
                    manual = False
                #to switch to controller input
                if event.key == K_c:
                    mode = False                                    
            #handle keyboard release set values equal to 0
            elif event.type == KEYUP:
                if event.key == K_w:
                    data['Controls'][0]['UP'] = 0    
                if event.key == K_s:
                    data['Controls'][0]['DOWN'] = 0 
                if event.key == K_a:
                    data['Controls'][0]['LEFT'] = 0 
                if event.key == K_d:
                    data['Controls'][0]['RIGHT'] = 0
    
        #else mode is controller
        else:
            #handle controller press
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == button_keys['up_arrow']:
                    data['Controls'][0]['UP'] = 1    
                if event.button == button_keys['down_arrow']:
                    data['Controls'][0]['DOWN'] = 1 
                if event.button == button_keys['left_arrow']:
                    data['Controls'][0]['LEFT'] = 1 
                if event.button == button_keys['right_arrow']:
                    data['Controls'][0]['RIGHT'] = 1 
                #to quit manual control
                if event.button == button_keys['PS']:
                    running = False
                #to switch to keyboard control
                if event.button == button_keys['up_arrow']:
                    mode = True
            #handle controller release set values equal to 0
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == button_keys['up_arrow']:
                    data['Controls'][0]['UP'] = 0    
                if event.button == button_keys['down_arrow']:
                    data['Controls'][0]['DOWN'] = 0 
                if event.button == button_keys['left_arrow']:
                    data['Controls'][0]['LEFT'] = 0 
                if event.button == button_keys['right_arrow']:
                    data['Controls'][0]['RIGHT'] = 0
            #handle controller analog
            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value
                if abs(analog_keys[1]) > .4:
                    if analog_keys[1] < -.7:
                        data['Controls'][0]['UP'] = analog_keys[1]
                    else:
                        data['Controls'][0]['UP'] = 0
                    if analog_keys[1] > .7:
                        data['Controls'][0]['DOWN'] = analog_keys[1]
                    else:
                        data['Controls'][0]['DOWN'] = 0
                if abs(analog_keys[0]) > .4:
                    if analog_keys[0] < -.7:
                        data['Controls'][0]['LEFT'] = analog_keys[0]
                    else:
                        data['Controls'][0]['LEFT'] = 0
                    if analog_keys[0] > .7:
                        data['Controls'][0]['RIGHT'] = analog_keys[0]
                    else:
                        data['Controls'][0]['RIGHT'] = 0
        #update json file
        with open("data.json", "w") as write_file: 
            json.dump(data,write_file)
        # close if not running
        if (running == False):
            pygame.display.quit()
            pygame.quit()
            exit()