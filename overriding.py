import logging

logging.basicConfig(filename='oops_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Parent:
    parent_attr = 100

    def __init__(self):
        print("Parent Constructor")

    def parent_method(self):
        print("Parent Method")

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print("Parent Attribute: ", Parent.parent_attr)


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")

    def child_method(self):
        print("Child Method")

    def parent_method(self):
        print("Overriding Parent Method")


if __name__ == '__main__':
    child = Child()
    child.child_method()
    child.parent_method()
    child.set_attr(200)
    child.get_attr()
