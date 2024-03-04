import colorgram
import random
import turtle as turtle_module
turtle_module.colormode(255)



rgb_colors = []
colors = colorgram.extract('image.jpg', 35)

# for color in colors:
#     rgb_colors.append(color.rgb)
# print((rgb_colors))

#colors in tuples
for color in colors:

    b = color.rgb.b
    r = color.rgb.r
    g = color.rgb.g
    new_color = (r, g, b)
    rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(226, 231, 236), (57, 106, 148), (224, 200, 110), (133, 85, 59), (222, 141, 65), (195, 145, 171), (234, 225, 203), (144, 179, 203), (224, 233, 230), (138, 82, 106), (209, 91, 68), (134, 182, 136), (187, 79, 121), (69, 104, 89), (236, 222, 230), (65, 155, 89), (133, 133, 75), (49, 155, 194), (183, 192, 201), (213, 178, 191), (22, 68, 111), (21, 59, 94), (226, 176, 168), (174, 202, 182), (115, 124, 149), (156, 207, 216), (70, 59, 48), (72, 64, 53), (119, 46, 42), (107, 48, 59), (53, 71, 65), (45, 66, 59)]
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

