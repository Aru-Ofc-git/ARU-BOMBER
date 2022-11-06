import os

if os.name == "nt":
	try:
		from bomber import windows
	except:
		os.system("pip install arubomber")
	try:
		windows.main()
	except:
		pass
else:
	try:
		from bomber import bomber
	except:
		os.system("pip install arubomber")
	try:
		bomber.main()
	except:
		pass
