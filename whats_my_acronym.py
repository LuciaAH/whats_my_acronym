def acronym(sentences):
	sentence = sentences.split()
	a = []
	i = 0
	
	while i != len(sentence):
		a.append(sentence[i][0])
		i += 1
	
	word = ''.join(a)
	print(word.upper())
# -------------------------------------
	a = ''
	i = 0

	for i in sentence:
		a += i[0].upper()
	
	print(a)

acronym(input('請輸入英文句子：'))





