from PIL import Image
import pytesseract 

image='image1.jpg'
image2='image2.jpg'
imgObj=Image.open(image)
imgObj2=Image.open(image2)
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(imgObj)
text2 = pytesseract.image_to_string(imgObj2)
print(text)
print(text2)