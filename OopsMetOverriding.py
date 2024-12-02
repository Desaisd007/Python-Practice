from abc import ABC,abstractmethod

class parent(ABC):
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print('parent display called')


class child(parent):
    def show(self):
        print('child show called')

    def display(self):
        print('child display called')
        super().display()
c=child()
c.show()
c.display()
