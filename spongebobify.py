import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap


def spongebobify(sentence):
	final_sentence = ''

	for word in sentence.split():
		for pos, letter in enumerate(word):
			if pos % 2 == 0:
				final_sentence += letter.lower()
			else:
				final_sentence += letter.upper()
		final_sentence += ' '

	return final_sentence


def build_image(spongbobified_sentence):
	image = Image.open('resources/mocking_spongebob.jpg')
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('/Library/Fonts/arial black.ttf', size=22)

	(W, H) = image.size
	y = 280
	
	for line in textwrap.wrap(spongbobified_sentence, width=32):
			(w, h) = draw.textsize(line, font=font)
			x = (W-w)/2

			draw.text((x-2, y-2), line, (0, 0, 0), font=font)
			draw.text((x+2, y-2), line, (0, 0, 0), font=font)
			draw.text((x+2, y+2), line, (0, 0, 0), font=font)
			draw.text((x-2, y+2), line, (0, 0, 0), font=font)
			draw.text((x, y), line, (255, 255, 255), font=font)

			y += font.getsize(line)[1]
	
	image.save('spongebobified.png')


build_image(spongebobify(sys.argv[1]))
