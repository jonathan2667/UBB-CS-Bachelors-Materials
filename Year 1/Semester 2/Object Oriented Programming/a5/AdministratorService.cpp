#include "AdministratorService.h"
#include<iostream>

AdministratorService::AdministratorService(Repository initialTutorialsRepository) : tutorialsRepository{initialTutorialsRepository}
{
}

bool AdministratorService::addTutorial(std::string title, std::string presenter, Duration duration, int likes, std::string link)
{
    Tutorial tutorialToAdd{ title, presenter, duration, likes, link };
    return this->tutorialsRepository.addTutorial(tutorialToAdd);
}

bool AdministratorService::removeTutorial(std::string title, std::string presenter)
{
    Duration nullDuration;
    nullDuration.minutes = 0;
    nullDuration.seconds = 0;
    Tutorial tutorialToRemove{ title, presenter, nullDuration, 0, "" };
    int indexOfTutorialToRemove = this->tutorialsRepository.getTutorialPosition(tutorialToRemove);
    return this->tutorialsRepository.removeTutorial(indexOfTutorialToRemove);
}

bool AdministratorService::updateTutorial(std::string title, std::string presenter, std::string newTitle, std::string newPresenter, Duration newDuration, int newLikes, std::string newLink)
{
    Duration nullDuration;
    nullDuration.minutes = 0;
    nullDuration.seconds = 0;
    Tutorial tutorialToUpdate{ title, presenter, nullDuration, 0, "" };
    Tutorial updatedTutorial{ newTitle, newPresenter, newDuration, newLikes, newLink };
    int indexOfTutorialToUpdate = this->tutorialsRepository.getTutorialPosition(tutorialToUpdate);
    return this->tutorialsRepository.updateTutorial(indexOfTutorialToUpdate, updatedTutorial);
}

bool AdministratorService::increaseLikes(std::string title, std::string presenter)
{
    Duration nullDuration;
    nullDuration.minutes = 0;
    nullDuration.seconds = 0;
    Tutorial tutorialToUpdate{ title, presenter, nullDuration, 0, "" };
    int indexOfTutorialToUpdate = this->tutorialsRepository.getTutorialPosition(tutorialToUpdate);
    Tutorial oldTutorial = this->tutorialsRepository.getAllTutorials().getElement(indexOfTutorialToUpdate);
    Tutorial updatedTutorial{ title, presenter, oldTutorial.getDuration(), oldTutorial.getLikes() + 1, oldTutorial.getLink()};
    return this->tutorialsRepository.updateTutorial(indexOfTutorialToUpdate, updatedTutorial);
}

DynamicVector<Tutorial> AdministratorService::getAllTutorials()
{
    return this->tutorialsRepository.getAllTutorials();
}

void AdministratorService::initializeAllTutorials()
{
    Duration duration;

    duration = generateRandomDuration();
    this->addTutorial("Learn C++ in 24h", "FreeCodeCamp", duration, 100785, "https://www.youtube.com");

    duration = generateRandomDuration();
    this->addTutorial("C++ Data Structures", "CS Dojo", duration, 184946, "https://www.odysee.com");

    duration = generateRandomDuration();
    this->addTutorial("C++ - From Zero To Hero", "Academind", duration, 1054165, "https://www.vimeo.com");

    duration = generateRandomDuration();
    this->addTutorial("C & C++ for Beginners", "BroCode", duration, 546354, "https://www.youtube.com");

    duration = generateRandomDuration();
    this->addTutorial("Game Devlopement with C++", "FreeCodeCamp", duration, 456434, "https://www.youtube.com");

    duration = generateRandomDuration();
    this->addTutorial("How to learn C++?", "Programming with Mosh", duration, 645654, "https://www.youtube.com");

    duration = generateRandomDuration();
    this->addTutorial("C++ Developer Roadmap", "Fireship", duration, 54656, "https://www.vimeo.com");

    duration = generateRandomDuration();
    this->addTutorial("How to master C++", "CS Dojo", duration, 100596, "https://www.odysee.com");

    duration = generateRandomDuration();
    this->addTutorial("Full Course - OOP in C++", "FreeCodeCamp", duration, 563000, "https://www.youtube.com");

    duration = generateRandomDuration();
    this->addTutorial("Introduction in C++", "BroCode", duration, 1674500, "https://www.youtube.com");

}


Duration AdministratorService::generateRandomDuration()
{
    Duration duration;
    duration.seconds = rand()%60;
    duration.minutes = rand()%60;
    return duration;
}