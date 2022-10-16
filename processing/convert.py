import os
from processing.extract import fetchAllWav
from system import utils as u

def convert_file_to_wav(file):
    """
    It takes a video file, converts it to a wav file, splits the wav file into 5 second chunks, and then
    converts each 5 second chunk into a spectrogram
    
    :param file: The file you want to convert to wav
    """

    basename_without_ext = os.path.splitext(os.path.basename(file))[0]

    os.system('ffmpeg -i "{}" -acodec pcm_s16le -ar 16000 "{}/{}.wav"'.format(file, "./"+u.dt_string, basename_without_ext))
    split_video_into_folder(u.dt_string+"/"+basename_without_ext+".wav","00","05","00")
    fetchAllWav(u.dt_string+"/wav_chunks")


def split_video_into_folder(file,hh,mm,ss):
    """
    It takes a video file, splits it into chunks of time, and saves each chunk as a separate wav file
    
    :param file: the video file to be split
    :param hh: hours
    :param mm: the number of minutes to split the video into
    :param ss: seconds
    """

    path = u.dt_string + "/wav_chunks/"

    os.system('ffmpeg -i "{}" -f segment -segment_time {}:{}:{} -c:a copy -acodec pcm_s16le -ar 16000 "{}/split_%03d.wav"'.format(file,hh,mm,ss,"./"+path))
