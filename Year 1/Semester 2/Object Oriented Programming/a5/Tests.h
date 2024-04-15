#pragma once
#include "DynamicVector.h"
#include "Tutorial.h"
#include "Repository.h"
#include "AdministratorService.h"
#include "UserService.h"

class Tests
{
public:
	void testDynamicVector();
	void testDomain();
	void testRepository();
	void testGetAllTutorials();
	void testAddTutorialToRepository();
	void testRemoveTutorialFromRepository();
	void testUpdateTutorialToRepository();
	void testGetTutorialPositionInRepository();
	void testAdministratorService();
	void testUserService();
	void testAll();
};

