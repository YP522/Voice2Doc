from generate.generateFolders import create_folder
from processing.convert import convert_file_to_wav, split_video_into_folder

import mimetypes

def checkFileType(file):
    """
    It checks the file type of the file passed to it and returns a string with the file type
    
    :param file: The file you want to check the type of
    """

    type_is = mimetypes.guess_type(file)[0]

    if type_is != None and "video" in type_is:
        print("its a video !")
    elif type_is != None and "audio" in type_is:
        print("its a audio !")        
    else:
        print("other!")

def run(file):
    """
    It creates a folder called "wav" and then converts the file to wav format
    
    :param file: The file you want to convert to wav
    """
    create_folder()
    convert_file_to_wav(file)