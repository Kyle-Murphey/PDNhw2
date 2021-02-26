#!/bin/bash
# Choose the partition that you are gonna use
# You can choose: parallel_programming_cpu OR debug_5min OR debug OR others 
#SBATCH --partition=parallel_programming_cpu
#SBATCH --exclusive
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=8
#SBATCH --chdir=/home/user007/HW2/
#SBATCH --output=/home/user007/HW2/autograding_%J_stdout.txt
#SBATCH --error=/home/user007/HW2/autograding_%J_stderr.txt
#SBATCH --time=00:15:00
#SBATCH --job-name=auto
#SBATCH --mail-user=youremail@ou.edu
#SBATCH --mail-type=ALL

#################################################

module purge

module load GCC
module load Python/3.8.2-GCCcore-9.3.0

python3 -u autograding_all.py