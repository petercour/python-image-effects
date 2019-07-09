import PIL.Image
im = PIL.Image.open('image.png')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('image_resize.png', 'jpeg')
