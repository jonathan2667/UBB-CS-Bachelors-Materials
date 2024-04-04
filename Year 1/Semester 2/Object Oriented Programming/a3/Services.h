#pragma once

#include "repo.h"

void addCountry(const char* name, const char* continent, float population);
void deleteCountry(const char* name);
void updateCountry(const char* name, const char* migrationTo, float migrationPopulation);

void undo();
void redo();
void pushRedo(Operation op);
void pushUndo(Operation op);