import os

def print_logo():
    logo= """\033[38;5;14m\n\033[38;5;14m                   -++ooooooo++-\n\033[38;5;14m                -oo:``       `./so.\n\033[38;5;14m              `so.               .so`\n\033[38;5;14m             .h-                   :y`\n\033[38;5;14m            `d-                     :h\n\033[38;5;14m            +o                       y:\n\033[38;5;14m            h-                       /s\n\033[38;5;14m            h:                       +s\n\033[38;5;14m            /s                       h:\n\033[38;5;14m            `d:`                  ``/y\n\033[38;5;198m       `-+oo+\033[38;5;12mohho\033[38;5;198moo:`       \033[38;5;220m `:+ooo\033[38;5;10mdho\033[38;5;220m +o+-\n\033[38;5;198m     -so:`    \033[38;5;14m +y-\033[38;5;198m`:os/   \033[38;5;220m :so:`\033[38;5;14m :y/   \033[38;5;220m  ./os-\n\033[38;5;198m   .y+`        \033[38;5;14m `+so:\033[38;5;198m`:y:\033[38;5;220m:y/ \033[38;5;14m.:os/    \033[38;5;220m      `+y.\n\033[38;5;198m  :h.            \033[38;5;14m  `:+oo\033[38;5;15mNNo\033[38;5;14moo+-`          \033[38;5;220m    .h:\n\033[38;5;198m -h`                 \033[38;5;220m  +s\033[38;5;198mso                 \033[38;5;220m  `h-\n\033[38;5;198m h-                  \033[38;5;220m `m`\033[38;5;198m`m`                 \033[38;5;220m  -h\n\033[38;5;198m N                   \033[38;5;220m :y \033[38;5;198m y:                 \033[38;5;220m   N\n\033[38;5;198m N                   \033[38;5;220m :h \033[38;5;198m h:                 \033[38;5;220m   N\n \033[38;5;198mh:                  \033[38;5;220m `m`\033[38;5;198m`m`                 \033[38;5;220m  :h\n \033[38;5;198m.h`                 \033[38;5;202m  /ss/                  \033[38;5;220m `h-\n  \033[38;5;198m:y-                 \033[38;5;202m `dd`               \033[38;5;220m   .y:\n   \033[38;5;198m.s+.              `/y:\033[38;5;220m:y/`              .+s.\n     \033[38;5;198m-oo/.``     ``:oo:  \033[38;5;220m  :oo:``      `./oo-\n        \033[38;5;198m-/++oooo+++:`    \033[38;5;220m    `:+++oo+o+++- \033[0m\n"""
    title="""     _____     _                 _\n    |_   _|___|_|___ ___ ___ _ _| |_ _ _____ \n      | | |  _| | .'|   | . | | | | | |     |\n      |_| |_| |_|__,|_|_|_  |___|_|___|_|_|_|\n                        |___|"""
    term_size, term_height = os.get_terminal_size().columns, os.get_terminal_size().lines
    if term_height > 30: print(int((term_height-35)/2)*"\n")
    if term_size > 50:
        print(int((term_size-50)/2)*" "+logo.replace("\n","\n"+int((term_size-50)/2)*" "))
        print(int((term_size-50)/2)*" "+title.replace("\n","\n"+int((term_size-50)/2)*" "))
        url = "github.com/PersephoneKarnstein/triangulum"
        print(int((term_size-len(url))/2)*" "+url+"\n\n")
        if term_height > 30: print(int((term_height-35)/2)*"\n")
    else: print("\n Welcome to Triangulum, a fuzzy triangulation solver.\n\n")

