#pragma once

template <typename T>
class DynamicVector
{
private:
	int capacity, size;
	T* elements;
	void resize();

public:
	//constructor
	DynamicVector(int initialCapacity = 10);

	//destructor
	~DynamicVector();

	//copy constructor
	DynamicVector(const DynamicVector& dynamicVectorToCopy);

	//assignemnt operator
	DynamicVector& operator=(const DynamicVector& dynamicVector);

	//methods
	void addElement(const T& elementToAdd);
	void removeElement(int indexFromWhereToRemove);
	void updateElement(int indexOfElementToUpdate, T updatedElement);
	int getSize();
	T getElement(int indexOfElementToGet);
	int findPositionOfElement(T elementToFindPosition);

};

template<typename T>
inline void DynamicVector<T>::resize()
{
	int temporaryCapacity = this->capacity * 2;
	T* temporaryElements = new T[temporaryCapacity];
	if (temporaryElements == nullptr)
		return;
	this->capacity = temporaryCapacity;
	for (int index = 0; index < this->size; index++)
		temporaryElements[index] = this->elements[index];
	delete[] this->elements;
	this->elements = temporaryElements;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(int initialCapacity) : 
	capacity{initialCapacity}, size{0}
{
	this->elements = new T[this->capacity];
}

template<typename T>
inline DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(const DynamicVector& dynamicVectorToCopy)
{
	this->capacity = dynamicVectorToCopy.capacity;
	this->size = dynamicVectorToCopy.size;
	this->elements = new T[this->capacity];
	for (int index = 0; index < this->size; index++)
		this->elements[index] = dynamicVectorToCopy.elements[index];
}

template<typename T>
inline DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector& dynamicVector)
{
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;
	
	delete[] this->elements;
	this->elements = new T[this->capacity];
	for(int index=0; index < this->size; index++)
		this->elements[index] = dynamicVector.elements[index];
	return *this;
}

template<typename T>
inline void DynamicVector<T>::addElement(const T& elementToAdd)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = elementToAdd;
	this->size++;
}

template<typename T>
inline void DynamicVector<T>::removeElement(int indexFromWhereToRemove)
{
	if (indexFromWhereToRemove < 0 || indexFromWhereToRemove>this->size)
		return;
	T* temporaryElements = new T[this->capacity];
	for (int index = 0; index < indexFromWhereToRemove; index++)
		temporaryElements[index] = this->elements[index];
	for (int index = indexFromWhereToRemove + 1; index < this->size; index++)
		temporaryElements[index - 1] = this->elements[index];
	delete[] this->elements;
	this->elements = temporaryElements;
	this->size--;
}

template<typename T>
inline void DynamicVector<T>::updateElement(int indexOfElementToUpdate, T updatedElement)
{
	this->elements[indexOfElementToUpdate] = updatedElement;
}

template<typename T>
inline int DynamicVector<T>::getSize()
{
	return this->size;
}

template<typename T>
inline T DynamicVector<T>::getElement(int indexOfElementToGet)
{
	return this->elements[indexOfElementToGet];
}

template<typename T>
inline int DynamicVector<T>::findPositionOfElement(T elementToFindPosition)
{
	for (int index = 0; index < this->size; index++)
		if (elementToFindPosition == this->elements[index])
			return index;
	return -1;
}
