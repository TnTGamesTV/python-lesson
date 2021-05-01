from functools import reduce

text = "Hallo. Ich bin ein kleiner Blindtext. Und zwar schon so lange ich denken kann. Es war nicht leicht zu verstehen, was es bedeutet, ein blinder Text zu sein: Man ergibt keinen Sinn. Wirklich keinen Sinn. Man wird zusammenhangslos eingeschoben und rumgedreht – und oftmals gar nicht erst gelesen. Aber bin ich allein deshalb ein schlechterer Text als andere? Na gut, ich werde nie in den Bestsellerlisten stehen. Aber andere Texte schaffen das auch nicht. Und darum stört es mich nicht besonders blind zu sein. Und sollten Sie diese Zeilen noch immer lesen, so habe ich als kleiner Blindtext etwas geschafft, wovon all die richtigen und wichtigen Texte meist nur träumen.";

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