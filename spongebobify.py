import sys
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap


def spongebobify(sentence):
	final_sentence = ''
	words = sentence.split()
	
	for word in words:
		for pos, letter in enumerate(word):
			if pos%2 == 0:
				final_sentence += letter.lower()
			else:
				final_sentence += letter.upper()
		final_sentence += ' '

	return final_sentence


def build_image(spongbobified_sentence):
	image = Image.open('resources/mocking_spongebob.jpg')
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('/Library/Fonts/arial black.ttf', size=18)

	message = spongbobified_sentence

	(W, H) = image.size
	y = 300
	
	for line in textwrap.wrap(message, width=45):
			(w, h) = draw.textsize(line, font=font)
			x = (W-w)/2

			draw.text((x-2, y-2), line,(0,0,0),font=font)
			draw.text((x+2, y-2), line,(0,0,0),font=font)
			draw.text((x+2, y+2), line,(0,0,0),font=font)
			draw.text((x-2, y+2), line,(0,0,0),font=font)
			draw.text((x, y), line, (255,255,255), font=font)

			y += font.getsize(line)[1]
	
	image.save('spongebobified.png')


build_image(spongebobify(sys.argv[1]))