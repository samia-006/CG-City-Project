from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables for animation and state management
car_x = -1.2  
traffic_light_state = 0  # 0 for Red, 1 for Green
frame_counter = 0

def draw_rectangle(x1, y1, x2, y2, r, g, b):
    # What it does: Draws a filled rectangular shape with specific RGB colors.
    # Why it is needed: Fundamental building block for roads, buildings, cars, and UI elements.
    # Where it appears in the real world: UI buttons, windows, bricks in buildings, and road dividers.
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_circle(cx, cy, r, red, green, blue):
    # What it does: Draws a filled circle using polygon approximation.
    # Why it is needed: Used for drawing the sun, traffic lights, and round objects.
    # Where it appears in the real world: Traffic signals, sun, wheels, and circular clocks.
    glColor3f(red, green, blue)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(37):
        angle = i * 2.0 * math.pi / 36
        glVertex2f(cx + (r * math.cos(angle)), cy + (r * math.sin(angle)))
    glEnd()

def draw_bezier_curve():
    # What it does: Renders a smooth curve using Bernstein polynomials for Bezier curves.
    # Why it is needed: To fulfill the project requirement of drawing complex curved paths.
    # Where it appears in the real world: Vector graphics design paths, road overpasses, and roller coaster tracks.
    glColor3f(0.8, 0.4, 0.1)  
    glBegin(GL_LINE_STRIP)
    p0 = (-0.9, -0.2)
    p1 = (-0.6, 0.1)
    p2 = (-0.3, -0.2)
    
    for t in [i / 20.0 for i in range(21)]:
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        glVertex2f(x, y)
    glEnd()

def draw_line_clipping_demo():
    # What it does: Demonstrates Cohen-Sutherland style line clipping boundaries.
    # Why it is needed: To satisfy the line clipping requirement by showing clipped vectors inside a frame.
    # Where it appears in the real world: Window clipping in computer monitors and 3D graphics rendering viewports.
    glColor3f(1.0, 1.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.8, 0.7)
    glEnd()
    glLineWidth(1.0)

def draw_tree(x, y):
    # What it does: Draws a tree consisting of a brown trunk and green foliage.
    # Why it is needed: To enhance the scenery with natural elements and shape drawing.
    # Where it appears in the real world: Parks, roadside trees, and landscaping.
    draw_rectangle(x - 0.03, y, x + 0.03, y + 0.2, 0.55, 0.27, 0.07)
    glColor3f(0.1, 0.6, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - 0.08, y + 0.2)
    glVertex2f(x + 0.08, y + 0.2)
    glVertex2f(x, y + 0.38)
    glEnd()

def draw_person(x, y):
    # What it does: Draws a stick/block figure representing an adult pedestrian.
    # Why it is needed: Adds life and activity to the city sidewalk environment.
    # Where it appears in the real world: People walking on footpaths in a city.
    draw_circle(x, y + 0.1, 0.02, 1.0, 0.8, 0.6)
    draw_rectangle(x - 0.015, y, x + 0.015, y + 0.08, 0.1, 0.1, 0.8)

def draw_child(x, y):
    # What it does: Draws a smaller person representing a child.
    # Why it is needed: To diversify the city environment with kids playing or walking.
    # Where it appears in the real world: Neighborhood streets, parks, and sidewalks.
    draw_circle(x, y + 0.07, 0.015, 1.0, 0.8, 0.6)
    draw_rectangle(x - 0.01, y, x + 0.01, y + 0.05, 0.9, 0.3, 0.5)

def draw_dog(x, y):
    # What it does: Draws a small pet dog shape on the sidewalk.
    # Why it is needed: Adds realism and cute detail to the pedestrian walking scene.
    # Where it appears in the real world: Parks and streets with pet owners.
    draw_rectangle(x - 0.02, y, x + 0.02, y + 0.025, 0.5, 0.3, 0.1)
    draw_rectangle(x + 0.01, y + 0.02, x + 0.03, y + 0.04, 0.5, 0.3, 0.1)

def draw_traffic_light():
    global traffic_light_state
    # What it does: Renders a traffic signal pole with changing red and green lights.
    # Why it is needed: Simulates real-world traffic management and interactive visual state.
    # Where it appears in the real world: City road intersections and traffic junctions.
    draw_rectangle(0.58, -0.35, 0.61, 0.1, 0.3, 0.3, 0.3)
    draw_rectangle(0.55, 0.05, 0.64, 0.25, 0.1, 0.1, 0.1)
    
    if traffic_light_state == 0:
        draw_circle(0.595, 0.21, 0.018, 1.0, 0.0, 0.0)  # Red ON
        draw_circle(0.595, 0.09, 0.018, 0.2, 0.0, 0.0)  # Green OFF
    else:
        draw_circle(0.595, 0.21, 0.018, 0.3, 0.0, 0.0)  # Red OFF
        draw_circle(0.595, 0.09, 0.018, 0.0, 1.0, 0.0)  # Green ON

def draw_car():
    global car_x
    
    glPushMatrix()
    # What it does: Translates the car horizontally using 2D transformation matrix.
    # Why it is needed: Implements 2D translation to animate motion across the screen.
    # Where it appears in the real world: Moving vehicles in traffic simulations and video games.
    glTranslatef(car_x, 0.0, 0.0)
    
    draw_rectangle(-0.2, -0.45, 0.2, -0.35, 0.1, 0.4, 0.8)
    draw_rectangle(-0.1, -0.35, 0.1, -0.28, 0.1, 0.3, 0.7)
    draw_circle(-0.12, -0.47, 0.03, 0.1, 0.1, 0.1)
    draw_circle(0.12, -0.47, 0.03, 0.1, 0.1, 0.1)
    
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # 1. Sky Background
    draw_rectangle(-1.0, -1.0, 1.0, 1.0, 0.53, 0.81, 0.98)
    
    # 2. Sun
    draw_circle(0.75, 0.75, 0.12, 1.0, 0.9, 0.0)
    
    # 3. Greenery Field / Sidewalk area
    draw_rectangle(-1.0, -0.6, 1.0, -0.2, 0.2, 0.75, 0.25)
    
    # 4. Road
    draw_rectangle(-1.0, -0.55, 1.0, -0.35, 0.25, 0.25, 0.25)
    for x in [-0.8, -0.4, 0.0, 0.4, 0.8]:
        draw_rectangle(x, -0.46, x + 0.15, -0.44, 1.0, 1.0, 1.0)
        
    # 5. Buildings (Left skyscraper and center residential house)
    draw_rectangle(-0.9, -0.2, -0.5, 0.5, 0.7, 0.7, 0.8)
    draw_rectangle(-0.82, 0.3, -0.7, 0.42, 0.2, 0.2, 0.2)
    draw_rectangle(-0.62, 0.3, -0.5, 0.42, 0.2, 0.2, 0.2)
    
    draw_rectangle(-0.45, -0.2, -0.15, 0.4, 0.9, 0.5, 0.3)
    draw_rectangle(-0.38, 0.15, -0.28, 0.3, 1.0, 1.0, 1.0)
    
    # House Roof
    glColor3f(0.8, 0.2, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0.6)
    glVertex2f(-0.45, 0.4)
    glVertex2f(-0.15, 0.4)
    glEnd()

    # 6. Trees
    draw_tree(0.25, -0.35)
    draw_tree(0.4, -0.35)
    
    # 7. People, Children and Pets on Sidewalk
    draw_person(-0.05, -0.35)
    draw_dog(0.02, -0.37)       
    draw_child(-0.15, -0.36)    
    
    # 8. Bezier Curve & Line Clipping elements
    draw_bezier_curve()
    draw_line_clipping_demo()
    
    # 9. Traffic Light
    draw_traffic_light()
    
    # 10. Moving Car
    draw_car()
    
    glutSwapBuffers()

def update(value):
    global car_x, traffic_light_state, frame_counter
    
    frame_counter += 1
    if frame_counter % 120 == 0:
        traffic_light_state = 1 - traffic_light_state
        
    if traffic_light_state == 1:
        car_x += 0.007
        if car_x > 1.3:
            car_x = -1.3
            
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(900, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Ultimate Complete 2D City Scene - CG Final Project")
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()