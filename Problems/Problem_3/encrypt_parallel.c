#include <stdio.h>
#include <stdlib.h> // for strtol
#include <string.h>
#include <omp.h>

int main (int argc, char *argv[])
{
    if( argc != 6)
    {
        printf("USE LIKE THIS: encrypt_parallel key input_text.txt num_threads output_text.txt time.txt\n");
        return EXIT_FAILURE;
    }

    char* p1;

    int key = strtol(argv[1], &p1, 10 );

    FILE *inputFile1;

    inputFile1 = fopen(argv[2], "r");

    int     thread_count;
    thread_count = strtol(argv[3], NULL, 10);

    printf("thread_count = %d\n", thread_count);

    FILE *outputFile;
    outputFile = fopen(argv[4], "w");

    FILE *outputTime;
    outputTime = fopen(argv[5], "w");

    // You can use the following lines of code
    // to store the text as a char array

    long lSize;
    unsigned char *buffer;

    /* Seek to the end of the file */
    fseek( inputFile1 , 0L , SEEK_END);
    lSize = ftell( inputFile1 );
    // printf("length file=%ld\n", lSize);
    rewind( inputFile1 );

    /* allocate memory for entire content */
    buffer = calloc( 1, lSize+1 );
    if( !buffer ) fclose(inputFile1),fputs("memory alloc fails",stderr),exit(1);

    /* copy the file into the buffer */
    if( 1!=fread( buffer , lSize, 1 , inputFile1) )
        fclose(inputFile1),free(buffer),fputs("entire read fails",stderr),exit(1);


    // Begin timing
    double start = omp_get_wtime();

    // TODO Parallel Encryption

    //End timing
    double end = omp_get_wtime();
    
    // Time calculation (in seconds)
    double time_passed = end - start;
    
    fprintf(outputTime, "%f", time_passed);

    // TODO Save encrypted file

    fclose (outputFile);
    fclose (outputTime);

    return 0;
}

// Read input
