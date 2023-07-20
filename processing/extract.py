import speech_recognition as sr
import os
from system import utils as u

from generate.generateDOCX import combine_word_documents, get_docx_files, makeDoc
from tqdm import tqdm

def fetchAllWav(path):
    """
    It takes a path to a directory, and for each file in that directory, it calls the function
    extract_from() on that file
    
    :param path: The path to the folder containing the wav files
    """
    for root, dirs, files in os.walk(path):
        for filename in tqdm(files):
            extract_from(os.path.join(path, filename))

import os
import speech_recognition as sr

def extract_from(source):
    """
    Prend en entrée le nom d'un fichier, extrait le texte du fichier, puis écrit le texte dans un nouveau fichier
    
    :param source: le chemin vers le fichier audio
    """
    r = sr.Recognizer()
    basename_without_ext = os.path.splitext(os.path.basename(source))[0]
    harvad = sr.AudioFile(source)

    with harvad as source:
        audio = r.record(source)

    try:
        val = r.recognize_google(audio, language="fr-FR")
    except sr.UnknownValueError:
        val = "[mot ou phrase non reconnue]"
    
    makeDoc(basename_without_ext, val)
    files = get_docx_files(u.dt_string+"/docs_chunks")
    combine_word_documents(files)
