
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <matrix_size>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);

    // Dynamic memory allocation for matrices
    double **a = (double **)malloc(n * sizeof(double *));
    double **b = (double **)malloc(n * sizeof(double *));
    double **c = (double **)malloc(n * sizeof(double *));
    
    for (int i = 0; i < n; ++i) {
        a[i] = (double *)malloc(n * sizeof(double));
        b[i] = (double *)malloc(n * sizeof(double));
        c[i] = (double *)malloc(n * sizeof(double));
    }

    // Initialize matrices a and b
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            a[i][j] = (double) rand() / RAND_MAX;
            b[i][j] = (double) rand() / RAND_MAX;
            c[i][j] = 0;
        }
    }

    // Matrix multiplication
    for (int i = 0; i < n; ++i) {
	for (int k = 0; k < n; ++k) {
        	for (int j = 0; j < n; ++j) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Free dynamically allocated memory
    for (int i = 0; i < n; ++i) {
        free(a[i]);
        free(b[i]);
        free(c[i]);
    }
    free(a);
    free(b);
    free(c);

    return 0;
}
