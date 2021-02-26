import numpy as np
import pandas as pd
import os
import subprocess
import glob

# To use this autograding
# you would need to place your zip file under a "submissions" folder

# Run like this python3 autograding_all.py

target_dir = "./submissions/"

prob_directory = "Problem_2/" 

# Unzipping files

l_zip_files = glob.glob(target_dir+'*.zip')

# Expected name of zip file
# walkerjohn_HW2.zip

for file in l_zip_files:
    print(file)

    # name folders with the name only
    # e.g. walkerjohn
    dir_file_name = file.split('_')[0]
    
    command = "(unzip -o {} -d {})".format(file ,dir_file_name)
    os.system(command)



# Copy Makefile if not there 

l_directories = glob.glob(target_dir+'*/')

dir_make = "./Makefile"
for dir in l_directories:
    dir_prob1 = dir + "Problem_2/"
    if not os.path.isfile(dir_prob1+"Makefile"):
        command = "(cp {} {})".format(dir_make, dir_prob1)
        os.system(command)

# run make

dir_make = "./Makefile"
for dir in l_directories:
    print(dir)
    dir_prob1 = dir + "Problem_2/"
    command = "(cd {} && make)".format(dir_prob1)
    os.system(command)

# Run the test cases
# serial_mult_mat_vec file_1.csv n_row_1 n_col_1 file_2.csv n_row_2 outputfile.csv

dir_test_prob1 = "./test_data/Problem_2/"

l_test = [["test1_input_mat_a.csv", 100, 500, "test1_input_mat_b.csv", 500, 1000, 1, "test1_1thr_results.csv", "test1_1thr_time.csv"],
          ["test1_input_mat_a.csv", 100, 500, "test1_input_mat_b.csv", 500, 1000, 2, "test1_2thr_results.csv", "test1_2thr_time.csv"],
          ["test1_input_mat_a.csv", 100, 500, "test1_input_mat_b.csv", 500, 1000, 4, "test1_4thr_results.csv", "test1_4thr_time.csv"],
          ["test1_input_mat_a.csv", 100, 500, "test1_input_mat_b.csv", 500, 1000, 8, "test1_8thr_results.csv", "test1_8thr_time.csv"],
          ["test2_input_mat_a.csv", 1000, 800, "test2_input_mat_b.csv", 800, 2000, 1, "test2_1thr_results.csv", "test2_1thr_time.csv"],
          ["test2_input_mat_a.csv", 1000, 800, "test2_input_mat_b.csv", 800, 2000, 2, "test2_2thr_results.csv", "test2_2thr_time.csv"],
          ["test2_input_mat_a.csv", 1000, 800, "test2_input_mat_b.csv", 800, 2000, 4, "test2_4thr_results.csv", "test2_4thr_time.csv"],
          ["test2_input_mat_a.csv", 1000, 800, "test2_input_mat_b.csv", 800, 2000, 8, "test2_8thr_results.csv", "test2_8thr_time.csv"],
          ["test3_input_mat_a.csv", 2000, 1000, "test3_input_mat_b.csv", 1000, 3000, 1, "test3_1thr_results.csv", "test3_1thr_time.csv"],
          ["test3_input_mat_a.csv", 2000, 1000, "test3_input_mat_b.csv", 1000, 3000, 2, "test3_2thr_results.csv", "test3_2thr_time.csv"],
          ["test3_input_mat_a.csv", 2000, 1000, "test3_input_mat_b.csv", 1000, 3000, 4, "test3_4thr_results.csv", "test3_4thr_time.csv"],
          ["test3_input_mat_a.csv", 2000, 1000, "test3_input_mat_b.csv", 1000, 3000, 8, "test3_8thr_results.csv", "test3_8thr_time.csv"],
          ["test4_input_mat_a.csv", 4000, 2000, "test4_input_mat_b.csv", 2000, 5000, 1, "test4_1thr_results.csv", "test4_1thr_time.csv"],
          ["test4_input_mat_a.csv", 4000, 2000, "test4_input_mat_b.csv", 2000, 5000, 2, "test4_2thr_results.csv", "test4_2thr_time.csv"],
          ["test4_input_mat_a.csv", 4000, 2000, "test4_input_mat_b.csv", 2000, 5000, 4, "test4_4thr_results.csv", "test4_4thr_time.csv"],
          ["test4_input_mat_a.csv", 4000, 2000, "test4_input_mat_b.csv", 2000, 5000, 8, "test4_8thr_results.csv", "test4_8thr_time.csv"] ]

for dir in l_directories:
    for i in range(len(l_test)):
    # for i in range(8):

        print(dir)
        dir_exe = dir + "Problem_2/parallel_mult_mat_mat"
        dir_output = dir + "Problem_2/"
        print(dir_exe)
        print("-------------------------------")
        command = "({} {} {} {} {} {} {} {} {} {})".format(dir_exe, dir_test_prob1 + l_test[i][0], l_test[i][1], l_test[i][2],
                                                             dir_test_prob1 + l_test[i][3],l_test[i][4],l_test[i][5], l_test[i][6],
                                                             dir_output + l_test[i][7], dir_output + l_test[i][8] )
        print(command)
        os.system(command)

# print(l_directories)

l_student_names = [dir.split('/')[2] for dir in l_directories]
# # print(l_student_names)

l_col_names = ["P2-T1","P2-T2","P2-T3","P2-T4","P3-T1","P3-T2","P3-T3","P3-T4","P4-T1"]

df_grades = pd.DataFrame(np.nan, index=[i for i in l_student_names],
                     columns=[i for i in l_col_names])

l_col_time_names = ["P2-T1-th1","P2-T1-th2","P2-T1-th4","P2-T1-th8",
                    "P2-T2-th1","P2-T2-th2","P2-T2-th4","P2-T2-th8",
                    "P2-T3-th1","P2-T3-th2","P2-T3-th4","P2-T3-th8",
                    "P2-T4-th1","P2-T4-th2","P2-T4-th4","P2-T4-th8",
                    "P3-T1-th1","P3-T1-th2","P3-T1-th4","P3-T1-th8",
                    "P3-T2-th1","P3-T2-th2","P3-T2-th4","P3-T2-th8",
                    "P3-T3-th1","P3-T3-th2","P3-T3-th4","P3-T3-th8",
                    "P3-T4-th1","P3-T4-th2","P3-T4-th4","P3-T4-th8"]

df_time = pd.DataFrame(np.nan, index=[i for i in l_student_names],
                     columns=[i for i in l_col_time_names])

# # print(df_grades)

l_files_benchmark = [ "test1_output_mat.csv",
                      "test2_output_mat.csv",
                      "test3_output_mat.csv",
                      "test4_output_mat.csv"]

# l_files_benchmark = [ "test1_output_mat.csv",
#                       "test2_output_mat.csv"]

l_files_results = [ "test1_1thr_results.csv",
                    "test2_1thr_results.csv",
                    "test3_1thr_results.csv",
                    "test4_1thr_results.csv"]

# l_files_results = [ "test1_1thr_results.csv",
#                     "test2_1thr_results.csv"]

l_files_time = [ "test1_1thr_time.csv", "test1_2thr_time.csv",
                 "test1_4thr_time.csv", "test1_8thr_time.csv",
                 "test2_1thr_time.csv", "test2_2thr_time.csv",
                 "test2_4thr_time.csv", "test2_8thr_time.csv",
                 "test3_1thr_time.csv", "test3_2thr_time.csv",
                 "test3_4thr_time.csv", "test3_8thr_time.csv",
                 "test4_1thr_time.csv", "test4_2thr_time.csv",
                 "test4_4thr_time.csv", "test4_8thr_time.csv"]

# l_files_time = [ "test1_1thr_time.csv", "test1_2thr_time.csv",
#                  "test1_4thr_time.csv", "test1_8thr_time.csv",
#                  "test2_1thr_time.csv", "test2_2thr_time.csv",
#                  "test2_4thr_time.csv", "test2_8thr_time.csv"]

for dir in l_directories:
    name_student = dir.split('/')[2]
    for i in range(len(l_files_benchmark)):

        # Comparing output files
        # print(dir)
        dir_prob1 = dir + "Problem_2/"
        # print("-------------------------------")
        results_benchmark_test_temp = np.genfromtxt("./" + dir_test_prob1 + l_files_benchmark[i], delimiter=',')
        results_test_temp = np.genfromtxt( dir_prob1 + l_files_results[i],  delimiter=',')

        if ( len(results_benchmark_test_temp) != len(results_test_temp) ):
            # print("Student:", name_student,"Test", (i+1),"Different size")
            df_grades.loc[name_student, l_col_names[i] ] = 0
            continue

        diff_temp = np.sum( np.absolute ( (results_benchmark_test_temp - results_test_temp)/results_benchmark_test_temp ) )
        # by unit 
        diff_temp = diff_temp/np.ravel(results_benchmark_test_temp).shape[0]

        # print(diff_temp)
        if diff_temp < 0.05:
            # print("Test", (i+1), "Succeeded")
            df_grades.loc[name_student, l_col_names[i] ] = 1
        else:
            # print("Test", (i+1), "Failed")
            df_grades.loc[name_student, l_col_names[i] ] = 0

    for i in range(len(l_files_time)):
        # Storing time
        time_temp = np.genfromtxt(dir_prob1 + l_files_time[i], delimiter=',')
        df_time.loc[name_student, l_col_time_names[i] ] = time_temp

l_files_benchmark2 = ["test1_text_output.txt",
                      "test2_text_output.txt",
                      "test3_text_output.txt",
                      "test4_text_output.txt"]

l_test2 = [[10, "test1_text_input.txt", 1, "test1_encrypted_1thr_result.txt","test1_text_1thr_time.txt"],
           [10, "test1_text_input.txt", 2, "test1_encrypted_2thr_result.txt","test1_text_2thr_time.txt"],
           [10, "test1_text_input.txt", 4, "test1_encrypted_4thr_result.txt","test1_text_4thr_time.txt"],
           [10, "test1_text_input.txt", 8, "test1_encrypted_8thr_result.txt","test1_text_8thr_time.txt"], 
           [10, "test2_text_input.txt", 1, "test2_encrypted_1thr_result.txt","test2_text_1thr_time.txt"],
           [10, "test2_text_input.txt", 2, "test2_encrypted_2thr_result.txt","test2_text_2thr_time.txt"],
           [10, "test2_text_input.txt", 4, "test2_encrypted_4thr_result.txt","test2_text_4thr_time.txt"],
           [10, "test2_text_input.txt", 8, "test2_encrypted_8thr_result.txt","test2_text_8thr_time.txt"],
           [10, "test3_text_input.txt", 1, "test3_encrypted_1thr_result.txt","test3_text_1thr_time.txt"],
           [10, "test3_text_input.txt", 2, "test3_encrypted_2thr_result.txt","test3_text_2thr_time.txt"],
           [10, "test3_text_input.txt", 4, "test3_encrypted_4thr_result.txt","test3_text_4thr_time.txt"],
           [10, "test3_text_input.txt", 8, "test3_encrypted_8thr_result.txt","test3_text_8thr_time.txt"],
           [10, "test4_text_input.txt", 1, "test4_encrypted_1thr_result.txt","test4_text_1thr_time.txt"],
           [10, "test4_text_input.txt", 2, "test4_encrypted_2thr_result.txt","test4_text_2thr_time.txt"],
           [10, "test4_text_input.txt", 4, "test4_encrypted_4thr_result.txt","test4_text_4thr_time.txt"],
           [10, "test4_text_input.txt", 8, "test4_encrypted_8thr_result.txt","test4_text_8thr_time.txt"]]

l_files_results2 = [ "test1_encrypted_1thr_result.txt",
                     "test2_encrypted_1thr_result.txt",
                     "test3_encrypted_1thr_result.txt",
                     "test4_encrypted_1thr_result.txt"]

l_files_time2 = [ "test1_text_1thr_time.txt", "test1_text_2thr_time.txt",
                  "test1_text_4thr_time.txt", "test1_text_8thr_time.txt",
                  "test2_text_1thr_time.txt", "test2_text_2thr_time.txt",
                  "test2_text_4thr_time.txt", "test2_text_8thr_time.txt",
                  "test3_text_1thr_time.txt", "test3_text_2thr_time.txt",
                  "test3_text_4thr_time.txt", "test3_text_8thr_time.txt",
                  "test4_text_1thr_time.txt", "test4_text_2thr_time.txt",
                  "test4_text_4thr_time.txt", "test4_text_8thr_time.txt"]

dir_test_prob3 = "./test_data/Problem_3/"
# run make

dir_make = "./Makefile"
for dir in l_directories:
    print(dir)
    dir_prob3 = dir + "Problem_3/"
    command = "(cd {} && make)".format(dir_prob3)
    os.system(command)

for dir in l_directories: 
    for i in range(len(l_test2)):
    # for i in range(8):

        print(dir)
        dir_exe = dir + "Problem_3/encrypt_parallel"
        dir_output = dir + "Problem_3/"
        print(dir_exe)
        print("-------------------------------")
        command = "({} {} {} {} {} {})".format(dir_exe, l_test2[i][0],  dir_test_prob3 + l_test2[i][1], l_test2[i][2],
                                                dir_output + l_test2[i][3], dir_output + l_test2[i][4] )
        print(command)
        os.system(command)

for dir in l_directories:
    name_student = dir.split('/')[2]
    for i in range(len(l_files_benchmark2)):

        # Comparing output files
        # print(dir)
        dir_prob3 = dir + "Problem_3/"
        # print("-------------------------------")

        with open("./" + dir_test_prob3 + l_files_benchmark2[i], 'rb') as f1:
            with open( dir_prob3 + l_files_results2[i], 'rb') as f2:
                if f1.read() == f2.read():
                    df_grades.loc[name_student, l_col_names[i+4] ] = 1
                else:
                    df_grades.loc[name_student, l_col_names[i+4] ] = 0

    for i in range(len(l_files_time2)):
        # Storing time
        time_temp = np.genfromtxt(dir_prob3 + l_files_time2[i], delimiter=',')
        df_time.loc[name_student, l_col_time_names[i+16] ] = time_temp

l_benchmark3 = [25]

l_test3 = [["test1_text_to_decrypt_input.txt", 1, "key1.txt"]]

l_files_results3 = [ "key1.txt"]

dir_test_prob4 = "./test_data/Problem_4/"
# run make

dir_make = "./Makefile"
for dir in l_directories:
    print(dir)
    dir_prob4 = dir + "Problem_4/"
    if os.path.isdir(dir_prob4):
        command = "(cd {} && make)".format(dir_prob4)
        os.system(command)

for dir in l_directories:


    dir_prob4 = dir + "Problem_4/"
    if os.path.isdir(dir_prob4):

        for i in range(len(l_test3)):
        # for i in range(8):

            print(dir)
            dir_exe = dir + "Problem_4/decrypt_parallel"
            
            print(dir_exe)
            print("-------------------------------")
            command = "({} {} {} {})".format(dir_exe, dir_test_prob4 + l_test3[i][0], l_test3[i][1],
                                            dir_prob4 +  l_test3[i][2] )
            print(command)
            os.system(command)


        name_student = dir.split('/')[2]
        for i in range(len(l_benchmark3)):

            # Comparing output files
            # print(dir)
            dir_prob3 = dir + "Problem_4/"
            # print("-------------------------------")

            key_temp = np.genfromtxt(dir_prob3 + l_files_results3[i], delimiter=',')

            if( key_temp == l_benchmark3[0] ):
                print("The same")
                df_grades.loc[name_student, l_col_names[i+8] ] = 1
            else:
                print("Different")
                df_grades.loc[name_student, l_col_names[i+8] ] = 0

print(df_grades)
df_grades.to_csv("grades.csv")
# print(df_time)
df_time.to_csv("time.csv")