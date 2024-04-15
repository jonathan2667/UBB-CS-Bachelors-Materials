 #include "Ui.h"
#include <iostream>
#include <string>
#include <cstdlib>

Ui::Ui(AdministratorService initialAdministratorService, UserService initialUserService) :
	administratorService{initialAdministratorService}, userService{initialUserService}
{
}

void Ui::addTutorialUi()
{
	std::string title = "", presenter = "", link = "";
	Duration duration{0,0};
	int likes = 0;

	std::cout << "Tutorial title: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Tutorial presenter: ";
	std::getline(std::cin, presenter);

	std::cout << "Tutorial duration:\n";

	std::cout << "Minutes(0-60): ";
	std::cin >> duration.minutes;
	std::cout << "Seconds(0-60): ";
	std::cin >> duration.seconds;

	std::cout << "Tutorial likes: ";
	std::cin >> likes;

	std::cout << "Tutorial link: ";
	std::cin.ignore();
	std::getline(std::cin, link);

	bool checkAdded = this->administratorService.addTutorial(title, presenter, duration, likes, link);
	if (checkAdded == false)
		std::cout << "Tutorial already exists!\n";
	else
		std::cout << "Tutorial successfully addded!\n";
}

void Ui::removeTutorialUi()
{
	std::string title = "", presenter = "";
	
	std::cout << "Title of tutorial to remove: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Presenter of tutorial to remove: ";
	std::getline(std::cin, presenter);

	bool checkRemoved = this->administratorService.removeTutorial(title, presenter);
	if (checkRemoved == false)
		std::cout << "Tutorial doesn't exist!\n";
	else
		std::cout << "Tutorial successfully removed!\n";
}

void Ui::updateTutorialUi()
{
	std::string title = "", presenter = "";

	std::cout << "Tutorial title: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Tutorial presenter: ";
	std::getline(std::cin, presenter);

	std::string newTitle, newPresenter, newLink;
	Duration newDuration;
	int newLikes;

	std::cout << "New tutorial title: ";
	std::getline(std::cin, newTitle);

	std::cout << "New tutorial presenter: ";
	std::getline(std::cin, newPresenter);

	std::cout << "New tutorial duration: \n";
	std::cout << "Minutes: ";
	std::cin >> newDuration.minutes;
	std::cout << "Seconds: ";
	std::cin >> newDuration.seconds;

	std::cout << "New tutorial likes: ";
	std::cin >> newLikes;

	std::cout << "New tutorial link: ";
	std::cin.ignore();
	std::getline(std::cin, newLink);

	bool checkUpdated = this->administratorService.updateTutorial(title, presenter, newTitle, newPresenter, newDuration, newLikes, newLink);
	if (checkUpdated == false)
		std::cout << "Tutorial doesn't exist!\n";
	else
		std::cout << "Tutorial successfully updated!\n";
}

void Ui::displayAllTutorials()
{
	DynamicVector<Tutorial> allTutorials= this->administratorService.getAllTutorials();
	for (int index = 0; index < allTutorials.getSize(); index++)
	{
		Tutorial currentTutorial = allTutorials.getElement(index);
		Duration currentDuration = currentTutorial.getDuration();
		std::cout << "#" << index + 1<< std::endl;
		std::cout << " Title: " << currentTutorial.getTitle() << std::endl << " Presenter: " << currentTutorial.getPresenter() << std::endl;
		std::cout << " Duration: " << currentDuration.minutes << ":" << currentDuration.seconds << " Likes: " << currentTutorial.getLikes() << " Link: " << currentTutorial.getLink() << std::endl << std::endl;
	}
}

void Ui::searchTutorialsByPresenter()
{
	std::string presenter;
	std::string userOption;

	std::cout << "\nSearch a presenter: ";
	std::cin.ignore();
	std::getline(std::cin, presenter);
	DynamicVector<Tutorial> searchedTutorials = this->userService.getTutorialsOfGivenPresenter(this->administratorService.getAllTutorials(), presenter);
	int currentIndex = 0;
	while (true)
	{
		if (searchedTutorials.getSize() == 0)
		{
			std::cout << "\nInvalid search! Please enter a valid presenter!\n";
			break;
		}
		if (currentIndex == searchedTutorials.getSize())
			currentIndex = 0;
		Tutorial currentTutorial = searchedTutorials.getElement(currentIndex);
		Duration currentDuration = currentTutorial.getDuration();
		std::cout << "\n#" << currentIndex + 1 << std::endl;
		std::cout << " Title: " << currentTutorial.getTitle() << std::endl << " Presenter: " << currentTutorial.getPresenter() << std::endl;
		std::cout << " Duration: " << currentDuration.minutes << ":" << currentDuration.seconds << " Likes: " << currentTutorial.getLikes() << " Link: " << currentTutorial.getLink() << std::endl << std::endl;

		std::cout << "Do you want to add this tutorial to your wishlist ? (yes/next)\n";
		std::cout << "Write 'x' to exit search!\n\n";

		std::string command = "start " + currentTutorial.getLink();
		system(command.c_str());

		while (true)
		{
			std::cout << "> ";
			std::cin >> userOption;
			if (userOption.compare("yes") == 0)
			{
				this->userService.addTutorialToWatchlist(currentTutorial);
				currentIndex++;
				break;
			}
			else if (userOption.compare("next") == 0)
			{
				currentIndex++;
				break;
			}
			else if (userOption.compare("x") == 0)
			{
				std::cout << "You exited the search!\n";
				return;
			}
			else
				std::cout << "\nTake your time to decide!\nHint:\nyes - add to watchlist\nnext - see next tutorial in the search\nx - exit the search\n\n";
		}
		std::cout << std::endl;
	}
}

void Ui::removeTutorialFromWatchlistUi()
{
	std::string title = "", presenter = "";
	std::string userOption;

	std::cout << "Title of tutorial to remove: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Presenter of tutorial to remove: ";
	std::getline(std::cin, presenter);

	bool checkRemoved = this->userService.removeTutorialFromWatchlist(title, presenter);
	if (checkRemoved == false)
		std::cout << "Tutorial doesn't exist!\n";
	else
	{
		std::cout << "\nWould you like to leave a like at this tutorial before removing it? (yes/no)\n";
		while (true)
		{
			std::cout << "> ";
			std::cin >> userOption;
			if (userOption.compare("yes") == 0)
			{
				this->administratorService.increaseLikes(title, presenter);
				std::cout << "Thank you for your feedback!\n";
				break;
			}
			else if (userOption.compare("no") == 0)
			{
				break;
			}
			else
				std::cout << "Please choose 'yes' or 'no'!\n";
		}
		std::cout << "Tutorial successfully removed!\n";
	}
}

void Ui::displayWatchlist()
{
	DynamicVector<Tutorial> allTutorials = this->userService.getWatchlist();
	for (int index = 0; index < allTutorials.getSize(); index++)
	{
		Tutorial currentTutorial = allTutorials.getElement(index);
		Duration currentDuration = currentTutorial.getDuration();
		std::cout << "#" << index + 1 << std::endl;
		std::cout << " Title: " << currentTutorial.getTitle() << std::endl << " Presenter: " << currentTutorial.getPresenter() << std::endl;
		std::cout << " Duration: " << currentDuration.minutes << ":" << currentDuration.seconds << " Likes: " << currentTutorial.getLikes() << " Link: " << currentTutorial.getLink() << std::endl << std::endl;
	}
}

void Ui::printUserMenu()
{
	std::cout << "\nHello User!\n\n";
	std::cout << "1. Search tutorials\n";
	std::cout << "2. Remove tutorial from watchlist\n";
	std::cout << "3. Display watchlist\n";
	std::cout << "0. Exit user mode\n";
}

void Ui::userMode()
{
	int optionChosen;
	printUserMenu();
	while (true)
	{
		std::cout << "\nEnter your option: ";
		std::cin >> optionChosen;
		if (std::cin.fail() || optionChosen < 0 || optionChosen > 3) {
			std::cout << "\nInvalid input! Please enter a valid option.\n\n";
			std::cin.clear(); 
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
			continue;
		}
		switch (optionChosen)
		{
		case 1:
			searchTutorialsByPresenter();
			break;
		case 2:
			removeTutorialFromWatchlistUi();
			break;
		case 3:
			displayWatchlist();
			break;
		case 0:
			std::cout << std::endl;
			return;
		default:
			std::cout << "\nInvalid option! Please try again!\n\n";
			break;
		}
	}
}

void Ui::startApplication()
{
	std::cout << "Welcome to 'Master C++' App!\n" << std::endl;
	std::cout << "What mode do you want to enter the app? (administrator/user)\n" << "Type 'exit' to close app\n\n";
	std::string accessMode;
	while (true)
	{
		std::cout << "Enter mode: ";
		std::cin >> accessMode;
		if (accessMode.compare("administrator") == 0)
			administratorMode();
		else if (accessMode.compare("user") == 0)
			userMode();
		else if (accessMode.compare("exit") == 0)
		{
			std::cout << "\nApplication exited successfully!\n";
			return;
		}
		else
			std::cout << "\nInvalid access mode!\nHint: administrator/user/exit\n\n";	
	}
}

void Ui::printAdministratorMenu()
{
	std::cout << "\nHello Administrator!\n\n";
	std::cout << "1. Add a tutorial\n";
	std::cout << "2. Remove a tutorial\n";
	std::cout << "3. Update a tutorial\n";
	std::cout << "4. Display all tutorials\n";
	std::cout << "0. Exit administrator mode\n";

}

void Ui::administratorMode()
{
	int optionChosen;
	printAdministratorMenu();
	while (true)
	{
		std::cout << "\nEnter your option: ";
		std::cin >> optionChosen;
		if (std::cin.fail() || optionChosen < 0 || optionChosen > 4) {
			std::cout << "\nInvalid input! Please enter a valid option.\n\n";
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			continue;
		}
		switch (optionChosen)
		{
		case 1:
			addTutorialUi();
			break;
		case 2:
			removeTutorialUi();
			break;
		case 3:
			updateTutorialUi();
			break;
		case 4: 
			displayAllTutorials();
			break;
		case 0:
			std::cout << std::endl;
			return;
		default:
			std::cout << "\nInvalid option! Please try again!\n\n";
			break;
		}
	}
}
