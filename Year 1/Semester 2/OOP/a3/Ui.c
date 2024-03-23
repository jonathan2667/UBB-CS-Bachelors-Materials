#include<stdio.h>
#include "Ui.h"
#include "Repo.h"
#include "Services.h"

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

void addDefaultCountries() {
    addCountry("Germany", "Europe", 83.3);
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

void displayCountriesByGivenString(const char* searchString) {
    int considerAllCountries = searchString == NULL || strlen(searchString) == 0;

    for (int i = 0; i < countryCount; ++i) {
        if (considerAllCountries || strstr(countries[i].name, searchString) != NULL) {
            printf("Name: %s, Continent: %s, Population: %.2f million\n",
                countries[i].name, countries[i].continent, countries[i].population);
        }
    }
}

void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {} // Clear the input buffer
}

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

void mainMenu() {
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

            //Remove newline character if present
            input[strcspn(input, "\n")] = 0;

            CountryDisplayFilter filter = (strlen(input) > 0) ? filterAboveOrEqual100Million : filterBelow100Million;

            //// You might want to modify this to pass an appropriate searchString or NULL
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