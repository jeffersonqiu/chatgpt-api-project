import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index

def pdf_engine_generator(pdf_file_name, index_name):
    pdf_path = os.path.join("data", pdf_file_name)
    index_path = os.path.join("indices", index_name)
    reader_object = PDFReader().load_data(file=pdf_path)
    index = get_index(reader_object, index_path)
    engine = index.as_query_engine()
    return engine


# canada_engine = pdf_engine_generator("Canada.pdf", "canada")
jeff_resume_engine = pdf_engine_generator("jefferson.pdf", "jefferson")




