from src.repository.repository_exception import RepositoryException

class Repository:
    def __init__(self):
        self._data = {}

    def check_if_present(self, id):
        if id in self._data:
            raise RepositoryException("It is already in!")

    def check_if_not_present(self, id):
        if id not in self._data:
            raise RepositoryException("It is not in!")

    def get_element_by_id(self, id):
        return self._data[id]

    def add(self, object):
        self.check_if_present(object.id)
        self._data[object.id] = object

    def remove(self, id):
        self.check_if_not_present(id)
        del self._data[id]

    def update(self, object):
        self.check_if_not_present(object.id)
        self._data[object.id] = object

    def search_by_id(self, id):
        object_list = []
        id = str(id)

        for object in self._data.values():
            object_id = str(object.id)
            if id in object_id:
                object_list.append(object)

        return object_list

    def search_by_name(self, name):
        object_list = []
        name = name.lower()

        for object in self._data.values():
            object_name = object.name.lower()
            if name in object_name:
                object_list.append(object)

        return object_list

    def get_all(self):
        return list(self._data.values())

    def get_all_ids(self):
        return list(self._data.keys())

    def delete_all(self):
        self._data.clear()
