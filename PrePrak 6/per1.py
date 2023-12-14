from PIL import ImageDraw, ImageFont, Image

gambarku = Image.open(r'D:\Pelajaran Kuliah\Praktikum\Smt 5\Pem. Fungsional\Modul 6\OrangOrangan.png')

# Convert the image to black and white
gambarBW = gambarku.convert("L")

# TODO 3: Add text according to the criteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('D:\Pelajaran Kuliah\Praktikum\Smt 5\Pem. Fungsional\Modul 6\krinkes\KrinkesDecorPERSONAL.ttf', 40)
text = "Capek Bangett"

# Get the bounding box of the text
text_bbox = draw.textbbox((0, 0), text, font)

# Calculate the position to center the text
text_x = (gambarku.width - text_bbox[2]) // 2
text_y = (gambarku.height - text_bbox[3]) // 2

# Draw the text on the image with white color
draw.text((text_x, text_y), text, font=font, fill=(120))

# TODO 4: Save the edited image using the save() function
gambarBW.save("percobaan1.png")

# TODO 5: Display the final result image
gambarBW.show()
