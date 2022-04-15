#!/bin/sh

#SBATCH --nodes=1
##SBATCH --time=unlimited
#SBATCH --time=7:00:00
#SBATCH --job-name=fc_{CH2FCHF2}
#SBATCH --error=fc.slurm.log
#SBATCH --output=fc_output.slurm.log
##SBATCH --cpus-per-task=5
##SBATCH --mem-per-cpu=8Gb
##SBATCH --ntasks=1 
##SBATCH --array=1
##SBATCH --partition=west
#SBATCH --partition=short

source activate cantera_env
python flame_speed_calc.py
