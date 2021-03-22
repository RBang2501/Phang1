#include<stdio.h>
#include<math.h>
struct Shape()
{
	double* points;
	int number_of_points;
	double* hitpoints;
	int number_of_hitpoints;
	int dimension;
	double* masses;
	double Thita;
	double* COM;
	double net_mass;
	double* velocity;
	double* angular_velocity;
};
struct Shape make_Shape(double* points,int number_of_points,int dimension,double* masses,double Thita,double* velocity,double* angular_velocity);
