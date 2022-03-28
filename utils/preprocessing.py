import chardet
import os
import re
import fitz
from pydantic import BaseModel
import docx as python_docx


class FormData(BaseModel):
    user_id: int
    company_id: int
    hash_id: int


def doc(path):
    input = python_docx.Document(path)
    data = ""
    full_text = []
    for para in input.paragraphs:
        full_text.append(para.text)
        data = '\n'.join(full_text)

    return data


def txt(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def pdf(path):
    fitz_doc = fitz.open(path)  # open document
    data = ""

    for page in fitz_doc:
        data = data + " " + page.get_text("text")

    return data


def identify_file_type(file_path: str):
    # Function to identify type of file
    try:
        if os.path.isdir(file_path):
            return "directory"
        extension = file_path[file_path.rindex(".") + 1:]
        if extension.isalnum():
            return extension
        else:
            return "unknown"

    except ValueError as e:
        return e


def preprocess_string(text: str):
    text = text.lower()
    text = re.sub('\r', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(r"[^a-zA-Z0-9. ]", "", text)
    text = re.sub(' +', ' ', text)
    text.strip()
    return text


def identify_text_encoding(text):
    # Function to identify encoding of given text body
    result = chardet.detect(text)
    char_enc = result['encoding']
    return {'encoding': char_enc}


def preprocessing_manager(path):
    try:
        file_extension = identify_file_type(path)
        # text = exec("{}.delay('{}')".format(file_extension, file_path))
        if file_extension == "txt":
            response = txt(path)
        elif file_extension == "pdf":
            response = pdf(path)
        elif file_extension == "doc":
            response = doc(path)
        elif file_extension == "docx":
            response = docx(path)
        else:
            pass

    except Exception as e:
        response = str(e)

    return response


docx = doc
