#include "UserService.h"

UserService::UserService(Repository initialTutorialsRepository) :
	tutorialsRepository{initialTutorialsRepository}
{
}

bool UserService::addTutorialToWatchlist(Tutorial tutorialToAdd)
{
	if (this->watchlist.findPositionOfElement(tutorialToAdd) != -1)
		return false;
	this->watchlist.addElement(tutorialToAdd);
	return true;
}


bool UserService::removeTutorialFromWatchlist(std::string title, std::string presenter)
{
	Duration nullDuration;
	nullDuration.minutes = 0;
	nullDuration.seconds = 0;
	Tutorial tutorialToRemove{ title, presenter, nullDuration, 0, "" };
	int indexOfTutorialToRemove = this->watchlist.findPositionOfElement(tutorialToRemove);
	if (indexOfTutorialToRemove < 0 || indexOfTutorialToRemove > this->watchlist.getSize())
		return false;
	this->watchlist.removeElement(indexOfTutorialToRemove);
	return true;
}

DynamicVector<Tutorial> UserService::getTutorialsOfGivenPresenter(DynamicVector<Tutorial> allTutorials, std::string presenter)
{
	if (presenter.compare("") == 0)
		return allTutorials;
	DynamicVector <Tutorial> neededTutorials;
	int sizeOfRepository = allTutorials.getSize();
	for (int index = 0; index < sizeOfRepository; index++)
	{
		Tutorial currentTutorial = allTutorials.getElement(index);
		if (currentTutorial.getPresenter().compare(presenter) == 0)
			neededTutorials.addElement(currentTutorial);
	}
	return neededTutorials;
}

DynamicVector<Tutorial> UserService::getWatchlist()
{
	return this->watchlist;
}
