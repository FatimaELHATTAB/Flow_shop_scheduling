'''
Sloving the fllow shop problem using Palmer's_Heurtistic

Author : Oussama Haddad
Vesion : 1.0

'''
import sys


# Read the instance from a File
#
# Return : number_machines , number_jobs , Instance as Array
#
def get_instance(file_name):

	instance = []

	file =  open(file_name,'r')
		
	allfile = file.read().split('\n')
	
	file.close()

	instance_array_line = []
	for line in allfile:

		a = line.split(' ')
		
		for e in a:
			if e != '':
				instance_array_line.append(int(e))

		if len(instance_array_line) != 0:
			instance.append(instance_array_line)
		instance_array_line = []


	return instance[0][0] , instance[0][1] , instance[1::]



# Calculate the slope index of Palmer’s Heuristic (1965)
# return a  dictionary as => { key  : is the number of jub  , value : is the slope index value }
def calculate_slope_index(nb_machine , nb_jobs , instance):

	slope_index = {}

	for i in range(0,nb_jobs):

		Si = 0

		for j in range(0,nb_machine):
			Si += (2*j- nb_machine -1) * instance[j][i]

		
		#print('S{} = {}'.format(i,Si))

		slope_index[i+1] = Si

	return slope_index

# Get Schedule jobs
def get_schedule(slope_index):

	
	result = []
	for key, value in sorted(slope_index.items(), key=lambda item: item[1], reverse=True):
		#result += '{:3},'.format(key)
		result.append(key)
	return result


# Calculate the total job execution makespan using the schedule_jobs list
def total_makespan(instance,nb_machine,nb_jobs,schedule_jobs):

	makeSpans = [ [0 for x in range(nb_jobs)] for y in range(nb_machine) ]

	
	makeSpans[0][0] = instance[0][ schedule_jobs[0] -1 ]

	for j in range(1,nb_machine):
		makeSpans[j][0] = makeSpans[j-1][0] + instance[j][ schedule_jobs[0]-1 ]

	for i in range(1,nb_jobs):
		makeSpans[0][i] = instance[0][ schedule_jobs[i]-1] + makeSpans[0][i-1]
		for j in range(1,nb_machine):
			makeSpans[j][i] = instance[j][ schedule_jobs[i]-1] + max(makeSpans[j-1][i],makeSpans[j][i-1])

	return makeSpans[nb_machine-1][nb_jobs-1]


# the Palmer's_Heurtistic , need the banch file name in a special formate ( see the ReadMe)
def palmers_Heurtistic(banch_file):
	nb_machines , nb_jobs , ins = get_instance(banch_file)
	di = calculate_slope_index(nb_machines , nb_jobs , ins)
	schedule_jobs =  get_schedule(di)

	print(*schedule_jobs, sep=', ',end='')
	print(',',end='')
	print(total_makespan(ins,nb_machines,nb_jobs,schedule_jobs ))


if __name__ == '__main__':
	palmers_Heurtistic(str(sys.argv[1]))
