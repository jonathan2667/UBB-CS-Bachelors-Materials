#pragma once
#include "Repository.h"

class UserService
{
private:
	Repository tutorialsRepository;
	DynamicVector<Tutorial> watchlist;
public:
	UserService(Repository initialTutorialsRepository);
	bool addTutorialToWatchlist(Tutorial tutorialToAdd);
	bool removeTutorialFromWatchlist(std::string title, std::string presenter);
	DynamicVector<Tutorial> getTutorialsOfGivenPresenter(DynamicVector<Tutorial> allTutorials, std::string presenter);
	DynamicVector<Tutorial> getWatchlist();
};

