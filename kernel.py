from os import system 
from time import sleep

osename = "OSystem"
version = "alpha-0.0.2"
tag_version = "Connection Update"
alocaent_drive = "0x800-1x200"

class osystem:
	def __init__(self):
		system("cls")
		self.loginSystem()
		self.startMensage()
		self.command_line()
		self.mainWindowTitleClass()

	def mainWindowTitleClass(self):
		system(f"title OSystem {version} {tag_version}")
		return True
	def loginSystem(self):
		# Tentar verificar se existe um nome de usuario
		try:
			a = open("login.json")
			a.close()
		except FileNotFoundError:
			print("Hello, Welcome to OSystem, please register")
			login = str(input("Create a Username: "))
			a = open("login.json", "wt+")
			a.write(login)
			a.close()
		else:
			pass

		# Verificar se existe uma senha
		try:
			a = open("bootSetups.json")
			a.close()
		except FileNotFoundError:
			password = str(input("Create a Password: "))
			a = open("bootSetups.json", "wt+")
			a.write(password)
		else:
			pass
	def startMensage(self):
		system("cls")
		print(f"\033[33mOSystem\033[m v(\033[35m{version}\033[m) {tag_version}")
		print(f"(C) \033[32m2022\033[m - https://github.com/WinOSE/OSystem - \033[36mFabric Datapack\n")
	def command_line(self):
		while True:
			try:
				cmd = str(input("\033[32m$\033[m "))
				if cmd == "shutdown":
					print("Ending all process of OSystem. . ."), sleep(0.83)
					print("Closing uncomplete tasks. . .     "), sleep(1.634)
					print("")
					print("Shutdown was effect with sucess!")
					break
				elif cmd.startswith("echo"):
					cmd = cmd.replace("echo ", "")
					cmd = cmd.replace("echo", "")
					if cmd == "":
						print("Usage:  [echo][mensage]")
					else:
						print(cmd)
				elif cmd.startswith("wget"):
					cmd = cmd.replace("wget ", "")
					cmd = cmd.replace("wget",  "")
					system(f"wget {cmd}")
				elif cmd == "version":
					print(f"OSystem {version} {tag_version}")
					print(f"Developer: \033[35mWinOSE Studios\033[m")
				elif cmd == "fabric":
					print("Fabric - Official Bootloader System")
					print(f"\033[34mWindows {alocaent_drive} - Drive of System\033[m")
				elif cmd == "update":
					system("wget https://github.com/WinOSE/kernel-updater/releases/download/2000/kernel-update.exe")
					system("start kernel_update.exe")
					break

				else:
					if cmd == "":
						pass
					else:
						print(f"{cmd}: Unknow Command")
			except Exception as e:
				print(f"Java.Exception.langIo.{e}")
			except KeyboardInterrupt:
				print(f"Java.Exception.keysIo.DriveTest.KeyboardInterrupt")
osystem()


