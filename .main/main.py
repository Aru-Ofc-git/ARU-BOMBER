import os

if os.name == "nt":
	try:
		from bomber import windows
	except:
		os.system("pip install arubomber")
	try:
		windows.main()
	except:
		os.system("pip install --upgrade arubomber")
else:
	try:
		from bomber import linux
	except:
		os.system("pip install arubomber")
	try:
		linux.main()
	except:
		os.system("pip install --upgrade arubomber")