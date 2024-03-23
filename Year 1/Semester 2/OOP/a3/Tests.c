#include "Tests.h"

// tests.c
#include <stdio.h>
#include <string.h>
#include "Services.h"
#include "Repo.h"

// Helper function to assert equality of floats, since direct comparison is not reliable
int assertFloatEqual(float a, float b) {
    float epsilon = 0.01f;
    return (fabs(a - b) < epsilon);
}

void testAddCountry() {
    printf("Testing addCountry...\n");
    addCountry("Testland", "TestContinent", 55.5);

    int found = 0;
    for (int i = 0; i < countryCount; i++) {
        if (strcmp(countries[i].name, "Testland") == 0) {
            found = 1;
            if (strcmp(countries[i].continent, "TestContinent") == 0 && assertFloatEqual(countries[i].population, 55.5)) {
                printf("PASS: testAddCountry\n");
            }
            else {
                printf("testAddCountry - continent or population\n");
            }
            break;
        }
    }
    if (!found) {
        printf("testAddCountry - Country \n");
    }
}

void testDeleteCountry() {
    printf("Testing deleteCountry...\n");
    // Ensure "Testland" is added before trying to delete
    addCountry("Testland", "TestContinent", 55.5);
    deleteCountry("Testland");

    for (int i = 0; i < countryCount; i++) {
        if (strcmp(countries[i].name, "Testland") == 0) {
            printf("testDeleteCountry - Country \n");
            return;
        }
    }
    printf("PASS: testDeleteCountry\n");
}

void testUpdateCountry() {
    printf("Testing updateCountry...\n");
    addCountry("Testland", "TestContinent", 55.5);
    updateCountry("Testland", "NewContinent", 60.0);

    for (int i = 0; i < countryCount; i++) {
        if (strcmp(countries[i].name, "Testland") == 0) {
            if (strcmp(countries[i].continent, "NewContinent") == 0 && assertFloatEqual(countries[i].population, 60.0)) {
                printf("PASS: testUpdateCountry\n\n\n\n\n");
            }
            else {
                printf(" testUpdateCountry - update\n\n\n\n\n");
            }
            return;
        }
    }
    printf(": testUpdateCountry - C update\n\n\n\n");
}

void test_all() {
    testAddCountry();
    testDeleteCountry();
    testUpdateCountry();
}

