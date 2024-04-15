#include "Tutorial.h"

Tutorial::Tutorial(std::string title, std::string presenter, Duration duration, int likes, std::string link)
{
    this->title = title;
    this->presenter = presenter;
    this->duration = duration;
    this->likes = likes;
    this->link = link;

}

std::string Tutorial::getTitle()
{
    return this->title;
}

std::string Tutorial::getPresenter()
{
    return this->presenter;
}

Duration Tutorial::getDuration()
{
    return this->duration;
}

int Tutorial::getLikes()
{
    return this->likes;
}

std::string Tutorial::getLink()
{
    return this->link;
}

void Tutorial::setTitle(std::string newTitle)
{
    this->title = newTitle;
}

void Tutorial::setPresenter(std::string newPresenter)
{
    this->presenter = newPresenter;
}

void Tutorial::setDuration(Duration newDuration)
{
    this->duration = newDuration;
}

void Tutorial::setLikes(int newLikes)
{
    this->likes = newLikes;
}

void Tutorial::setLink(std::string newLink)
{
    this->link = newLink;
}

bool Tutorial::operator==(const Tutorial& tutorialToCompare)
{
    if (this->title == tutorialToCompare.title && this->presenter == tutorialToCompare.presenter)
        return true;
    return false;
}

void Tutorial::operator=(const Tutorial& tutorialToCopy)
{
    this->title = tutorialToCopy.title;
    this->presenter = tutorialToCopy.presenter;
    this->duration = tutorialToCopy.duration;
    this->likes = tutorialToCopy.likes;
    this->link = tutorialToCopy.link;
}
