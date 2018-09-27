from PIL import Image
import pytesseract

image = Image.open(u'./QQ截图20180927140753.png')
pytesseract.image_to_string(image)