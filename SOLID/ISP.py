# Interface Segregation Principle
# you don't want to put so many methods into an interface/base-class

from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # do something meaningful here
        pass

# *** these two methods are bad design and breaks ISP pattern ***
    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print("I am scanning the doc")


# this base class inherits from two other base classes, although it is not recommended in most cases
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    # here we use decorator pattern and inject these two objects here
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # throws an exception