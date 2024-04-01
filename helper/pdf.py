import os
from llama_index.readers import PDFReader
from helper.helper import get_index

def pdf_engine_generator(pdf_file_name, index_name):
    pdf_path = os.path.join("data", pdf_file_name)
    index_path = os.path.join("indices", index_name)
    reader_object = PDFReader().load_data(file=pdf_path)
    index = get_index(reader_object, index_path)
    engine = index.as_query_engine()
    return engine

jeff_resume_engine = pdf_engine_generator("jefferson.pdf", "jefferson")




