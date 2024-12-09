def single_root_words(root_word, *other_words):
    roots_word_lower = root_word.lower()
    same_words = []
    for i in other_words:
        k = i.lower()
        if roots_word_lower in k or k in roots_word_lower:
            same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)