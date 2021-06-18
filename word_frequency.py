import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.file = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        self.open = open(self.file)
        self.read = self.open.read
        return self.read
        print(f"{self.read}")
        #raise NotImplementedError("FileReader.read_contents")

class WordList:
    def __init__(self, text):
        self.text = text.split().lower()
        self.word_list = []
        self.dict = {}

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        for word in self.text:
            clean = word.strip(string.punctuation)
            self.word_list.append(cleaned)
        return self.word_list

        def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
            for word in self.word_list:
                if word in STOP_WORDS:
                    self.word_list.remove(word)
                elif word in self.dict:
                    self.dict[word] = self.dict[word] + 1
                else word not in self.dict:
                    self.dict[word] = 1
        

if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
