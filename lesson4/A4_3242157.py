from functools import reduce

text = input("Eingabe: ");

lower_text = text.lower();
split_text = text.split(" ");

total_count = len(text);
word_count = len(split_text);
and_count = lower_text.count('und');

maximum_word = reduce(lambda max_word, current_word: (max_word, current_word)[len(current_word) > len(max_word)], split_text, "");

print("Anzahl Zeichen: {}".format(total_count));
print("Anzahl Wörter: {}".format(word_count));
print("Anzahl und: {}".format(and_count));
print("Längstes Wort: {}".format(maximum_word));