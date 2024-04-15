#pragma once
#include "Repository.h"

class AdministratorService
{
private:
	Repository tutorialsRepository;
public:
	AdministratorService(Repository initialTutorialsRepository);
	bool addTutorial(std::string title, std::string presenter, Duration duration, int likes, std::string link);
	bool removeTutorial(std::string title, std::string presenter);
	bool updateTutorial(std::string title, std::string presenter, std::string newTitle, std::string newPresenter, Duration newDuration, int newLikes, std::string newLink);
	bool increaseLikes(std::string title, std::string presenter);
	DynamicVector<Tutorial> getAllTutorials();
	void initializeAllTutorials();
	Duration generateRandomDuration();
};

