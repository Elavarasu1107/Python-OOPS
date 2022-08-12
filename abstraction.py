from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='oops_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class ClassOne(ABC):

    @abstractmethod
    def method_one(self):
        pass

    @abstractmethod
    def method_two(self):
        pass


class ClassTwo(ClassOne):

    def method_one(self):
        print("Method One")

    def method_two(self):
        print("Method One")


if __name__ == '__main__':
    obj = ClassTwo()
    obj.method_one()
    obj.method_two()
