import requests
import random
import string
import time
import os


class NitroGen:
	def __init__(file):
		file.fileName = "generated.txt"

	def main(cons):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▀██░██▄██▄░▄█░▄▄▀█▀▄▄▀█░██
██░█░█░██░▄██░██░▀▀▄█░██░█▄██
██░██▄░█▄▄▄██▄██▄█▄▄██▄▄██▀██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
		cons.slowType(
		    "This Discord Nitro scraper is made by codeisnotfunjk & optimized by MeowcaTheoRange\n",
		    .02)
		time.sleep(1)
		cons.slowType(
		    "By using this, you understand that this generator is for educational purposes only.\nMess with the code as you wish.\n",
		    .02)
		time.sleep(1)
		cons.slowType(
		    "LICENSE: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)",
		    .02)
		print("""___________________
| /--\            |
| |CC|  (i) (\\$\\) |
|-\--/---BY---NC--|
|_________________|
""")
		time.sleep(1)
		cons.slowType(
		    "\nHow many codes would you like to generate and check?: ",
		    .02,
		    newLine=False)
		gencode = int(input(''))
		cons.slowType("\nPress enter to confirm: ", .02, newLine=False)
		vercode = input('')
		vercode = vercode if vercode != "" else None
		cons.generator(gencode)
		#cons.checker(notify=vercode)
		input("\nThis is the end! Press Enter 5 times to close the program.")
		[input(input_thing) for input_thing in range(4, 0, -1)]

	def slowType(main, text, sleep_time, newLine=True):
		for i in text:
			print(i, end="", flush=True)
			time.sleep(sleep_time)
		if newLine:
			print()

	def generator(file, amount):
		with open(file.fileName, "w", encoding="utf-8") as txtfile:
			print("Please wait, generating for you...")
			timeTaken = time.time()
			for i in range(amount):
				code = "".join(
				    random.choices(string.ascii_uppercase + string.digits +
				                   string.ascii_lowercase,
				                   k=16))
				with open("list.md", "w", encoding="utf-8") as mdfile:
					strip_code = code
					req = requests.get(
					    f"https://discordapp.com/api/v6/entitlements/gift-codes/{strip_code}?with_application=false&with_subscription_plan=true"
					)
					if req.status_code == 200:
						print(f" Valid | {code} ")
						mdfile.write(
						    f"> ![VALID](assets/yes.png) Valid: {code}\n\n-\n\n"
						)
						break
						return 0
					elif req.status_code == 429:
						print(f" Rate-Limited | ( code {code} ) ")
						mdfile.write(
						    f"> ![RATELIMITED](assets/warn.png) Rate-limited: {code}\n\n-\n\n"
						)
					else:
						print(f" Invalid | {code} ")
						mdfile.write(
						    f"> ![INVALID](assets/no.png) Invalid: {code}\n\n-\n\n"
						)

	def checker(fileimport, notify=None):
		with open(fileimport.fileName, "r", encoding="utf-8") as txtfile:
			with open("list.md", "w", encoding="utf-8") as mdfile:
				for line in txtfile.readlines():
					strip_code = raw_code.strip("https://discord.gift/")
					req = requests.get(
					    f"https://discordapp.com/api/v6/entitlements/gift-codes/{strip_code}?with_application=false&with_subscription_plan=true"
					)
					if req.status_code == 200:
						print(f" Valid | {raw_code} ")
						mdfile.write(
						    f"> ![VALID](assets/yes.png) Valid: {raw_code}\n\n-\n\n"
						)
					elif req.status_code == 429:
						print(f" Rate-Limited | ( code {raw_code} ) ")
						mdfile.write(
						    f"> ![RATELIMITED](assets/warn.png) Rate-limited: {raw_code}\n\n-\n\n"
						)
					else:
						print(f" Invalid | {raw_code} ")
						mdfile.write(
						    f"> ![INVALID](assets/no.png) Invalid: {raw_code}\n\n-\n\n"
						)


if __name__ == '__main__':
	Gen = NitroGen()
	Gen.main()
