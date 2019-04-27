try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

def ocr_core(filename):

	text = pytesseract.image_to_string(Image.open(filename), lang='chi_sim', config=tessdata_dir_config)
	return text

print(ocr_core('images/sample-png-files.png'))