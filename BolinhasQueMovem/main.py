from dearpygui.dearpygui import * 
from random              import random
from random              import randint
from Model               import BigLittleBall 
import math 

setup_viewport() 
maximize_viewport() 

NUM_BALLS = 20
w, h      = get_viewport_width(), get_viewport_height()
balls     = [ BigLittleBall( pos = [random()*w, random()*h], vel = [randint(-50,50), randint(-50,50)], mass = 25*random(), num = i) for i in range(NUM_BALLS)  ]

def verify_border( ball, max_x : float, max_y : float ):
    if ball.pos_x - ball.mass < 0 or ball.pos_x + ball.mass > max_x:  
        ball.vel_x *= -1
    if ball.pos_y - ball.mass < 0 or ball.pos_y + ball.mass > max_y:   
        ball.vel_y *= -1 
        

def verify_collision( one, other): 
    D = math.sqrt( (one.pos_x-other.pos_x)**2 + (one.pos_y-other.pos_y)**2 )
    if D < ( one.mass + other.mass ):
        one.colision( other )
        
def update_draw( ball, num : int ): 
    configure_item( 1001+num, center = balls[num].get_pos() )

with window( id = 1, no_resize = True ) as main_win : 
    add_drawlist( id = 1_000, width = get_item_width(1), height = get_item_height(1) )
    for i in range( NUM_BALLS ): 
        draw_circle( id = 1_001+i, center = balls[i].get_pos(), radius = balls[i].mass, color = (255,255,255,255) )

set_primary_window( main_win, True )
while is_dearpygui_running(): 
    render_dearpygui_frame() 
    
    dt_t = get_delta_time()
    
    for i in range( NUM_BALLS ):
        for j in range(i+1, NUM_BALLS):
            verify_collision(balls[i], balls[j])
    
        verify_border( balls[i], w, h )
    
        balls[i].update( dt_t*10 )
    
        update_draw( balls[i], i )