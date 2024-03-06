import sys
import cx_Freeze
from cx_Freeze import setup, Executable

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('tetrax.py', base = "Win32GUI")]

cx_Freeze.setup(
    name = "tetr_x!",
    options = {"build_exe" : 
        {"packages" : ["pygame"], "include_files" : ["save_file.csv", "tetrax.py",
                                                     "button.py", "tile.py",
                                                     "name.py", "highscore.py",
                                                     "score_field.py",

                                                     "title_col_1.png", "title_col_2.png", 
                                                     "title_col_3.png", "title_col_4.png", 
                                                     "title_col_5.png", "title_col_6.png", 
                                                     "title_col_7.png", "title_col_8.png",

                                                     "beep.mp3", "gameover.mp3", 
                                                     "intro.mp3", "level_1.mp3",
                                                     "level_2.mp3", "level_3.mp3",
                                                     "level_4.mp3", "level_5.mp3", 
                                                     "levelup.mp3", "linedown.mp3",
                                                     "lock.mp3", "newrecord.mp3", 
                                                     "tetrx.mp3", "turnl.mp3",
                                                     "turnr.mp3"]}}, 
    executables = executables
)