#!/usr/bin/env python3 



"""
		SoundConverter@PrimeSecurity	: 13.11.2023 19.14	: GNU GPL V3

Ses formatlarını hızlı ve kolay şekilde birbirie çevirmek ve ses den metne dönüştürmek için
basit bir python3 betiği. Format dönüştürme işlemleri çevrimdışı yapılabilirken ses den metne 
Google api kullandığı için online olmalıdır.


"""





import os
import sys
import shutil
import argparse
from soundlib.converter import SUPPORTED_SOUND_FORMATS, GenericAudioConverter
from soundlib.terminal_tools import ErrorPrinter,InformationPrinter,LogPrinter,WarnPrinter
from soundlib.terminal_tools import TitlePrinter
import pathlib

args = argparse.ArgumentParser()
args.add_argument("-i",required=True,help="Input file path")
args.add_argument("-o",required=True,help="Output file path without extensions.")
args.add_argument("-f",required=True,help="Target file format")
args = vars(args.parse_args())

input_file = args["i"]
output_file = args["o"]
target_format = args["f"].upper()
#input_file = pathlib.Path(input_file)
output_file = pathlib.Path(output_file)


TEMP_DIR = "tmp"

TitlePrinter(f"Powered By Prime")

if not os.path.exists(TEMP_DIR):
    InformationPrinter(f"Execute: mkdir {TEMP_DIR}.")
    os.makedirs(TEMP_DIR)

if not os.path.exists(input_file):
    ErrorPrinter(f"File '{input_file}' not found.")
    sys.exit(1)

if target_format not in SUPPORTED_SOUND_FORMATS:
    ErrorPrinter(f"Target file format '{target_format}' not supported.")
    ErrorPrinter(f"Supported formats: {SUPPORTED_SOUND_FORMATS}.")
    sys.exit(1)


input_file_format = input_file.split(".")[-1].upper()

if input_file_format == target_format:
    ErrorPrinter(f"target format == input format exiting...")
    sys.exit(1)

InformationPrinter(f"Traying to convert...")    
convert_result = GenericAudioConverter(
    target_file_path=input_file,
    temp_dir_path=TEMP_DIR,
    TARGET_FILE_FORMAT=target_format
)

if convert_result["success"] == "false":
    ErrorPrinter(f"Failed to convert file.")
    ErrorPrinter(f"{convert_result['code']}")
    sys.exit(1)
    

output_file_name = str(output_file) + "." +str(target_format).lower()
shutil.copy(src=convert_result['path'],dst=output_file_name)

InformationPrinter(f"Removing temp files...")
os.remove(convert_result["path"])
InformationPrinter(f"File successfully saved: {output_file_name}")
InformationPrinter(f"Proccess complated.")

