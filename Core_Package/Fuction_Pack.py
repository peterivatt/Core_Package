import os

def folder2files(folder,startstr="",endstr=""):
	"""
	Returns a sorted, filtered list of files contained in a folder
	
	Parameters
	----------
	folder : string 
		The path to the folder to be opened.
	startstr : string, optional
		Remove files that do not start with this string.
	startstr : string, optional
		Remove files that do not end with this string.
	
	Returns
	-------
	file_list : list, strings
		A list of filenames.
	"""
	
	file_list = os.listdir(folder)
	
	file_list.sort()
	
	if startstr =! "":
		for file in file_list:
			if file.startswith(startstr) != True:
				file_list.remove(file)
	
	if endstr =! "":
		for file in file_list:
			if file.endswith(endstr) != True:
				file_list.remove(file)
	
	return file_list
