
import csv

vns_file = csv.DictReader(open("best_parameters.csv"))
ag_file = csv.DictReader(open("fatima.csv"))
best_algorithme = ''
best_solution = 0
name = '9550.txt'
for row in vns_file:
 if name+' ' == row['instance']:
  seq = row['seq']
  x = seq.split(',')
  res_vns = int(x[-1])
  vns_all = row
  print(res_vns) 
  
for row in ag_file:
 if name == row['probleme']:
  res_ag = int(row['makespan'])
  ag_all = row
  print(res_ag) 
  
if res_ag < res_vns:
 best_algorithme = 'AG'
 best_solution = res_ag
 best_parameters = ag_all
else:
 best_algorithme = 'VNS' 
 best_solution = res_vns
 best_parameters = vns_all

print(best_algorithme,best_solution,best_parameters) 
