"""
text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f' <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))
"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []  # inner elements of this element

    # loop through all inner items of this object recursively
    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        # do same process for all inner elements
        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    # call htmlBuilder from current class without creating any extra objects
    @staticmethod
    def create(name):
        return HtmlBuilder(name)


# Builder Pattern
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        # returning self here allows us to chain this item to another method call
        return self

    def __str__(self):
        return str(self.__root)  # calls the __str__ method on the HtmlElement class


# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
builder = HtmlElement.create('ul')
print(builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world'))
