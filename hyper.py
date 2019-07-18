'''
Basic hyper heuristic for flow shop problem , it use different heuristics in heuristic_list 
and choose the best solution , it mean the solution that give slowest Make span

Author : Oussama Haddad
Vesion : 1.0

'''


import sys
import subprocess as sb

heuristic_dictionary = {}

heuristic_list = [

	'neh.exe',
	'NehAmelioree.exe',
	'cds.exe',
	'python Palmer_s_Heurtistic.py',
	#'./VNS'
]



heuristic_output_list =[]

#Get the VNS Result
cmd = 'vns.exe '+sys.argv[1]+' '+ sb.getoutput('python Palmer_s_Heurtistic.py '+ sys.argv[1])
rr = sb.getoutput(cmd ).split(',')
rr.append('VNS')
heuristic_output_list.append(rr)

for heuristic in heuristic_list:
	rr= sb.getoutput(heuristic +' '+sys.argv[1] ).split(',')
	rr.append(heuristic)
	heuristic_output_list.append( rr )
for output in heuristic_output_list:
	gg = output[:-2]
	gg.append(output[-1])

	heuristic_dictionary[ int(output[-2] ) ] = 	gg #heuristic_dictionary[ output[-1]  ] = output[:-1]

min_makeSpan = min(heuristic_dictionary)



print(*heuristic_dictionary[min_makeSpan], sep=', ',end=', ')

print('{}'.format(min_makeSpan))