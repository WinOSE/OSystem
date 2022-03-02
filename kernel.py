from os import system 
from time import sleep

osename = "OSystem"
version = "alpha-0.0.1"
tag_version = ""

class osystem:
	def __init__(self):
		system("cls")
		self.loginSystem()
		self.startMensage()
		self.command_line()

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
		print(f"OSystem v({version}) {tag_version}")
		print(f"")
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
					cmd = cmd.replace("echo ")
					cmd = cmd.replace("echo")
					if cmd == "":
						print("Usage:  [echo][mensage]")
					else:
						print(cmd)
				elif cmd == "version":
					print(f"OSystem {version} {tag_version}")
					print(f"Developer: \033[35mWinOSE Studios\033[m")
				

				else:
					if cmd == "":
						pass
					else:
						print(f"{cmd}: Unknow Command")
			except Exception as e:
				print(f"Java.Exception.langIo.{e}")
osystem()


