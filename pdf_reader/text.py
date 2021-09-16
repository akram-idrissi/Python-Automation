import os 
import PyPDF2

def get_text(path): 

	with open(path, 'rb') as f: 
		pdf = PdfFileReader(path)

		text = ""

		for page in range(pdf.getNumPages()): 
			page_object = getpage.getPage(page)
			text += page_object.extractText() 

	return text 

