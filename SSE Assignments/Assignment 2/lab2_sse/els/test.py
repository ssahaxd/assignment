import os, glob
from pwn import *


def get_file_list(file_location):
    files = glob.glob(file_location)
    return files


for file in get_file_list("/media/sf_Assignment_2/lab2_sse/els/*"):
    print(file)
    cm = "/media/sf_Assignment_2/lab2_sse/cs20s044_CS21Z004_2 $(cat "+file+")"
    io = process(cm,shell=True)
    b = io.recvline()
    print(b)
 







