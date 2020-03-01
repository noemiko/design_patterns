# Factory Method
# In the Factory Method, we execute a single function, passing a parameter that
# provides information about what we want. We are not required to know any details
# about how the object is implemented and where it is coming from.
import json
import xml.etree.ElementTree as tree


class FactoryParser:
    def __new__(cls, filepath):
        if filepath.endswith('json'):
            connector = JSONParser
        elif filepath.endswith('xml'):
            connector = XMLParser
        else:
            raise ValueError('Cannot connect to {}'.format(filepath))
        return connector(filepath)


class JSONParser:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as file:
            self.data = json.load(file)

    @property
    def parsed_data(self):
        return self.data


class XMLParser:
    def __init__(self, filepath):
        self.tree = tree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = FactoryParser(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    extract_data_from('data/recipes.yolo')

    xml_file = extract_data_from("./data/books.xml")
    books = xml_file.parsed_data.getroot()
    for book in books:
        print(book.tag, book.attrib)
    json_file = extract_data_from("./data/example_2.json")

    for movie in json_file.parsed_data:
        print(movie)


if __name__ == '__main__':
    main()
