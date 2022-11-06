#import os

#if os.name == "nt":
#	try:
#		from bomber import windows
#	except:
#		os.system("pip install arubomber")
#	try:
#		windows.main()
#	except:
#		os.system("pip install --upgrade arubomber")
#else:
#	try:
#		from bomber import linux
#	except:
#		os.system("pip install arubomber")
#	try:
#		linux.main()
#	except:
#		os.system("pip install --upgrade arubomber")



import os,time
try:
	from bomber import bomber
except:
	print('arubomber not found')
	time.sleep(5)
	os.system('pip install --upgrade arubomber')

try:
	bomber.main()
except:
	print('found a error. Please connect with aru')
