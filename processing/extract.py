import speech_recognition as sr
import os

from generate.generateDOCX import makeDoc

def fetchAllWav(path):
    """
    It takes a path to a directory, and for each file in that directory, it calls the function
    extract_from() on that file
    
    :param path: The path to the folder containing the wav files
    """

    for root, dirs, files in os.walk(path):
        for filename in files:
    
            extract_from(path+"/"+filename)

def extract_from(source):
    """
    It takes a file name as input, extracts the text from the file, and then writes the text to a new
    file
    
    :param source: the path to the audio file
    """
    r=sr.Recognizer()

    basename_without_ext = os.path.splitext(os.path.basename(source))[0]

    harvad=sr.AudioFile(source)

    with harvad as source:
        audio=r.record(source)

    val=r.recognize_google(audio, language="fr-FR")
    makeDoc(basename_without_ext,val)
