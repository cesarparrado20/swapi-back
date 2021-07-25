def first_exercise():
    for i in range(101):
        additional_word = ''
        if i % 2 == 0:
            additional_word += ' buzz'
        if i % 5 == 0:
            additional_word += ' bazz'
        print('{}{}'.format(i, additional_word))


class SecondExercise:
    all_words = [
        'audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary',
        'bronzor', 'carracosta', 'charmeleon', 'cresselia', 'croagunk',
        'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite',
        'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur',
        'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus',
        'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone',
        'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir',
        'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel',
        'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty',
        'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax',
        'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue',
        'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull',
        'yamask'
    ]
    sub_words_dict = None
    longest_sequence = None
    size_longest_sequence = 0

    def __init__(self):
        self.sub_words_dict = self.get_sub_words_for_all_words()

    def get_sub_words_for_all_words(self):
        sub_words_dict = {}
        for name in self.all_words:
            letter = name[-1]
            words_start_with_letter = list(
                filter(lambda s: s.startswith(letter), self.all_words)
            )
            if words_start_with_letter:
                sub_words_dict.update({name: words_start_with_letter})
        return sub_words_dict

    def calculate_longest_sequence(self, word_list=None, sequence=None):
        word_list = word_list or self.all_words
        sequence = sequence or []
        for word in word_list:
            current_sequence = sequence.copy()
            sub_words = self.sub_words_dict.get(word)
            if word not in current_sequence and sub_words:
                current_sequence.append(word)
                self.calculate_longest_sequence(
                    sub_words.copy(), current_sequence.copy()
                )
            else:
                current_sequence.append(word)
                size_current_sequence = len(current_sequence)
                if size_current_sequence > self.size_longest_sequence:
                    self.size_longest_sequence = size_current_sequence
                    self.longest_sequence = current_sequence

    def execute(self):
        self.calculate_longest_sequence()
        print(' '.join(self.longest_sequence))


def main():
    print(
        'a. Desarrolla un algoritmo que imprima los números del 0 al 100. '
        'Adicionalmente debe imprimirse en la misma línea la palabra buzz en '
        'caso de que el número sea par. Sí el número es múltiplo de 5 debe '
        'imprimirse en la misma línea la palabra bazz. \n'
    )
    first_exercise()
    print("\n b. Your task in this exercise is as follows: Take the following "
          "selection of 70 English Pokemon names (extracted from Wikipedia's "
          "list of Pokemon), and generate the/a sequence with the highest "
          "possible number of Pokemon names where the subsequent name starts "
          "with the final letter of the preceding name. No Pokemon name is "
          "to be repeated. \n")
    second_exercise = SecondExercise()
    second_exercise.execute()


if __name__ == '__main__':
    main()
