class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq_counter = Counter()
        for word in words2:
            word_freq_counter = Counter(word)
            for char, freq in word_freq_counter.items():
                max_freq_counter[char] = max(max_freq_counter[char], freq)
        universal_words = []
        for word in words1:
            word_freq_counter = Counter(word)
            is_universal = all(freq <= word_freq_counter[char] for char, freq in max_freq_counter.items())
            if is_universal:
                universal_words.append(word)
        return universal_words
