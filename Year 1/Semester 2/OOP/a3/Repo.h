#pragma once

typedef struct {
    char name[50];
    char continent[20];
    float population;
} Country;

extern Country countries[100];

extern int countryCount;

typedef enum {
    ADD_COUNTRY,
    DELETE_COUNTRY,
    UPDATE_COUNTRY
} OperationType;

// Define a structure to store an operation
typedef struct {
    OperationType type;
    Country country;
    float prevPopulation;
    char prevName[50];
} Operation;

// Define stacks for undo and redo
extern Operation undoStack[100];
extern int undoTop;
extern Operation redoStack[100];
extern int redoTop;