import glob
import os
import logging

class EmptyListError(Exception):
    pass

def filter_word_file_in_dir(dir_name):
    logging.info('directory path provided by user is: {}'.format(dir_name))
    try:
        list_of_files = (filter( os.path.isfile,glob.glob(dir_name + '*.pdf')))
        pdf_files=list(list_of_files)
        if pdf_files==[]:
            raise EmptyListError
    except EmptyListError as e:
        logging.error("No Pdf files found in the given directory and hence no file to merge")
    except Exception as e1:
        logging.error(e1)
    else:
        logging.info("Pdf files to be merge identified successfully")        
    return pdf_files