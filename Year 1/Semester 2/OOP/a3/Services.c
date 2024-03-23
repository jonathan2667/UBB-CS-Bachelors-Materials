#include "Services.h"
#include "Repo.h"


// Function to add or update a country
void addCountry(const char* name, const char* continent, float population) {
    int index = -1;
    printf("%f\n", population); // Correct format specifier for float

    // Check if the country already exists
    for (int i = 0; i < countryCount; ++i) {
        if (strcmp(countries[i].name, name) == 0) {
            index = i;
            break;
        }
    }

    if (index == -1) { // Country doesn't exist, add a new one
        if (countryCount < 50) {
            Country newCountry;
            strcpy(newCountry.name, name);
            strcpy(newCountry.continent, continent);
            newCountry.population = population;

            countries[countryCount++] = newCountry;
            printf("Country added successfully.\n");

            Operation op;
            op.type = ADD_COUNTRY;
            strcpy(op.country.name, name);
            strcpy(op.country.continent, continent);
            op.country.population = population;
            pushUndo(op);
        }
        else {
            printf("Maximum number of countries reached.\n");
        }
    }
    else { // Country exists, update it
        countries[index].population = population;
        printf("Country population updated successfully.\n");
    }
}

// Function to delete a country
void deleteCountry(const char* name) {
    int index = -1;

    // Find the index of the country
    for (int i = 0; i < countryCount; ++i) {
        if (strcmp(countries[i].name, name) == 0) {
            index = i;
            break;
        }
    }

    if (index != -1) { // Country found, delete it
        for (int i = index; i < countryCount - 1; ++i) {
            countries[i] = countries[i + 1];
        }
        countryCount--;
        printf("Country deleted successfully.\n");

        Operation op;
        op.type = DELETE_COUNTRY;
        strcpy(op.country.name, countries[index].name);
        strcpy(op.country.continent, countries[index].continent);
        op.country.population = countries[index].population;
        pushUndo(op);
    }
    else {
        printf("Country not found.\n");
    }
}

// Function to update a country, considering migration
void updateCountry(const char* name, const char* migrationTo, float migrationPopulation) {
    int indexMigrationFrom = -1;
    int indexMigrationTo = -1;

    // Find the index of the country frome where people leave
    for (int i = 0; i < countryCount; ++i) {
        if (strcmp(countries[i].name, name) == 0) {
            indexMigrationFrom = i;
            break;
        }
    }

    // Find the index of the country frome where people migrate
    for (int i = 0; i < countryCount; ++i) {
        if (strcmp(countries[i].name, migrationTo) == 0) {
            indexMigrationTo = i;
            break;
        }
    }

    if (indexMigrationFrom != -1 && indexMigrationTo != -1) { // Country found, update it
        // Check if migration is specified
        if (strlen(migrationTo) > 0) {
            // Decrease population in the current country due to migration
            countries[indexMigrationFrom].population -= migrationPopulation;

            // Increase population in the specified country due to migration
            countries[indexMigrationTo].population += migrationPopulation;
        }
        Operation op;
        op.type = UPDATE_COUNTRY;
        strcpy(op.country.name, countries[indexMigrationFrom].name);
        strcpy(op.country.continent, countries[indexMigrationFrom].continent);
        op.country.population = countries[indexMigrationFrom].population;
        strcpy(op.prevName, migrationTo);
        op.prevPopulation = migrationPopulation;
        pushUndo(op);

        printf("Country information updated successfully.\n");
    }
    else {
        printf("Country not found.\n");
    }
}



/*REDO UNDO*/


void undo() {
    if (undoTop == -1) {
        printf("No operations to undo.\n");
        return;
    }

    // Pop the last operation from the undo stack
    Operation op = undoStack[undoTop--];

    // Perform undo based on the operation type
    switch (op.type) {
    case ADD_COUNTRY:
        // To undo an add, we delete the country
        deleteCountry(op.country.name);
        break;
    case DELETE_COUNTRY:
        // To undo a delete, we re-add the country
        addCountry(op.country.name, op.country.continent, op.country.population);
        break;
    case UPDATE_COUNTRY:
        // To undo an update, we revert to the previous population
        updateCountry(op.country.name, op.prevName, op.prevPopulation);
        break;
    }

    // Push the operation to the redo stack
    pushRedo(op);
}

void redo() {
    if (redoTop == -1) {
        printf("No operations to redo.\n");
        return;
    }

    // Pop the last operation from the redo stack
    Operation op = redoStack[redoTop--];

    // Perform redo based on the operation type
    switch (op.type) {
    case ADD_COUNTRY:
        addCountry(op.country.name, op.country.continent, op.country.population);
        break;
    case DELETE_COUNTRY:
        deleteCountry(op.country.name);
        break;
    case UPDATE_COUNTRY:
        updateCountry(op.country.name, op.prevName, op.country.population);
        break;
    }

    // Push the operation to the undo stack
    pushUndo(op);
}

void pushUndo(Operation op) {
    if (undoTop < 99) {
        undoStack[++undoTop] = op;
    }
}

void pushRedo(Operation op) {
    if (redoTop < 99) {
        redoStack[++redoTop] = op;
    }
}