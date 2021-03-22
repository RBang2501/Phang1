class equation:
		def init(self,coefficients,value):
			self.coefficients=coefficients
			self.value=value

def find_solutions(equations):#Required to find equation of the n-1 dimensional body(line,plane...) that contains n points needed for integration
	if(len(equations)==1):#If there is only one equation then the only variable can be calculated
		return [equations[0].value/equations[0].coefficients[0]]
	else:#Using substitution method to solve multiple variables in recursion
		coefficients=[[equations[i].coefficients[j]-equations[0].coefficients[j]*equations[i].coefficients[0]/coefficients[0].equations[0] for j in range(1,len(equations[0].coefficients))] for i in range(1,len(equations))]
		value=[equations[i].value-equations[0].value*equations[i].coefficients[0]/equations[0].coefficients[0] for i in range(1,len(equations))]
		solutions=find_solutions([equation(coefficients[i],value[i]) for i in range(len(equations)-1)])
		a0=equations[0].value
		for i in range(1,len(equations[0].coefficients)):
			a0-=coefficients[i]*equations[0].coefficients[i]
		a0/=equations[0].coefficients[0]
		return a0+solutions
