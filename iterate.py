#This is a script that uses itertools in python to make a combinatorial matrix with all possible combinations of give values of variables.

import itertools
   
Variable1=[100,95,90,]
Variable2=[100,95,90,]
Variable3=[100,95,90,]
Variable4=[100,95,90,]
Variable5=[100,95,90,]


    
import sys
filename  = open("outputfile_nolessthan50",'w')
sys.stdout = filename
for combination in itertools.product(Variable1, Variable2, Variable3, Variable4, Variable5):
    print combination