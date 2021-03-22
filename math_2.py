import math
class SOP:
	
	def init(self,terms,coefficients,powers):
		self.terms=terms
		self.coefficients=coeffecients
		self.powers=powers
	
	def evaluate(self,values):
		sum1=0
		for i in range(len(self.terms)):
			switch1=type(terms[i])
			swicth2=type(powers[i])
			if(switch1==int or switch1==float):
				if(swicth2==int or switch2==float):
					sum1+=coefficients[i]*math.pow(terms[i],powers[i])
				elif(switch2==str):
					sum1+=coefficients[i]*math.pow(terms[i],values[powers[i]])
				else:
					sum1+=coefficients[i]*math.pow(terms[i],powers[i].evaluate(values))
			elif(switch1==str):
				if(swicth2==int or switch2==float):
					sum1+=coefficients[i]*math.pow(values[terms[i]],powers[i])
				elif(switch2==str):
					sum1+=coefficients[i]*math.pow(values[terms[i]],values[powers[i]])
				else:
					sum1+=coefficients[i]*math.pow(values[terms[i]],powers[i].evaluate(values))
			elif(switch1==int or switch1==float):
				if(swicth2==int or switch2==float):
					sum1+=coefficients[i]*math.pow(terms[i].evaluate(),powers[i])
				elif(switch2==str):
					sum1+=coefficients[i]*math.pow(terms[i].evaluate(),values[powers[i]])
				else:
					sum1+=coefficients[i]*math.pow(terms[i].evaluate(),powers[i].evaluate(values))
		return sum1

class POS:
	
	def init(self,terms,coefficient,powers):
		self.terms=terms
		self.coefficient=coefficient
		self.powers=powers
	
	def evaluate(self,values):
		pro=coefficient
		for i in range(len(self.terms)):
			switch1=type(terms[i])
			swicth2=type(powers[i])
			if(switch1==int or switch1==float):
				if(swicth2==int or switch2==float):
					pro*=math.pow(terms[i],powers[i])
				elif(switch2==str):
					pro*=math.pow(terms[i],values[powers[i]])
				else:
					pro*=math.pow(terms[i],powers[i].evaluate(values))
			elif(switch1==str):
				if(swicth2==int or switch2==float):
					pro*=math.pow(values[terms[i]],powers[i])
				elif(switch2==str):
					pro*=math.pow(values[terms[i]],values[powers[i]])
				else:
					pro*=math.pow(values[terms[i]],powers[i].evaluate(values))
			elif(switch1==int or switch1==float):
				if(swicth2==int or switch2==float):
					pro*=math.pow(terms[i].evaluate(),powers[i])
				elif(switch2==str):
					pro*=math.pow(terms[i].evaluate(),values[powers[i]])
				else:
					pro*=*math.pow(terms[i].evaluate(),powers[i].evaluate(values))
		return pro
