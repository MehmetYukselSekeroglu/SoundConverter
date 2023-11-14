from soundlib.speec2text import voice2text
from soundlib.converter import GenericAudioConverter,SUPPORTED_SOUND_FORMATS
from soundlib.terminal_tools import InformationPrinter,ErrorPrinter,LogPrinter,WarnPrinter
from soundlib.terminal_tools import TitlePrinter
import pathlib
import argparse
import sys
import os
import shutil


args = argparse.ArgumentParser()
args.add_argument("-i",required=True,help="Input file path")
args.add_argument("-l",required=False,help="Target languages")
args = vars(args.parse_args())

input_file_path = pathlib.Path(args["i"])
input_file_str = args["i"]



if args["l"] == None:
    target_lang = "tr-TR"
else:
    target_lang = args["l"]
    

TEMP_DIR = "tmp"+os.sep

TitlePrinter(f"Powered By Prime")

if not os.path.exists(TEMP_DIR):
    InformationPrinter(f"Execute: mkdir {TEMP_DIR}.")
    os.makedirs(TEMP_DIR)

if not os.path.exists(input_file_str):
    ErrorPrinter(f"File '{input_file_str}' not found.")
    sys.exit(1)    



input_file_format = input_file_str.split(".")[-1].upper()

if input_file_format not in SUPPORTED_SOUND_FORMATS:
    ErrorPrinter(f"Format {input_file_format} not supported.")
    ErrorPrinter(f"Supported fortmats: {SUPPORTED_SOUND_FORMATS}")
    sys.exit(1)

if input_file_format != "WAV":
    data_is = GenericAudioConverter(
        target_file_path=input_file_str,
        TARGET_FILE_FORMAT="WAV",
        temp_dir_path=TEMP_DIR
    )
    
    if data_is["success"] != "true":
        ErrorPrinter("Failed to convert wav exiting...")
        ErrorPrinter(f"{data_is['code']}")
        sys.exit(1)
    
    WAV_PATH = data_is["path"]

else:
    WAV_PATH = input_file_path
    
    
    
InformationPrinter(f"Requesting Google Api pls wait...")

data_is = voice2text(target_file_path=WAV_PATH,lang_is=target_lang)

if data_is[0] != "true":
    ErrorPrinter(f"Speech2text proccess failed. exiting...")
    ErrorPrinter(f"{data_is[1]}")
    sys.exit(1)



InformationPrinter(f"Convert successfully. printing...")
print(f"------------- speec2text -------------")
print(data_is[1])
print("---------------------------------------")

InformationPrinter("Proccess complated.")
