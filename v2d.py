# _________________________________________________________________________________________________________________________________ #
#                                                                                                                                   #
#        __  __                                                     ___             ____                          Video & Audio     #
#       /\ \/\ \                __                                /'___`\          /\  _`\                         to word file     #
#       \ \ \ \ \      ___     /\_\       ___        __          /\_\ /\ \         \ \ \/\ \      ___       ___                     #
#        \ \ \ \ \    / __`\   \/\ \     /'___\    /'__`\        \/_/// /__         \ \ \ \ \    / __`\    /'___\                   #  
#         \ \ \_/ \  /\ \L\ \   \ \ \   /\ \__/   /\  __/           // /_\ \         \ \ \_\ \  /\ \L\ \  /\ \__/                   # 
#          \ `\___/  \ \____/    \ \_\  \ \____\  \ \____\         /\______/          \ \____/  \ \____/  \ \____\                  #
#           `\/__/    \/___/      \/_/   \/____/   \/____/         \/_____/            \/___/    \/___/    \/____/                  #
#                                                                                                                                   #
# _________________________________________________________________________________________________________________________________ #
                                                                             
from system import utils as u
from system import v2d_S as s
import typer
#####################################################################################################################################


class main():

    # Start Script
    app = typer.Typer()

    # Open help
    @app.command()
    def help():
        typer.echo(u.help)

    # Get the current version
    @app.command()
    def version():
        typer.echo(f"{u.prefix} Voice2Doc version : {u.version}")

    # Learn more about Voice2Doc
    @app.command()
    def about():
        typer.echo(u.about)

    # Learn more about PicChecK
    @app.command()
    def credits():
        typer.echo(u.credits)

   # Learn more about PicChecK
    @app.command()
    def run(file: str):
        s.run(file)

    # init app
    if __name__ == "__main__":
        app()