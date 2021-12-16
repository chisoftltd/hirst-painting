import colorgram

rgb_colors = []
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)
print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
color_list = [(240, 231, 221), (228, 152, 86), (120, 171, 203), (1, 0, 0), (40, 111, 159), (240, 201, 83)]