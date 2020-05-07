# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:47:47 2020

@author: utente
"""

"""
import pygame, math

pygame.init()
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, size, position, heading, color=(0,0,0), depth=0):
    
    trunk_ratio = 0.29
    trunk = size*trunk_ratio  
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u,v)=position
    newposition = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, position, newposition)
    
    if order > 0:
        
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        
    else:
        color1 = color
        color2 = color
        
    
    newsize = size*(1-trunk_ratio)
    draw_tree(order-1, theta, newsize, position, heading-theta, color1, depth+1)
    draw_tree(order-1, theta, newsize, position, heading+theta, color2, depth+1)
    

def gameloop():
    
    theta = 0
    while True:
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;
            
        theta += 0.01
        
        main_surface.fill((255,255,0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2,surface_size-50), -math.pi/2)
        
        pygame.dispaly.flip()
        my_clock.tick(120)
        

gameloop()

pygame.quit()
"""

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def reflect_x(self):
        
        r = Point(self.x, -self.y)
        return r
    
    def slope_from_origin(self):
        
        if self.x == 0:
            s = 'nan'
        else:
            s = self.y/self.x
        return s
    
    def get_line_to(self, b):
        
        if self.x == b.x:
            line = (self.x, 'nan')
        else:
            m = (self.y-b.y)/(self.x-b.x)
            q = -self.x*m+self.y
            line = (m,q)
        
        return line
        
        

def distance(a,b):
    
    d = ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
    
    return d


class SMS_store():
    
    



