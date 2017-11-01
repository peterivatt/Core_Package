import os

def folder2files(folder,startstr):
	"""
	Returns a sorted, filtered list of files contained in a folder
	
	Parameters
	----------
	folder : string 
		The path to the folder to be opened.
	startstr : string
		Remove files that do not start with this string.
	
	Returns
	-------
	file_list : list, strings
		A list of filenames.
	"""
	
	file_list = os.listdir(folder)
	
	file_list.sort()
	
	for file in file_list:
		if file.startswith(startstr) != True:
			file_list.remove(file)
	
	return file_list
