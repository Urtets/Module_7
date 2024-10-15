class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            line = ''
            with open(file_name, encoding='utf-8') as file:
                symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for item in file:
                    line = line + item.lower()
                for i in symbols:
                    line = line.replace(i, '')
            split_line = line.split()
            all_words[file_name] = []
            all_words[file_name] = split_line
        return all_words

    def find(self, word):
        just_dict = {}
        for key in self.get_all_words():
            for i in range(len(self.get_all_words()[key])):
                if self.get_all_words()[key][i] == word.lower():
                    just_dict[key] = i + 1
                    break
        return just_dict

    def count(self, word):
        just_dict = {}
        for key in self.get_all_words():
            counter = 0
            for i in range(len(self.get_all_words()[key])):
                if self.get_all_words()[key][i] == word.lower():
                    counter += 1
            just_dict[key] = counter
        return just_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
