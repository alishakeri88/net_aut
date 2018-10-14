#updated on 10-14-2018
import os

def print_dict(path, ind):
	indent =  '\t' * int(ind)
	for child in os.listdir(path):
		child_path = os.path.join(path, child)
		if os.path.isdir(child_path):
			print_dict(child_path, ind + 1)
		else:
			print indent + "+" + child_path

print_dict('/home/ali/Desktop', 0)
