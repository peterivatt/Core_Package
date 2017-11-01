import os

##########################################################
### List of files in folder
##########################################################

# Create list of files in folder, filtered by starts with.
def folder2files(folder,startstr):
	# Opens folder and orders
	file_list = os.listdir(folder)
	file_list.sort()
	
	#Removes files that don't start with given string.
	for file in file_list:
		if file.startswith(startstr) != True:
			file_list.remove(file)
	return file_list
