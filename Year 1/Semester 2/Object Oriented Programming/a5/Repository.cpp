#include "Repository.h"
#include<iostream>
Repository::Repository(DynamicVector<Tutorial> initialTutorials) : 
    allTutorials{initialTutorials}
{
}

DynamicVector<Tutorial> Repository::getAllTutorials()
{
    return this->allTutorials;
}

bool Repository::addTutorial(Tutorial tutorialToAdd)
{
    if (this->allTutorials.findPositionOfElement(tutorialToAdd) != -1)
        return false;
    this->allTutorials.addElement(tutorialToAdd);
    return true;
}

bool Repository::removeTutorial(int indexOfTutorialToRemove)
{
    if (indexOfTutorialToRemove < 0 || indexOfTutorialToRemove >= this->allTutorials.getSize())
        return false;
    this->allTutorials.removeElement(indexOfTutorialToRemove);
    return true;
}

bool Repository::updateTutorial(int indexOfTutorialToUpdate, Tutorial updatedTutorial)
{
    if (indexOfTutorialToUpdate < 0 || indexOfTutorialToUpdate >= this->allTutorials.getSize())
        return false;
    this->allTutorials.updateElement(indexOfTutorialToUpdate, updatedTutorial);
    return true;

}

int Repository::getTutorialPosition(Tutorial tutorialToGetPosition)
{
    return this->allTutorials.findPositionOfElement(tutorialToGetPosition);
}
