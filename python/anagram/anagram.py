def find_anagrams(word, candidates):
    return [candidate
            for candidate in candidates
            if sorted(candidate.lower()) == sorted(word.lower())
            if candidate.lower() != word.lower()]
