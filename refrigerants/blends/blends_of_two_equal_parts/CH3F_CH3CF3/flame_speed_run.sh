#!/bin/sh

#SBATCH --nodes=1
#SBATCH --time=7-00:00:00
#SBATCH --job-name=fc_CH3F(1)_CH3CF3(2)
#SBATCH --error=error_fc.slurm.log
#SBATCH --output=output_fc.slurm.log
##SBATCH --cpus-per-task=5
##SBATCH --mem-per-cpu=8Gb
##SBATCH --ntasks=1 
##SBATCH --array=1
#SBATCH --partition=west

source activate cantera_env
python flame_speed_calc.py

