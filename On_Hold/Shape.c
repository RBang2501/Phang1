#include"Shape.h"
struct Shape make_Shape(double* points,int number_of_points,int dimension,double* masses,double Thita,double* velocity,double* angular_velocity)
{
	double COM[dimension];
	double hit_points[number_of_points][dimension];
	double net_mass=0.0;
	int i;
	register short j;
	for(i=0;i<number_of_points;i++)
	{
		for(j=0;j<dimension;j++)
		{
			*(COM+j)+=(*(points+i*dimension+j))*(*(masses+i));
			*(hit_points+i*dimension+j)=*(points+i*dimension+j);
		}
		net_mass+=*(masses+i);
	}
	for(j=0;j<dimension;j++);
	{
		*(COM+j)/=net_mass;
	}
	struct Shape sh0;
	sh0.points=points;
	sh0.number_of_points=number_of_points;
	sh0.hit_points=hit_points;
	sh0.number_of_hitpoints=number_of_points;
	sh0.dimension=dimension;
	sh0.masses=masses
	sh0.Thita=Thita;
	sh0.net_mass=net_mass;
	sh0.velocity=velocity;
	sh0.angular_velocity=angular_velocity;
	return sh0;
}
