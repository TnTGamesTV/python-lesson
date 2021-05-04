from functools import reduce
from pathlib import Path
import re

local_path = Path(__file__).parent.absolute();

with open(local_path.joinpath('Erlkoenig.txt'), 'r', 512, 'utf-8') as input:
    text = input.read();

lower_text = text.lower();
cleaned_text = re.sub("([^\w\säöüß'][ ]*)", ' ', lower_text.replace('\n', ' '));
split_text = cleaned_text.strip().split(" ");

total_count = len(text);
word_count = len(split_text);
father_count = cleaned_text.count('vater');

maximum_word = reduce(lambda max_word, current_word: (max_word, current_word)[len(current_word) > len(max_word)], split_text, "");

output_content = "Anzahl Zeichen: {}\nAnzahl Wörter: {}\nAnzahl Vater: {}\nLängstes Wort: {}".format(total_count, word_count, father_count, maximum_word);

with open(local_path.joinpath('statistik.txt'), 'w', 512, 'utf-8') as output:
    output.write(output_content)