
import os


class Dictionary:
    def __init__(self):
        # Initialize the 'titles' dictionary
        self.titles = {}

    def add_title(self, title, score):
        """
        Check if a title exits in the dictionary.
        If so, alert title already exists.
        If not, add to dictionary.
        """
        if title in self.titles:
            raise KeyError(f'{title} already exists.')
        else:
            self.titles[title] = str(score)

    def remove_title(self, title):
        """
        Checks if a title exists in the 'titles' dictionary.
        If so, delete the title element from the dictionary.
        Else, alert that the title does not exist.
        """
        if title in self.titles:
            del self.titles[title]
        else:
            raise KeyError(f'{title} does not exist.')

    def save(self, file_name):
        """Writes the key, value pairs within the 'titles' dictionary into 'save.txt' file."""
        if file_name == '':
            raise KeyError(f'File name cannot be blank.')
        else:
            with open(os.path.join(os.path.expanduser('~'), 'Documents/ranking_list/saves', file_name), 'w') as outfile:
                for key, value in self.titles.items():
                    outfile.write(key)
                    outfile.write('\t')
                    outfile.write(value)
                    outfile.write('\n')

    def delete(self, file_name):
        """Deletes the contents of 'save.txt' file."""
        if file_name in os.listdir(os.path.join(os.path.expanduser('~'), 'Documents/ranking_list/saves')):
            os.remove(os.path.join(os.path.expanduser('~'), 'Documents/ranking_list/saves', file_name))
        elif file_name == '':
            raise KeyError('File name cannot be blank.')
        else:
            raise KeyError(f'{file_name} does not exist in directory.')

    def load(self, file_name):
        """Reads the lines of 'save.txt' and adds them to the 'titles' dictionary as key, value pairs."""
        if file_name in os.listdir(os.path.join(os.path.expanduser('~'), 'Documents/ranking_list/saves')):
            with open(os.path.join(os.path.expanduser('~'), 'Documents/ranking_list/saves', file_name), 'r') as outfile:
                for line in outfile:
                    key, value = line.split('\t')
                    value = value.rstrip()
                    self.titles[key] = value
        elif file_name == '':
            raise KeyError('File name cannot be blank.')
        else:
            raise KeyError(f'{file_name} does not exist in directory.')

    def sort_by_score(self):
        """:return: a sorted list of tuples of the 'titles' dictionary's key, value pairs."""
        return sorted(self.titles.items(), key=lambda x: x[1], reverse=True)
