from PIL import Image

image_monro = Image.open("monro.jpg")
rgb_image_monro = image_monro.convert("RGB")

image_red, image_green, image_blue = rgb_image_monro.split()

coordinates1_red = (50, 0, image_red.width, image_red.height)
crop1_red = image_red.crop(coordinates1_red)

coordinates2_red = (25, 0, image_red.width-25, image_red.height)
crop2_red = image_red.crop(coordinates2_red)

coordinates1_blue = (0, 0, image_blue.width-50, image_blue.height)
crop1_blue = image_blue.crop(coordinates1_blue)

coordinates2_blue = (25, 0, image_blue.width-25, image_blue.height)
crop2_blue = image_blue.crop(coordinates2_blue)

coordinates1_green = (25, 0, image_green.width-25, image_green.height)
crop1_green = image_green.crop(coordinates1_green)

monro_blend_red = Image.blend(crop1_red, crop2_red, 0.5)
monro_blend_blue = Image.blend(crop1_blue, crop2_blue, 0.5)

new_image = Image.merge("RGB", (monro_blend_red, crop1_green, monro_blend_blue))
new_image.save("new_image.jpg")

new_image.thumbnail((80, 80))
new_image.save("resizer_image.jpg")
