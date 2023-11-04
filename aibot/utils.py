from enum import Enum
from pathlib import Path

default_manifest = """{
    "aidoc": "AI_DOCUMENT_LOADER"
}
"""

def write_default_manifest(filepath):
    filepath = Path(filepath)

    if not filepath.parent.is_dir():
        print(f"Parent directory doesn't exists for {filepath}")
        return
    
    if filepath.is_file():
        print(f"File already exists at {filepath}")
        return
    
    try:
        with open(filepath, 'w') as file:
            file.write(default_manifest)
    
    except IOError as e:
        print(f"Error writing default inventory manifest: {e}")

def create_embeddings_from_pdf(filepath, save_directory):
    from langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import Chroma
    from langchain.embeddings import OpenAIEmbeddings

    loader = PyPDFLoader(str(filepath))

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(loader.load())

    vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory=str(save_directory))
    vectordb.persist()

    return vectordb

class ContentTypes(Enum):
    AUDIO       = 'audio/mpeg'
    JPEG        = 'image/jpeg'
    PNG         = 'image/png'
    SVG         = 'image/svg+xml'
    PDF         = 'application/pdf'
    MARKDOWN    = 'text/markdown'
    CSV         = 'text/csv'
    OBJ         = 'model/obj'
    PLAIN_TEXT  = 'text/plain'