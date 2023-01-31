
import cantera as ct
import numpy as np
import pandas as pd
import os 
import re
from subprocess import getoutput
import sys
import csv


print("Running Cantera Version: " + str(ct.__version__))

############################## specify the files that you'd like to convert ####################################
selected_files = ['chem0120.inp',
 'chem0121.inp',
 'chem0122.inp',
 'chem0123.inp',
 'chem0124.inp',
 'chem0125.inp',
 'chem0126.inp',
 'chem0127.inp',
 'chem0128.inp',
 'chem0129.inp',
 'chem0130.inp',
 'chem0131.inp',
 'chem0132.inp',
 'chem0133.inp',
 'chem0134.inp',
 'chem0135.inp',
 'chem0136.inp',
 'chem0137.inp',
 'chem0138.inp',
 'chem0139.inp',
 'chem0140.inp']


############### copies chemkin files to dups folder #############################

for file in selected_files: 
    
    match = re.search('chem([0-9]+).inp', file)
    
    directory ='.'


    #os.system('source activate ct_env') #if on local, this is cantera 2.6 beta
    os.system('source activate cantera_env') #if on discovery, will be cantera 2.5


    #copy folders so i dont screw up the original, and change into the new directory with copies
    os.makedirs('copies', exist_ok=True)

    #copy chem.inp file into dups folder, and will then convert this copy into .cti
    os.command = f'scp {file} copies/copy_{file}'
    os.system(os.command)
    os.system('scp tran.dat copies/tran.dat')

    #now look in the dups folder
    os.chdir('./copies')









    ############################# converts the dup_chem.inp files to .cti files #############################

    x = 0
    while x == 0: 
    #this is a string of the output when I try to convert this file to a cti file. Will probably produce an error
        output = getoutput( f'ck2cti --input=copy_{file} --transport=tran.dat') 
        #if command passed without an error
        if re.search('PASSED',output):
            print('**************************command passed, converting to cti***************************')
            x += 1 
        #if command generated the Duplicate error
        else:
            print('*******************************needs some work****************************************')
            if re.search('Encountered\sunmarked\sduplicate\sreaction',output):
                match = re.search('See\slines\s([0-9]+)\sand\s([0-9]+)\sof\sthe\sinput\sfile',output)
                #capture the line numbers with the duplicate reactions
                line_numbers = [int(match.group(1)), int(match.group(2))]
                print(f'Unmarked duplicates on lines {match.group(1)} and {match.group(2)}')
                print('Editing chemkin file to allow conversion to .cti')
                #write the lines of the chemkin input file to a list so that I can insert the "DUPLICATE" statement
                with open(f'copy_{file}','r') as f:
                    data = f.readlines()
                    print(data[line_numbers[0]-1], data[line_numbers[1]-1])

                #start editing the .inp file below

                #'adjustments' will make sure that, even when I add an element in 'data', my index will still be correct
                adjustments = [0,1]
                for i,adjust in zip(line_numbers,adjustments): 
                    start = i+adjust-1
                    count = 0 
                    while count == 0: 
                        #if you don't see a blank line after the duplicated reaction line, keep going until you do
                        if not re.search('^\n', data[start]): 
                            print('no match')
                            print(start)
                            print(data[start])
                            start += 1
                        #when we get to the blank line after the reaction block, insert "DUPLICATE" and stop the loop for this line number
                        else: 
                            print('there is a match')
                            data.insert(start,'DUPLICATE')
                            count = 1 
                #now overwrite the input file with the change 
                with open(f'copy_{file}','w+') as f: 
                    for l in data: 
                        f.write(l)
                        x==0

            #if the command generated an error that is not the Duplicate error
            else:
                #if code ever gets to here, just cry
                print('There is another error, see Output')
                print(output)
                x += 1
                
    os.chdir('../')



