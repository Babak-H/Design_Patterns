# Single Responsibility Principle
# means each class should have one and only one responsibility.
# if you put every single method inside a class, we call it god object (very bad design pattern, avoid it)


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today')
j.add_entry('I ate a bug')

print(j.__str__())

file = r'/Users/bob_g/desktop/journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as f:
    print(f.read())
