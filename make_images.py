from PIL import Image, ImageDraw

# Create X image
x_img = Image.new("RGBA", (80, 80), (255, 255, 255, 0))
draw_x = ImageDraw.Draw(x_img)
draw_x.line((10, 10, 70, 70), fill="red", width=10)
draw_x.line((70, 10, 10, 70), fill="red", width=10)
x_img.save("x.png")

# Create O image
o_img = Image.new("RGBA", (80, 80), (255, 255, 255, 0))
draw_o = ImageDraw.Draw(o_img)
draw_o.ellipse((10, 10, 70, 70), outline="blue", width=10)
o_img.save("o.png")

print("✅ Images created successfully!")
