
def palindrome(s):
	if len(s) <= 1:
		return True

	return s[0] == s[len(s) - 1] and palindrome(s[1: len(s) - 1])

print(palindrome("aabc"))