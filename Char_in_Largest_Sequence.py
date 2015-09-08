word = 'aeeefaadfafegaaf'
champCount = 0
contenderCount = 0

print(word)

for x in range (1,len(word)):
	if word[x-1] == word[x]:
		contenderCount += 1
		if contenderCount>champCount:
			champLetter = word[x]
			champCount = contenderCount
	else :
		contenderCount = 0
print('most repeated letter in a sequence is ' + champLetter)
