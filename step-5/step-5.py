from PIL import Image, ImageDraw, ImageFilter

x_margin = 16
y_margin = 16
half_element_size = 30
null_radius  = 20
queen_radius = 27
null_color       = "#FFFFFF"
queen_color      = "#FF0000"
back_groud_color = "#4F81BD"
queen_position = (3, 5, 2, 8, 1, 7, 4, 6)

im = Image.new("RGB", (half_element_size*2*8 + x_margin*2, half_element_size*2*8 + y_margin*2), back_groud_color)
draw = ImageDraw.Draw(im)
for i in range(0,8):
    for j in range (0,8):
        circle_color = null_color
        circle_radius = null_radius
        if j==(queen_position[i]-1):
            circle_color = queen_color
            circle_radius = queen_radius
        bbox = (
            x_margin + (j*2+1)*half_element_size - circle_radius, 
            y_margin + (i*2+1)*half_element_size - circle_radius, 
            x_margin + (j*2+1)*half_element_size + circle_radius, 
            y_margin + (i*2+1)*half_element_size + circle_radius)

        draw.ellipse(bbox, fill=circle_color)

filtered_image = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=50, threshold=1) )
# filtered_image.show()
filtered_image.save("Equeen_CentSym.png", "PNG")
