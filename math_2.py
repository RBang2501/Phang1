import math
class term:
	
	def init(self,variable_ids,coefficient,powers):
		self.variable_ids=variable_ids
		self.coefficient=coefficient
		self.powers=powers
	
	def evaluate_term(self,values):
		pro=self.coefficient
		for i in range(len(self.variable_ids)):
			pro*=math.pow(values[variable_ids[i]],evaluate_term(powers[i]) if type(powers[i])==term else powers[i])
		return pro
		
class equation:

	def init(self,terms):
		self.terms=terms
	
	def evaluate_equation(self,values):
		sum=0
		for i in self.terms:
			sum+=i.evaluate_term(values)
		return sum
