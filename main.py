import colorgram
import random
import turtle as dot

# colors = colorgram.extract("hirst-painting.jpg", 2 ** 32)
# color_list = []
#
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)

color_palette = [(245, 245, 245), (31, 102, 156), (149, 23, 55), (224, 158, 51), (165, 64, 109), (234, 207, 216),
                 (217, 212, 50), (170, 72, 47), (42, 104, 61), (205, 223, 230), (205, 137, 175), (96, 170, 115),
                 (55, 37, 44), (39, 54, 121), (34, 36, 72), (22, 68, 58), (231, 188, 21), (56, 80, 48), (234, 241, 237),
                 (210, 100, 48), (244, 218, 7), (161, 101, 153), (47, 149, 185), (127, 160, 186), (217, 177, 190),
                 (109, 120, 159), (94, 154, 115), (180, 186, 212), (172, 203, 181), (226, 177, 166), (65, 81, 42),
                 (167, 200, 211), (58, 58, 57), (138, 43, 41)]


def change_color():
    rnd_col = random.choice(color_palette)
    R = rnd_col[0]
    G = rnd_col[1]
    B = rnd_col[2]
    colors = (R, G, B)
    return colors


dot.colormode(255)
dot.speed(25)
dot.penup()

x = 0
y = 0
dot_gap = 40
dot_size = 20

for i in range(10):
    dot.setx(x)
    dot.sety(y)

    for c in range(10):
        dot.pendown()
        dot.dot(dot_size, change_color())
        dot.penup()
        dot.forward(dot_gap)

    y += dot_gap

screen = dot.Screen()
screen.exitonclick()