#pragma once
#include <string>

typedef struct
{
	int minutes, seconds;
}Duration;

class Tutorial
{
private:
	std::string title;
	std::string presenter;
	int likes;
	Duration duration;
	std::string link;
public:
	Tutorial() : title(""), presenter(""), likes(0), duration({ 0, 0 }), link("") {}
	Tutorial(std::string title,
		std::string presenter,
		Duration duration,
		int likes,
		std::string link);
	std::string getTitle();
	std::string getPresenter();
	Duration getDuration();
	int getLikes();
	std::string getLink();
	void setTitle(std::string newTitle);
	void setPresenter(std::string newPresenter);
	void setDuration(Duration newDuration);
	void setLikes(int newLikes);
	void setLink(std::string newLink);
	bool operator==(const Tutorial& tutorialToCompare);
	void operator=(const Tutorial& tutorialToCopy);
};

