from jproperties import Properties
from PIL import Image, ImageDraw, ImageFont
import math

image_path = ""
output_image_path = ""
font_path = ""


def main():
    dir(Image)
    file_name = output_image_path
    # picture = Image.open('D:\\MV5BODI5Mzk4NDYwNF5BMl5BanBnXkFtZTgwOTYzOTg4OTE@._V1_.jpg')

    # picture = picture.resize((int(picture.size[0] / 1), int(picture.size[1] / 1)))
    # dim = picture.size
    # print(f"This is the current width and height of the image: {dim}")
    # picture.save("Compressed_" + file_name, optimize=True, quality=80)

    image = Image.open(image_path)
    scaleFac = 0.9
    charWidth = 10
    charHeight = 18
    w, h = image.size
    image = image.resize((int(scaleFac * w), int(scaleFac * h * (charWidth / charHeight))), Image.NEAREST)
    w, h = image.size
    pixels = image.load()

    font = ImageFont.truetype(font_path, 15)
    outputImage = Image.new('RGB', (charWidth * w, charHeight * h), color=(0, 0, 0))
    draw = ImageDraw.Draw(outputImage)

    def getSomeChar(h):
        chars = "01"[::-1]
        charArr = list(chars)
        l = len(charArr)
        mul = l / 256
        return charArr[math.floor(h * mul)]

    for i in range(h):
        for j in range(w):
            r, g, b = pixels[j, i]
            grey = int((r / 3 + g / 3 + b / 3))
            pixels[j, i] = (grey, grey, grey)
            draw.text((j * charWidth, i * charHeight), getSomeChar(grey),
                      font=font, fill=(r, g, b))

    outputImage.save("../../output/name_for_output.png")

if __name__ == "__main__":
    main()