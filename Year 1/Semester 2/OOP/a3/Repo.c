#include "Repo.h"

Country countries[100]; // Definition of the array.

int countryCount = 0;
int undoTop = -1; // Initial value set based on your logic
int redoTop = -1; // Initial value set based on your logic

Operation undoStack[100];
Operation redoStack[100];