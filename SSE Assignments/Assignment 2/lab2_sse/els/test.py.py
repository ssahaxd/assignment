import os, glob


def get_file_list(file_location):
    files = glob.glob(file_location)
    return files


for file in get_file_list("./els/*"):
	print file 
	cm = f"./cs20s044_CS21Z004_2 $(cat {file})"
	print cm
	os.system(cm)
