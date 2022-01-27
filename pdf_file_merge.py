import logging
import PyPDF2
from pdfFiles import filter_word_file_in_dir

logging.basicConfig(filename="C:/Users/vmuth/Downloads/check_logs.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class NoPDfFileError(Exception):
    pass

def merge_pdfs(pdf_files):
    filemerger = PyPDF2.PdfFileMerger()
    logging.debug("files to be merged are : {}".format(pdf_files))
    try:
        if pdf_files:
            for i in pdf_files:
                filemerger.append(PyPDF2.PdfFileReader(i, 'rb'))
                logging.info("file {} is merged successfully".format(i))
        else:
            raise "NoPDfFileError"
    except NoPDfFileError as p:
        logging.error("could not find pdf file in given directory")
    except Exception as e:
        logging.error("Error occured in pdf_file_merge.py")
        return False
    else:
        logging.info("No Exception during merging pdfs")
        filemerger.write("C:/Users/vmuth/Downloads/New_Merged_File.pdf")
    return True
