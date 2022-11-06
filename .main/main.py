try:
	from bomber import windows #windows
	from bomber import bomber #any os
	from bomber import linux #linux

	if os.name == "nt":
		windows.main()
	else:
		bomber.main()
except:
	import sys
	print('arubomber not installed')
	sys.exit()
