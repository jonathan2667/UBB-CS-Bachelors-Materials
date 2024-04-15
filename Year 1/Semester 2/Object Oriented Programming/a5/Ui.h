#pragma once
#include "AdministratorService.h"
#include "UserService.h"

class Ui
{
private:
	AdministratorService administratorService;
	UserService userService;
public:
	Ui(AdministratorService initialAdministratorService, UserService initialUserService);
	
	//administrator functionalities
	void addTutorialUi();
	void removeTutorialUi();
	void updateTutorialUi();
	void displayAllTutorials();
	void printAdministratorMenu();
	void administratorMode();

	//user functionalities
	void searchTutorialsByPresenter();
	void removeTutorialFromWatchlistUi();
	void displayWatchlist();
	void printUserMenu();
	void userMode();

	void startApplication();
};

