import os

def folder2files(folder, startstr="", endstr=""):
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
	out : list, strings
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

def unitconvert(a, weight=("kg","kg"), length=("m","m"), area=("m2","m2"), volume=("m3","m3"), mixingR("pp","pp"), time=("s","s")):
	"""
	Converts a number to new units
	
	Parameters
	----------
	a : float or integer
		The number to be converted.
	weight : tuple, optional
		First string in tuple represents the current unit of weight the second string represents the target unit.
	length : tuple, optional
		First string in tuple represents the current unit of lenght the second string represents the target unit.
	area : tuple, optional
		First string in tuple represents the current unit of area the second string represents the target unit.	
	volume : tuple, optional
		First string in tuple represents the current unit of volume the second string represents the target unit.
	mixingR : tuple, optional
		First string in tuple represents the current unit of mixingR the second string represents the target unit.
	time : tuple, optional
		First string in tuple represents the current unit of time the second string represents the target unit.
	
	Returns
	-------
	out : float
		The original number converted into target units.
	"""
	
	Unit_Dict = {"kg" : 1.,\
				 "g"  : 1.E-3,\
				 "mg" : 1.E-6,\
				 "ug" : 1.E-9,\
				 "ng" : 1.E-12,\
				 \
				 "km" : 1.E+3,\
				 "m"  : 1.,\
				 "cm" : 1.E-2,\
				 "mm" : 1.E-3,\
				 "um" : 1.E-6,\
				 "nm" : 1.E-9,\
				 \
				 "km2" : 1.E+6,\
				 "m2"  : 1.,\
				 "cm2" : 1.E-4,\
				 "mm2" : 1.E-6,\
				 "um2" : 1.E-12,\
				 "nm2" : 1.E-18,\
				 \
				 "km3" : 1.E+9,\
				 "m3"  : 1.,\
				 "cm3" : 1.E-6,\
				 "mm3" : 1.E-9,\
				 "um3" : 1.E-18,\
				 "nm3" : 1.E-27,\
				 \
				 "pp"  : 1.,\
				 "ppm" : 1.E-6,\
				 "ppb" : 1.E-9,\
				 "ppt" : 1.E-12,\
				 }

	#Time units use seperate dictionary to remove the risk of mixing up m(minute) and m(meter).
	Time_Dict = {"year" : 3.154E+7,\
				 "day"  : 8.64E+4,\
				 "hour" : 3.6E+3,\
				 "min"  : 6.0E+1,\
				 "s"  	: 1.,\
				 "ms"   : 1.E-3,\
				 "us"   : 1.E-6,\
				 "ns"   : 1.E-9\
				 }
	
	a *= (Unit_Dict[mixingR[0]] / Unit_Dict[mixingR[1]])
	a *= (Unit_Dict[length[0]] / Unit_Dict[length[1]])
	a *= (Unit_Dict[weight[0]] / Unit_Dict[weight[1]]) 
	a *= (Unit_Dict[area[0]]   / Unit_Dict[area[1]])
	a *= (Unit_Dict[volume[0]] / Unit_Dict[volume[1]])
	a *= (Time_Dict[time[0]]   / Time_Dict[time[1]])
		
	return a

