#pragma once
#include "Tutorial.h"
#include "DynamicVector.h"

class Repository
{
private:
	DynamicVector<Tutorial> allTutorials;
public:
	Repository(DynamicVector<Tutorial> initialTutorials = NULL);
	DynamicVector<Tutorial> getAllTutorials();
	bool addTutorial(Tutorial tutorialToAdd);
	bool removeTutorial(int indexOfTutorialToRemove);
	bool updateTutorial(int indexOfTutorialToUpdate, Tutorial updatedTutorial);
	int getTutorialPosition(Tutorial tutorialToGetPosition);
};

