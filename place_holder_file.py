#place holder file


#if this did accidently end up being submitted please ignore this

#make super secret  in spotifify from super secret elsewhere?
#python 3 main.py "playlist link?"
#track should have stuff for artist id, album idea, name, albumn, etc.

import numpy as np
xval:list = np.arange(1,MAX_N)

# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0 - TODO
## defining our data structures
class Node: # NOT given to students
    # TODO
    weight: int
    left: any
    right: any
    letter: str
    
    def __init__(self, letter, w, l,r):
        self.letter = letter
        self.weight = w
        self.left = l
        self.right = r

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None: # if 'TODO': # TODO
        coding[v.letter] = path # TODO
    else:
        retrieve_codes(v.left, path + '0') # TODO
        retrieve_codes(v.right, path + "1") # TODO

# STEP 1
## counting the frequencies - TODO
for letter in message:
    if letter not in freq.keys():
        freq[letter] =1
    else:
        freq[letter] += 1

# STEP 2
## initialize the nodes - TODO
nodes = list()
nodes.append(Node(0, 'a'))

# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined: Node = None # TODO

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
result: str = str() # TODO (hint coding[letter] -> code)

# for letter, code in coding.items():
#     print(letter, ":", code)
#     result += code

# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')



HOBBIT = "And people will say: ‘Let’s hear about Frodo and the Ring!’ And they’ll say: ‘Yes, that’s one of my favorite stories. Frodo was very brave, wasn’t he dad?’ ‘Yes, my boy, the famousest of the hobbits, and that’s saying a lot."

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Freije Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = POKEMON_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = JIGGLE_JIGGLE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = ALPHABET[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = SITH_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = GREEN_LATTERN[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = JEDI_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)



    yep = "Ay, ay, ay Good to see you, come on in, let's go Yeah, let's go Ha-ha-ha-ha Alright, alright OK, uh, alright, OK Alright, OK Return of the Mack, get up! What it is, what it does, what it is, what it isn't Looking for a better way to get up out of bed Instead of getting on the Internet and checking on who hit me Get up! Thrift shop, pimp-strut walking, little bit of humble, little bit of cautious Somewhere between like Rocky and Cosby. Sweater game, nope, nope y'all can't copy Yup. Bad, moon-walking, this here is our party, my posse's been on Broadway And we did it our way Grown music, I shed my skin and put my bones into everything I record to it And yet I'm on Let that stage light go and shine on down Got that Bob Barker suit game and Plinko in my style Money, stay on my craft and stick around for those pounds But I do that to pass the torch and put on for my town Trust me. On my I-N-D-E-P-E-N-D-E-N-T shit, hustling Chasing dreams since I was fourteen with the four-track bussing Halfway cross that city with the backpack, fat cat, crush shit Labels out here Nah, they can't tell me nothing (Hey, hey, hey) We give that to the people Spread it across the country (Hey, hey, hey) Labels out here Nah, they can't tell me nothing (Hey, hey, hey) We give it to the people Spread it across the country (Hey, hey, hey) Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Nah, can I kick it? Thank you. Yeah I'm so damn grateful I grew up, really wanted gold fronts But that's what you get when Wu-Tang raised you Y'all can't stop me, go hard like I got a 808 in my heart beat And I'm eating at the beat like you give a little speed to a great white shark on Shark Week Raw. Time to go off. I'm gone Deuces goodbye. I got a world to see, and my girl she wanna see Rome Caesar'll make you a believer Nah I never ever did it for a throne That validation comes from giving it back to the people Nah sing this song and it goes like "Raise those hands, this is our party We came here to live life like nobody was watching" I got my city right behind me If I fall, they got me Learn from that failure gain humility and then we keep marching. I said Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us And so we put our hands up And so we put our hands up Wa oh oh oh wa oh oh oh wa oh oh Let's go! Na na na na na na na na (aha) Hey And all my people say Na na na na na na na na (that's right, feels good) Hey And all my people say Na na na na na na na na (it's alright) (Oh oh oh oh oh oh oh oh) And all my people say Na na na na na na na na Mack-le-le-le-le-le-more Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us"

    yep2 ="I run from the liars The fuel on the fire I know I created myself I know I can't fight The sad days and bad nights But I never asked for your help You got hurt No, we don't belong together So you took the love from my arms Into the arms of yours But I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it No, I don't need a cure for me I don't like the tension The misapprehensions About our nature in love The glorious teachers Are no use for creatures Who knows how to play with the gods? You got nerves but they never show Unless they hurt, so you blamed it all On my love, the moving Heart I got But I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it I don't need it Please, no cure for me Please, no cure for me Cure for me Cure for me Please, no cure for me Cure for me Please, no cure for me Cure for me Cure for me (And you need to know I don't need it) I don't need it (And you should know) I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me"