#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

// Function to check if a number is prime
int isPrime(int number) {
    if (number <= 1) return 0;
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) return 0;
    }
    return 1;
}

// Function to print Pascal's Triangle
void printPascalsTriangle(int n) {
    for (int line = 0; line < n; line++) {
        // Print leading spaces for each line to make it appear as an equilateral triangle
        for (int i = 0; i < n - line - 1; i++) {
            printf(" ");
        }

        int value = 1; // The first value in a line is always 1
        for (int k = 0; k <= line; k++) {
            printf("%d ", value);
            value = value * (line - k) / (k + 1);
        }
        printf("\n");
    }
}

// Function to find and print the longest contiguous subsequence of prime numbers
void findLongestPrimeSubsequence(int vector[], int lengthOfVector) {
    int maxLength = 0, start = 0; // For the longest sequence
    int currentLength = 0, currentStart = 0;

    for (int i = 0; i < lengthOfVector; i++) {
        if (isPrime(vector[i])) {
            if (currentLength == 0) currentStart = i; // Start of a new subsequence
            currentLength++;
        }
        else {
            if (currentLength > maxLength) {
                maxLength = currentLength;
                start = currentStart;
            }
            currentLength = 0; // Reset for the next potential subsequence
        }
    }

    // Check at the end in case the longest subsequence is at the end of the vector
    if (currentLength > maxLength) {
        maxLength = currentLength;
        start = currentStart;
    }

    printf("The longest contiguous subsequence of prime numbers is of length %d: ", maxLength);
    for (int i = start; i < start + maxLength; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n");
}

void performOperations() {
    int option, n, lengthOfVector, vector[1000];

    while (1) {
        printf("Menu:\n");
        printf("1. Print Pascal's Triangle.\n");
        printf("2. Find the longest contiguous subsequence of prime numbers.\n");
        printf("3. Exit.\n");
        printf("Choose an option: ");
        scanf("%d", &option);

        switch (option) {
        case 1:
            printf("Enter the dimension (n) for Pascal's Triangle: ");
            scanf("%d", &n);
            printPascalsTriangle(n);
            break;

        case 2:
            printf("Enter the length of the vector: ");
            scanf("%d", &lengthOfVector);
            printf("Enter the elements of the vector: ");
            for (int i = 0; i < lengthOfVector; ++i) {
                scanf("%d", &vector[i]);
            }
            findLongestPrimeSubsequence(vector, lengthOfVector);
            break;

        case 3:
            return; // Exit the program

        default:
            printf("Invalid option. Please try again.\n");
            break;
        }
    }
}

int main() {
    performOperations();
    return 0;
}
