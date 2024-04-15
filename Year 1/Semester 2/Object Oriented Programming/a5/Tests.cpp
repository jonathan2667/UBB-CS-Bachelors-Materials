#include "Tests.h"
#include <assert.h>
#include <iostream>

void Tests::testDynamicVector()
{
    DynamicVector<int> testVector;
    assert(testVector.getSize() == 0);

    // Test adding elements
    for (int index = 0; index <= 10; index++)
        testVector.addElement(index);
    assert(testVector.getSize() == 11);

    // Test getting elements
    assert(testVector.getElement(0) == 0);
    assert(testVector.getElement(1) == 1);
    assert(testVector.getElement(2) == 2);

    // Test updating elements
    testVector.updateElement(1, 5);
    assert(testVector.getElement(1) == 5);

    // Test removing elements
    testVector.removeElement(0);
    testVector.removeElement(77);
    assert(testVector.getSize() == 10);
    assert(testVector.getElement(0) == 5);
    assert(testVector.getElement(1) == 2);

    // Test findPositionOfElement
    assert(testVector.findPositionOfElement(2) == 1);
    assert(testVector.findPositionOfElement(5) == 0);
    assert(testVector.findPositionOfElement(100) == -1);

    // Test copy constructor
    DynamicVector<int> testVectorForCopy(testVector);
    assert(testVectorForCopy.getSize() == 10);
    assert(testVectorForCopy.getElement(0) == 5);
    assert(testVectorForCopy.getElement(1) == 2);

    // Test assignment operator
    DynamicVector<int> testVectorToAssign;
    testVectorToAssign = testVectorForCopy;
    assert(testVectorToAssign.getSize() == 10);
    assert(testVectorToAssign.getElement(0) == 5);
    assert(testVectorToAssign.getElement(1) == 2);
}

void Tests::testDomain()
{
    Duration duration;
    duration.minutes = 1;
    duration.seconds = 30;
    Tutorial testTutorial("Object Oriented Programming", "John Smith", duration, 100, "www.example.com");

    // Test getters
    assert(testTutorial.getTitle() == "Object Oriented Programming");
    assert(testTutorial.getPresenter() == "John Smith");
    assert(testTutorial.getDuration().minutes == 1);
    assert(testTutorial.getDuration().seconds == 30);
    assert(testTutorial.getLikes() == 100);
    assert(testTutorial.getLink() == "www.example.com");

    // Test setters
    testTutorial.setTitle("Data Structures and Algorithms");
    assert(testTutorial.getTitle() == "Data Structures and Algorithms");
    testTutorial.setPresenter("Jane Doe");
    assert(testTutorial.getPresenter() == "Jane Doe");
    Duration newDuration;
    newDuration.minutes = 2;
    newDuration.seconds = 15;
    testTutorial.setDuration(newDuration);
    assert(testTutorial.getDuration().minutes == 2 && testTutorial.getDuration().seconds == 15);
    testTutorial.setLikes(200);
    assert(testTutorial.getLikes() == 200);
    testTutorial.setLink("www.example2.com");
    assert(testTutorial.getLink() == "www.example2.com");

    // Test equality operator
    Tutorial testTutorialEqual("Data Structures and Algorithms", "Jane Doe", newDuration, 200, "www.example2.com");
    assert(testTutorial == testTutorialEqual);

    // Test assignment operator
    Tutorial testTutorialAssign("Intro to C++", "Sarah Johnson", duration, 50, "www.cpp.com");
    testTutorial = testTutorialAssign;
    assert(testTutorial.getTitle() == "Intro to C++");
    assert(testTutorial.getPresenter() == "Sarah Johnson");
    assert(testTutorial.getDuration().minutes == 1);
    assert(testTutorial.getLikes() == 50);
    assert(testTutorial.getLink() == "www.cpp.com");
}

void Tests::testRepository()
{
    this->testGetAllTutorials();
    this->testAddTutorialToRepository();
    this->testRemoveTutorialFromRepository();
    this->testUpdateTutorialToRepository();
    this->testGetTutorialPositionInRepository();
}

void Tests::testGetAllTutorials()
{
    // Test the getAllTutorials function
    Tutorial testTutorialToInitialiseRepository("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com");
    // Initialize the repository with the sample tutorials
    DynamicVector<Tutorial> initialTutorials;
    initialTutorials.addElement(testTutorialToInitialiseRepository);
    Repository repository(initialTutorials);
    DynamicVector<Tutorial> allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 1);
    assert(allTutorials.getElement(0) == Tutorial("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com"));

}

void Tests::testAddTutorialToRepository()
{

    Tutorial validTutorial("Title 4", "Presenter 4", Duration{ 0, 30 }, 25, "https://www.youtube.com");
    // Initialize the repository with the sample tutorials
    DynamicVector<Tutorial> initialTutorials;
    Repository repository(initialTutorials);
    // Test the addTutorialToRepository function
    bool added = repository.addTutorial(validTutorial);
    assert(added == true);
    DynamicVector<Tutorial> allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 1);
    assert(allTutorials.getElement(0) == validTutorial);
    // Test adding the same tutorial again (should not add)
    added = repository.addTutorial(validTutorial);
    assert(added == false);
    allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 1);
}

void Tests::testRemoveTutorialFromRepository()
{
    Tutorial testTutorialToCheckRemoveElement("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com");
    Tutorial testTutorialToCheckRemovedPosition("Title 2", "Presenter 2", Duration{ 0, 45 }, 15, "https://www.youtube.com");
    Tutorial tutorialToTestAdd("Title 4", "Presenter 4", Duration{ 0, 30 }, 25, "https://www.youtube.com");

    // Initialize the repository with the sample tutorials
    DynamicVector<Tutorial> initialTutorials;
    initialTutorials.addElement(testTutorialToCheckRemoveElement);
    initialTutorials.addElement(testTutorialToCheckRemovedPosition);
    Repository repository(initialTutorials);

    // Test the removeTutorialFromRepository function
    bool removed = repository.removeTutorial(1);
    assert(removed == true);
    DynamicVector<Tutorial> allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 1);
    assert(allTutorials.getElement(0) == testTutorialToCheckRemoveElement);

    // Test removing a tutorial with an invalid index (should not remove)
    removed = repository.removeTutorial(77);
    assert(removed == false);
    allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 1);

    // Test adding a tutorial after removing one
    bool added = repository.addTutorial(tutorialToTestAdd);
    assert(added == true);
    allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 2);
    assert(allTutorials.getElement(1) == tutorialToTestAdd);
}

void Tests::testUpdateTutorialToRepository()
{
    Tutorial testTutorialToCheckUpdatePosition("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com");
    Tutorial testTutorialToBeUpdated("Title 2", "Presenter 2", Duration{ 0, 45 }, 15, "https://www.youtube.com");
     // Initialize the repository with the sample tutorials
    DynamicVector<Tutorial> initialTutorials;
    initialTutorials.addElement(testTutorialToCheckUpdatePosition);
    initialTutorials.addElement(testTutorialToBeUpdated);
    Repository repository(initialTutorials);
    // Test updating a tutorial at a valid index
    Tutorial tutorialToTestUpdate("Title 4", "Presenter 4", Duration{ 0, 30 }, 25, "https://www.youtube.com");
    repository.addTutorial(tutorialToTestUpdate);
    Tutorial updatedTutorial("Updated Title 4", "Updated Presenter 4", Duration{ 0, 45 }, 20, "https://www.youtube.com");
    bool updated = repository.updateTutorial(2, updatedTutorial);
    assert(updated == true);
    DynamicVector<Tutorial> allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 3);
    assert(allTutorials.getElement(2) == updatedTutorial);

    // Test updating a tutorial at an invalid index
    updated = repository.updateTutorial(77, updatedTutorial);
    assert(updated == false);
    allTutorials = repository.getAllTutorials();
    assert(allTutorials.getSize() == 3);
    assert(allTutorials.getElement(2) == updatedTutorial);
}

void Tests::testGetTutorialPositionInRepository()
{
    Tutorial testTutorial1("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com");

    // Initialize the repository with the sample tutorials
    DynamicVector<Tutorial> initialTutorials;
    initialTutorials.addElement(testTutorial1);
    Repository repository(initialTutorials);

    // Test the getTutorialPositionInRepository function with an existing tutorial
    int position = repository.getTutorialPosition(testTutorial1);
    assert(position == 0);

    // Test the getTutorialPositionInRepository function with a non-existing tutorial
    Tutorial nonExistingTutorial("Non-Existing", "Presenter", Duration{ 0, 30 }, 25, "https://www.youtube.com");
    position = repository.getTutorialPosition(nonExistingTutorial);
    assert(position == -1);
}

void Tests::testAdministratorService()
{
    DynamicVector<Tutorial> initialTutorials;
    Repository repository{ initialTutorials };
    AdministratorService administratorService{ repository };

    // Test the addTutorialToService function
    assert(administratorService.addTutorial("Title 1", "Presenter 1", Duration{ 1, 0 }, 10, "https://www.youtube.com") == true);
    assert(administratorService.addTutorial("Title 2", "Presenter 2", Duration{ 2, 0 }, 20, "https://www.youtube.com") == true);

    // Test the getAllTutorialsService function
    DynamicVector<Tutorial> allTutorials = administratorService.getAllTutorials();
    assert(allTutorials.getSize() == 2);

    // Test the removeTutorialFromService function
    assert(administratorService.removeTutorial("Title 1", "Presenter 1") == true);
    assert(administratorService.getAllTutorials().getSize() == 1);

    // Test the updateTutorialFromService function
    assert(administratorService.updateTutorial("Title 2", "Presenter 2", "New Title", "New Presenter", Duration{ 3, 0 }, 30, "https://www.youtube.com") == true);
    Tutorial updatedTutorial = administratorService.getAllTutorials().getElement(0);
    assert(updatedTutorial.getTitle() == "New Title");
    assert(updatedTutorial.getPresenter() == "New Presenter");
    assert(updatedTutorial.getDuration().minutes == 3);
    assert(updatedTutorial.getDuration().seconds == 0);
    assert(updatedTutorial.getLikes() == 30);
    assert(updatedTutorial.getLink() == "https://www.youtube.com");

    // Test the increaseLikes function
    assert(administratorService.increaseLikes("New Title", "New Presenter") == true);
    updatedTutorial = administratorService.getAllTutorials().getElement(0);
    assert(updatedTutorial.getLikes() == 31);
}


void Tests::testUserService()
{
    // create sample data
    Duration tutorialDuration1{ 10, 30 };
    Tutorial testTutorialToCheckUserAdd{ "Title 1", "Presenter 1", tutorialDuration1, 20, "https://www.youtube.com" };
    Duration tutorialDuration2{ 8, 45 };
    Tutorial testTutorialToCheckUserRemove{ "Title 2", "Presenter 2", tutorialDuration2, 10, "https://www.youtube.com" };
    
    // create UserService
    DynamicVector<Tutorial> initialTutorials;
    Repository repository{ initialTutorials };
    UserService userService{repository};

    // test addTutorialToWatchlist
    assert(userService.addTutorialToWatchlist(testTutorialToCheckUserAdd) == true);
    assert(userService.addTutorialToWatchlist(testTutorialToCheckUserAdd) == false);
    assert(userService.getWatchlist().getSize() == 1);

    // test removeTutorialFromWatchlist
    assert(userService.removeTutorialFromWatchlist("Title 1", "Presenter 1") == true);
    assert(userService.removeTutorialFromWatchlist("Title 1", "Presenter 1") == false);
    assert(userService.getWatchlist().getSize() == 0);

    // test getTutorialsOfGivenPresenter
    DynamicVector<Tutorial> allTutorials;
    allTutorials.addElement(testTutorialToCheckUserAdd);
    allTutorials.addElement(testTutorialToCheckUserRemove);
    DynamicVector<Tutorial> neededTutorials = userService.getTutorialsOfGivenPresenter(allTutorials, "");
    assert(neededTutorials.getSize() == 2);
    neededTutorials = userService.getTutorialsOfGivenPresenter(allTutorials, "Presenter 1");
    assert(neededTutorials.getSize() == 1);
}

void Tests::testAll()
{
    this->testDynamicVector();
    this->testDomain();
    this->testRepository();
    this->testAdministratorService();
    this->testUserService();
}
