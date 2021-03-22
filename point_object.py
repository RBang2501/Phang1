class point_object:
	default_mass=1
	default_x=0
	default_y=0
	default_speedx=0
	default_speedy=0
	
	def init(self,position=[default_x,default_y],velocity=[default_speedx,default_speedy],mass=default_mass):
		error=0
		if(not type(position)==list):
			error=1;
		elif(not type(velocity)==list):
			error=2;
		elif(not (type(mass)==int or type(mass)==float)):
			error=3;
		elif(not len(position)==len(position)):
			error=4;
		else:
			for i range(len(position)):
				if(type(position[i])==int or type(position[i])==float):
					error=5;
					break;
				if(type(velocity[i])==int or type(velocity[i])==float):
					error=6;
					break;
		if(error==1):
			raise "Position has to be a list of coordinates"
		if(error==2):
			raise "Velocity has to be a list of velocities along axii"
		if(error==3):
			raise "Mass has to be a number"
		if(error==4):
			raise "Dimension of position and velocity has to be same"
		if(error==5):
			raise "A coordinate has to be a number"
		if(error==6):
			raise "Velocity has to be a number"
		self.position=position
		self.velocity=velocity
		self.mass=mass
