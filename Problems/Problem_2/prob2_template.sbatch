#!/bin/bash
# Choose the partition that you are gonna use
# You can choose: parallel_programming_cpu OR debug_5min OR debug OR others 
#SBATCH --partition=parallel_programming_cpu
#SBATCH --exclusive
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=8
#SBATCH --chdir=/home/user007/HW2/Problem_2
#SBATCH --output=/home/user007/HW2/Problem_2/hw2_%J_stdout.txt
#SBATCH --error=/home/user007/HW2/Problem_2/hw2_%J_stderr.txt
# Adjust time according to your needs and queue limit 
#SBATCH --time=00:15:00
#SBATCH --job-name=hw2-p2
#SBATCH --mail-user=youremail@ou.edu
#SBATCH --mail-type=ALL

#################################################

echo "**Test 1 - 1 threads**"
./parallel_mult_mat_mat test1_input_mat_a.csv 100 500 test1_input_mat_b.csv 500 1000 1 output1.csv test1_time_1thr.csv

echo "**Test 1 - 2 threads**"
./parallel_mult_mat_mat test1_input_mat_a.csv 100 500 test1_input_mat_b.csv 500 1000 2 output1.csv test1_time_8thr.csv

# ...