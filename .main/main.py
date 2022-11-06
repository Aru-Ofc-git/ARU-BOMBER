import os

if os.name == "nt":
	try:
		from bomber import windows
	except:
		os.system("pip install arubomber")
	windows.main()
else:
	try:
		from bomber import bomber
	except:
		os.system("pip install arubomber")
	bomber.main()
