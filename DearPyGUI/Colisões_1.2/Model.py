from dearpygui.dearpygui import * 
import math 

class BigLittleBall: 
    vel_x, vel_y = 0.0, 0.0  
    pos_x, pos_y = 0.0, 0.0 
    Ecx, Ecy     = 0.0, 0.0  
    mass         = 0.0
    num          = 0.0

    def __init__(self, pos : list, vel : list, mass : float, num : int ):
        self.num = num 
        self.pos_x, self.pos_y = pos
        self.vel_x, self.vel_y = vel 
        self.mass = mass 

    def update(self, delta_t : float ):
        self.pos_x += self.vel_x * delta_t 
        self.pos_y += self.vel_y * delta_t 

    def colision( self, other ): 
        self.vel_x  = (self.vel_x *( self.mass - other.mass ) + 2*other.vel_x*other.mass)/ (self.mass + other.mass)
        self.vel_y  = (self.vel_y *( self.mass - other.mass ) + 2*other.vel_y*other.mass)/ (self.mass + other.mass)
        other.vel_x = (other.vel_x*( other.mass - self.mass ) + 2*self.vel_x *self.mass) / (self.mass + other.mass)
        other.vel_y = (other.vel_y*( other.mass - self.mass ) + 2*self.vel_y *self.mass) / (self.mass + other.mass)
        
        

    def get_pos( self ):
        return [ self.pos_x, self.pos_y ]