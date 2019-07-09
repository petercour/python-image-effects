import PIL.Image, PIL.ImageFilter
im = PIL.Image.open('image.png')
im2 = im.filter(PIL.ImageFilter.BLUR)
im2.save('image-blur.png', 'jpeg')
