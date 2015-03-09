from collections import defaultdict

def parse_vars(filename):

	variables = defaultdict()
	with open(filename) as f:
		data = f.read()
	
	data = data.split("\n") #split vars by new line
	for line in data:
		line = line.split(": ")
		variables[line[0]] = line[1].split(" ")

	return variables

def parse_cons(filename):

	with open(filename) as f:
		data = f.read()
	
	return data.split("\n")


class cspsolver:
	def __init__(self,var_fname, con_fname):
			self.vars = parse_vars(var_fname) #dictionary of lists key is var and val is domain list 
			self.cons = parse_cons(con_fname) #string of equations used to evaluate 


if __name__ == "__main__":
	solver = cspsolver("ex2.var","ex2.con")
