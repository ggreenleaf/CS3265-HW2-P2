from collections import OrderedDict

def parse_vars(filename):

	variables = OrderedDict()
	with open(filename) as f:
		data = f.read()
	
	data = data.split("\n") #split vars by new line
	for line in data:
		key,val = line.split(": ") #split var and var domain
		val = val.split(" ") #splits domain into list of possible values
		variables[key] = [val,0] #list of domain and index of current assignment
		
	return variables

def parse_cons(filename):
	with open(filename) as f:
		data = f.read()

	data = [x.replace(" ","") for x in data.split("\n")]
	return data


class cspsolver:
	def __init__(self,var_fname, con_fname):
		self.variables = parse_vars(var_fname) #dictionary of lists key is var and val is domain list 
		self.cons = parse_cons(con_fname) #string of equations used to evaluate 
			
	def display_assignments(self):
		for key in self.variables.keys():
			assignment_index = self.variables[key][-1]
			print key, self.variables[key][0][assignment_index]
	
	def eval_constraints(self):
		for con in self.cons:
			key1 = con[0] #all variables are singal
			op = con[1]
			key2 = con[2]
			
			var1 = self.variables[key1][0][self.variables[key1][-1]]
			var2 = self.variables[key2][0][self.variables[key2][-1]]
			if not eval(var1+op+var2):
				return False #constraints failed

if __name__ == "__main__":
	solver = cspsolver("ex2.var","ex2.con")
