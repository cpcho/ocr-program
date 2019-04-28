try:
	from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
	import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

def ocr_core(filename):
	im = image_enhancer(filename)
	text = pytesseract.image_to_string(im, lang='chi_sim', config=tessdata_dir_config)
	return text

def image_enhancer(filename):
	im = Image.open(filename)
	im = im.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(im)
	im = enhancer.enhance(2)
	im = im.convert('1')
	return im