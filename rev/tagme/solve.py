
def fatal(s):
	print("Fatal error:", s)
	exit(1)


RING = [None] * 4600
ptr = 0
size = 0

moves = [
	{"chr": 'a', "move": "ns"},
	{"chr": 'b', "move": "jjj"},
	{"chr": 'n', "move": "a"},
	{"chr": 'd', "move": "q"},
	{"chr": 'p', "move": "cor"},
	{"chr": 'f', "move": "gg"},
	{"chr": 's', "move": "aaa"},
	{"chr": 'e', "move": "tt"},
	{"chr": 'j', "move": "gg"},
	{"chr": 'c', "move": "flag"},
]

def get_ring():
	global ptr
	if ptr == size:
		fatal("Dry")
	char = RING[ptr]
	ptr = (ptr + 1) % 4600
	return char


def set_ring(char):
	global size
	RING[size] = char
	size = (size + 1) % 4600
	if size == ptr:
		print('Win')
		exit(0)


def ring_is_empty():
	return size == ptr


def get_move(move):
	for i, m in enumerate(moves):
		if move == m['chr']:
			return i
	return -1


def play():
	if ring_is_empty():
		return 1
	move_idx = get_move(get_ring())
	if move_idx == -1:
		fatal("Bizzare")
	i = 1
	while i <= 1:
		if ring_is_empty():
			return 1
		if get_move(get_ring()) == -1:
			fatal("Bizzarre")
		i += 1
	s = moves[move_idx]['move']
	for j in range(len(s)):
		set_ring(s[j])
	return 0


def print_ring():
	if ptr < size:
		print(RING[ptr:size])
	elif size < ptr:
		print(RING[:ptr] + RING[size:])


def load(s):
	if len(s) > 29:
		fatal("Too long")
	for i in range(len(s)):
		curr = s[i]
		if (i & 1) != 0:
			if i % 6 > 3:
				if curr <= 'p': # curr > 'p'
					fatal(f"Forbidden-1 {i} {curr}")
			elif curr <= 'k' or curr == 's': # curr > 'k' && curr != 's'
				fatal(f"Forbidden-2 {i} {curr}")
		elif curr == 'c' or curr > 'l': # curr != 'c' && curr <= 'l'
			fatal(f"Forbidden-3 {i} {curr}")
		set_ring(curr)


DEBUG = 0
load("ananasananasananasananasana")

mx = 0
print_ring()
while True:
	b = play()
	if DEBUG:
		print_ring()
	else:
		if ptr < size:
			ln = len(RING[ptr:size])
		elif size < ptr:
			ln = len(RING[:ptr] + RING[size:])
	mx = max(mx, ln)
	if b:
		break

print(mx)

# corctf{ananasananasananasananasana}
