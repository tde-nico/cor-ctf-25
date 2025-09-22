def encode(arr, text, wordlist, key):
	v4 = wordlist[key]
	arr.append(v4)
	for i in range(len(text)):
		v9 = key ^ ord(text[i])
		if v9 >= len(wordlist):
			exit(1)
		v5 = wordlist[v9]
		arr.append(v5)
		key ^= i ^ v9
	return arr

def decode(arr, wordlist):
	res = []
	key = wordlist.index(arr[0])
	for i in range(1, len(arr)):
		v9 = wordlist.index(arr[i])
		v5 = key ^ v9
		if v5 >= 256:
			exit(1)
		res.append(chr(v5))
		key ^= (i - 1) ^ v9
	return res

with open('rockyou.txt', 'r') as f:
	wordlist = f.read().splitlines()

with open('encoded.rj', 'r') as f:
	result = f.read().strip().split('\n')[0].split(' ')

print(''.join(decode(result, wordlist)))

# corctf{r0cky0u_3nc0d1ng_r0cks}
