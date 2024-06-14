def find_bridge(words, word_1, word_2):
    pre_to_bhd = {}
    bhd_to_pre = {}

    for node in words:
        pre, bhd = node['pre'], node['bhd']
        if pre not in pre_to_bhd:
            pre_to_bhd[pre] = []
        pre_to_bhd[pre].append(bhd)

        if bhd not in bhd_to_pre:
            bhd_to_pre[bhd] = []
        bhd_to_pre[bhd].append(pre)

    if word_1 not in pre_to_bhd or word_2 not in bhd_to_pre:
        return 'No word1 or word2 in the graph'

    bridge_words = []
    for intermediate in pre_to_bhd[word_1]:
        if intermediate in bhd_to_pre[word_2]:
            bridge_words.append(intermediate)

    if not bridge_words:
        return 'No bridge words from word1 to word2!'
    elif len(bridge_words) == 1:
        return f'The bridge word from {word_1} to {word_2} is {bridge_words[0]}'
    else:
        return f'The bridge words from {word_1} to {word_2} are {", ".join(bridge_words)}.'

