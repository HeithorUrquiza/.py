# import colorgram

# colors = colorgram.extract("C:\\Users\\heith\\OneDrive\\Documentos\\GitHub\\Python_cods\\Projects\\Intermediate\\hirst_painting\\image.jpg", 30)

# list_colors = []

# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     rgb_color = (r, g, b)
    
#     list_colors.append(rgb_color)
    
# print(list_colors)

import turtle as t
import random

tom = t.Turtle()
tom.shape("classic")
tom.penup()
tom.hideturtle()
colors_list = [(199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191)]
tom.setpos(-100.0, -20.0) 
t.colormode(255)


y = -20.0
for step in range(101):
    tom.dot(20, random.choice(colors_list))
    tom.forward(50)
    y += 4.0
    
    if step % 10 == 0:
        tom.setpos(-100.0, y)
        
screen = t.Screen()
screen = t.exitonclick()
