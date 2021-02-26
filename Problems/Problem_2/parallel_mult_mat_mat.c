#include <stdio.h>
#include <stdlib.h> // for strtol
#include <string.h>
#include <omp.h>


int main (int argc, char *argv[])
{
    if( argc != 10)
    {
        printf("USE LIKE THIS: parallel_mult_mat_mat file_1.csv n_row_1 n_col_1 file_2.csv n_row_2 n_col_2 num_threads results_matrix.csv time.csv\n");
        return EXIT_FAILURE;
    }

    FILE *inputFile1;
    FILE *inputFile2;

    char* p1;
    char* p2;

    inputFile1 = fopen(argv[1], "r");

    int n_row1 = strtol(argv[2], &p1, 10 );
    int n_col1 = strtol(argv[3], &p2, 10 );
    
    inputFile2 = fopen(argv[4], "r");

    int n_row2 = strtol(argv[5], &p1, 10 );
    int n_col2 = strtol(argv[6], &p2, 10 );

    int     thread_count;
    thread_count = strtol(argv[7], NULL, 10);
    // printf("thread_count = %d\n", thread_count);

    FILE *outputFile;
    outputFile = fopen(argv[8], "w");

    FILE *outputTime;
    outputTime = fopen(argv[9], "w");

    // Code for allocation of Matrix
    // This reference may be useful
	// We suggest using data type double
    // https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/

    // TODO: Code for processing csv files

    // As stated in Section 2.6.4 from "An Introduction to Parallel" Programming by Pacheco
    // We are interesting in timing the multiplication process

    // Start timing
    double start = omp_get_wtime();
    
    // TODO Parallelize the calculation of multiplication
        
    double end = omp_get_wtime();
    
    // Time calculation (in seconds)

    double time_passed = end - start;

    // save time to file
    fprintf(outputTime, "%f", time_passed);

    // TODO save result matrix to csv file

    fclose (inputFile1);
    fclose (inputFile2);
    fclose (outputFile);
    fclose (outputTime);

    return 0;
}

