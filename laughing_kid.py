import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap


def build_image(sentence):
    image = Image.open('resources/laughing_kid.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/Library/Fonts/arial black.ttf', size=24)

    (W, H) = image.size
    y = 25

    for line in textwrap.wrap(sentence, width=40):
        (w, h) = draw.textsize(line, font=font)
        x = (W - w) / 2

        draw.text((x - 2, y - 2), line, (0, 0, 0), font=font)
        draw.text((x + 2, y - 2), line, (0, 0, 0), font=font)
        draw.text((x + 2, y + 2), line, (0, 0, 0), font=font)
        draw.text((x - 2, y + 2), line, (0, 0, 0), font=font)
        draw.text((x, y), line, (255, 255, 255), font=font)

        y += font.getsize(line)[1]

    image.save('laughing_kidded.png')


build_image(sys.argv[1])
