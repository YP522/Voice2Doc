from datetime import datetime


author  = "YP522"
email   = "yp@ypetit.web-edu.fr"
version = "0.0.0"
prefix  = "[V2D]"
name    = "Voice2Doc" 
line    = "#######################################################################################"
good    = "[√]"
bad     = "[X]"
errors  = ["File Not found", "Not the same size"]

#                                   TIME                                      #
now = datetime.now()
day = now.strftime("%d:%m:%Y")
time = now.strftime("%H:%M:%S")
dt_string = "output/"+now.strftime("%d-%m-%Y-%H-%M-%S")

#                                   CMDS                                      #


def log(elt):
    return print(f"{prefix} {elt}")


credits = f"{prefix} Create by {author}"


help = f"""
{line}
                  {name} {version} » HELP | What can I do to help you ?
{line}

    - help    : Get help for execute commands of {name}              {prefix}
    - version : Get current version of {name}                        {prefix}
    - about   : What is {name} ?                                     {prefix}
    - credits : Get current authors of {name}                        {prefix}

    - run [file] [output]: Generate a doc with {name} software!      {prefix}

{line}
"""

about = f"""
{line}
                  {name} {version} » About | What is {name}  ?
{line}

    {name} is a free python project for extract text from audio or audio-video

    V2T gives a doc report with the paragraph

    OutPut :

        * WAV files for extract text
        * DOC report synthesis of content

{line}

Credits : {credits}

"""
