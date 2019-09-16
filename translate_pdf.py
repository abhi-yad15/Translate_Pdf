from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
from googletrans import Translator
from win32com import client
import time
import os
import sys

def convert_pdf_to_doc(name):
	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	cd=os.getcwd()
	chrome_options.add_experimental_option('prefs', {
    "download.default_directory": cd
	})
	driver = webdriver.Chrome(options=chrome_options) 
	driver.get("https://www.foxitsoftware.com/pdf-to-word-converter/")
	print("------------------------\n Website Opened\n---------------------\n")
	wait = WebDriverWait(driver, 600)
	k="//*[@id=\"uploadifive-file_upload\"]/input[2]"
	button = wait.until(EC.presence_of_element_located((
	    By.XPATH, k)))
	driver.implicitly_wait(10)
	loc=cd+"/"+name
	button.send_keys(loc)
	time.sleep(20)
	print("------------------------\n File Uploaded\n---------------------\n")
	k="//*[@id=\"convert-submit\"]"
	button = wait.until(EC.presence_of_element_located((
	    By.XPATH, k))).click()
	#ActionChains(driver).move_to_element(button).click(button).perform()
	time.sleep(60)
	k="//*[@id=\"download-url\"]"
	button = wait.until(EC.presence_of_element_located((
	    By.XPATH, k)))
	ActionChains(driver).move_to_element(button).click(button).perform()
	time.sleep(30)
	print("------------------------\n Pdf_To_Doc_Converted\n---------------------\n")
	driver.quit()


def doc2pdf(doc_name, pdf_name):
    try:
        word = client.DispatchEx("Word.Application")
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc = word.Documents.Open(doc_name,ReadOnly = 1)
        worddoc.SaveAs(pdf_name, FileFormat = 17)
        worddoc.Close()
        return pdf_name
    except Exception as e:
        print(e)

def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def table_print(b):
    try:
        for row in b.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if(not len(paragraph.text)==0):
                        translator = Translator()
                        tran=translator.translate(paragraph.text , dest='hi')
                        paragraph.text=tran.text
    except Exception as e:
        for tc in b._tbl.iter_tcs():
            cell = _Cell(tc, b)
            for b_tc in iter_block_items(cell):
                if isinstance(b_tc, Paragraph):
                    if(not len(b_tc.text)==0):
                        try:
                            translator = Translator()
                            tran=translator.translate(b_tc.text , dest='hi')
                            b_tc.text=tran.text
                            print("_______Trasnlating______\n")
                        except:
                            pass



if __name__=='__main__':
	name=sys.argv[1]
	lang=sys.argv[2]
	convert_pdf_to_doc(name)
	#os.system("psiphon3.exe &")
	#time.sleep(60)
	doc=os.path.splitext(name)[0]+".docx"
	doc1=os.path.splitext(name)[0]+"_"+lang+".docx"
	document = Document(doc)
	for block in iter_block_items(document):
		if isinstance(block, Paragraph):
			try:
				if(not len(block.text)==0):
					translator = Translator()
					tran=translator.translate(block.text , dest=lang)
					print(block.text)
					block.text=tran.text
			except Exception as e:
				print(e)
		elif isinstance(block, Table):
				table_print(block)
	cd1=os.getcwd()
	doc_name = cd1+"/"+doc1
	name1=os.path.splitext(name)[0]+"_"+lang+".pdf"
	ftp_name = cd1+"/"+name1
	print(ftp_name)
	print(doc_name)
	document.save(doc1)
	doc2pdf(doc_name, ftp_name)
	os.remove(doc_name)
	os.remove(cd1+"/"+doc)


