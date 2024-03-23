#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent a Country
typedef struct {
    char name[50];
    char continent[20];
    float population;
} Country;

Country countries[100];
int countryCount = 0;

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
Operation undoStack[100];
int undoTop = -1;
Operation redoStack[100];
int redoTop = -1;

// Function Prototypes
void addDefaultCountries();
void addCountry(const char* name, const char* continent, float population);
void deleteCountry(const char* name);
void updateCountry(const char* name, const char* migrationTo, float migrationPopulation);
void displayCountriesByGivenString(const char* searchString);

void undo();
void redo();
void pushUndo(Operation op);
void pushRedo(Operation op);
// Main menu function
void printMenu();
void mainMenu();

int main() {
    mainMenu();
    return 0;
}

// Function to add 10 default countries
void addDefaultCountries() {
    addCountry("Germany", "Europe", 83.2);
    addCountry("Mexico", "America", 128.9);
    addCountry("Indonesia", "Asia", 273.5);
    addCountry("Egypt", "Africa", 102.3);
    addCountry("United Kingdom", "Europe", 67.9);
    addCountry("Vietnam", "Asia", 97.3);
    addCountry("Argentina", "America", 45.4);
    addCountry("Kenya", "Africa", 53.8);
    addCountry("Spain", "Europe", 46.9);
    addCountry("Thailand", "Asia", 69.8);
}

// Function to add or update a country
void addCountry(const char* name, const char* continent, float population) {
    int index = -1;

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

// Function to display countries containing a given string
void displayCountriesByGivenString(const char* searchString) {
    int considerAllCountries = searchString == NULL || strlen(searchString) == 0;

    for (int i = 0; i < countryCount; ++i) {
        if (considerAllCountries || strstr(countries[i].name, searchString) != NULL) {
            printf("Name: %s, Continent: %s, Population: %.2f million\n",
                countries[i].name, countries[i].continent, countries[i].population);
        }
    }
}



// Filter functions
int filterBelow100Million(const Country* country) {
    return country->population < 100;
}

int filterAboveOrEqual100Million(const Country* country) {
    return country->population >= 100;
}
typedef int (*CountryDisplayFilter)(const Country*);
void displayCountriesByGivenPopulation(const char* searchString, CountryDisplayFilter filter) {
    int displayAll = searchString == NULL || strlen(searchString) == 0;

    for (int i = 0; i < countryCount; ++i) {
        if (filter(&countries[i])) {
            printf("Name: %s, Continent: %s, Population: %.2f million\n",
                countries[i].name, countries[i].continent, countries[i].population);
        }
    }
}

void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {} // Clear the input buffer
}

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

// The main menu for UI
void printMenu() {
    printf("\nWorld Population Monitoring\n");
    printf("1. Add country.\n");
    printf("2. Delete country.\n");
    printf("3. Update country.\n");
    printf("4. Display countries by a given string.\n");
    printf("5. Undo last operation.\n");
    printf("6. Redo last operation.\n");
    printf("7. Display all countries whose population over 100 million\n");
    printf("8. Exit!\n");
}

// Function to display the main menu
void mainMenu() {
    // Add 10 default countries
    addDefaultCountries();

    // Display the initial list of countries
    displayCountriesByGivenString("");

    // Add, delete, update, and display countries based on user input
    int choice;
    do {
        printMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);
        clearInputBuffer(); // Clear buffer after scanf to prepare for fgets

        switch (choice) {
        case 1: {
            char name[50];
            char continent[20];
            float population;

            printf("Enter Country Name: ");
            scanf("%s", name);

            printf("Enter Continent: ");
            scanf("%s", continent);

            printf("Enter Population (in million): ");
            scanf("%f", &population);

            addCountry(name, continent, population);
            break;
        }
        case 2: {
            char name[50];
            printf("Enter Country Name to Delete: ");
            scanf("%s", name);
            deleteCountry(name);
            break;
        }
        case 3: {
            char name[50];
            char migrationTo[50];
            float migrationPopulation;

            printf("Enter Country Name: ");
            scanf("%s", name);

            printf("Enter Migration To (leave empty for no migration): ");
            scanf("%s", migrationTo);

            if (strlen(migrationTo) > 0) {
                printf("Enter Migration Population (in million): ");
                scanf("%f", &migrationPopulation);
            }
            else {
                migrationPopulation = 0;
            }

            updateCountry(name, migrationTo, migrationPopulation);
            break;
        }
        case 4: {
            char input[100]; // Adjust size as necessary

            printf("Enter a search string (press enter for all countries): ");
            fgets(input, sizeof(input), stdin);

            // Remove newline character if present
            input[strcspn(input, "\n")] = 0;

            displayCountriesByGivenString(strlen(input) > 0 ? input : NULL);
            break;
        }
        case 5:
            undo();
            break;
        case 6:
            redo();
            break;
        case 7:
        {
            char input[100]; // Adjust size as necessary
            printf("Press enter for below 100 million ");
            fgets(input, sizeof(input), stdin);

            // Remove newline character if present
            input[strcspn(input, "\n")] = 0;

            CountryDisplayFilter filter = (strlen(input) > 0) ? filterAboveOrEqual100Million : filterBelow100Million;

            // You might want to modify this to pass an appropriate searchString or NULL
            displayCountriesByGivenPopulation(NULL, filter);
            break;
        }
        case 8:
        {
            printf("Bye!\n");
            return;
        }
        default:
            printf("Invalid choice! Please try again!\n");
        }

    } while (choice != 8);
}
