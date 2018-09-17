import re

# a = re.sub("s","法克",re.findall('thumbnail_(.*?).jpg','https://simg3.gelbooru.com/thumbnails/08/b1/thumbnail_08b162bdc0b67f69eef0bcadf02cf811.jpg')[0])

a = re.findall('thumbnail_(.*?).jpg','https://simg3.gelbooru.com/thumbnails/08/b1/thumbnail_08b162bdc0b67f69eef0bcadf02cf811.jpg')

print(
    a[-1]
)