class Solution(object):
	def fullJustify(self, words, maxWidth):
		start = end = 0
		result, curr_words_length = [], 0
		for i, word in enumerate(words):
			if len(word) + curr_words_length + end - start > maxWidth:
				if end - start == 1:
					result.append(words[start] + ' ' * (maxWidth - curr_words_length))

				else:
					total_space = maxWidth - curr_words_length
					space, extra = divmod(total_space, end - start - 1)
					for j in range(extra):
						words[start + j] += ' '
					result.append((' ' * space).join(words[start: end]))
				curr_words_length = 0
				start = end = i
			end += 1
			curr_words_length += len(word)
		result.append(' '.join(words[start:end]) + ' ' * (maxWidth - curr_words_length - (end - start - 1)))
		