from system import utils as u
from pathlib import Path

def create_folder():
    """
    Create folders for the project
    """
    Path(u.dt_string+"/wav_chunks/").mkdir(parents=True, exist_ok=True)
    Path(u.dt_string+"/docs_chunks/").mkdir(parents=True, exist_ok=True)    