# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
POKEMON_LYRICS = 'I wanna be the very best. Like no one ever was. To catch them is my real test. To train them is my cause. I will travel across the land. Searching far and wide. Each Pokemon to understand. The power that\'s inside. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny. (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon. (gotta catch \'em all.) Gotta catch \'em all. Yeah. Every challenge along the way. With courage I will face. I will battle every day. To claim my rightful place. Come with me, the time is right. There\'s no better team. Arm in arm we\'ll win the fight. It\'s always been our dream. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon (gotta catch \'em all.) Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Yeah! (Pokemon, gotta catch \'em all). Its you and me. I know it\'s my destiny. (Pokemon) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you Pokemon. (gotta catch \'em all). Gotta catch \'em all. (Pokemon)'
JIGGLE_JIGGLE = 'You have to have something that sticks. You have to have something that\'s monumental. When you walk out on stage, that\'s been monumental. (Jiggle, jiggle) Can you remember any of the rap that you did? My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. I sip booze from chalices, holding my palaces. Crib is so crampy suckers suffer from paralysis. Rhymes, I write them in the castle. You try to diss me and pretty soon your ass. Will squat in a cell \'cause I can tell you it\'s illegal. Treason, that\'s the reason I\'m regal. You do the time for the crime of lèse-majesté. And **** the police \'cause they can\'t arrest me. (They can\'t arrest me, they can\'t arrest me). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?)'
ALPHABET = 'Now it\'s time for our wrap up. Let\'s give it everything we\'ve got. Ready, begin. Artificial amateurs aren\'t at all amazing. Analytically, I assault, animate things. Broken barriers bounded by the bomb beat. Buildings are broken, basically I\'m bombarding. Casually create catastrophes, casualties. Canceling cats got their canopies collapsing. Detonate a dime of dank daily doin\' dough. Demonstrations, Don Dada on the down low. Eatin\' other editors with each and every energetic. Epileptic episode, elevated etiquette. Furious fat fabulous fantastic. Flurries of funk felt feeding the fanatics. Imitators idolize, I intimidate. In a instant, I\'ll rise in a irate state. Juiced on my jams like jheri curls, jockin\' joints. Justly, it\'s just me, writin\' my journals. Kindly I\'m kindling all kinds of ink on. Karate kick type Brits in my kingdom. Let me live a long life, lyrically lessons is. Learned lame louses just lose to my livery. My mind makes marvelous moves, masses. Marvel and move, many mock what I\'ve mastered.  Niggas nap knowin\' I\'m nice naturally. Knack, never lack, make noise nationally.  Operation, opposition, off, not optional. Out of sight, out of mind, wide beaming opticals. Perfected poem, powerful punchlines. Pummeling petty powder puffs in my prime. Quite quaint quotes keep quiet it\'s Quannum Quarrelers ain\'t got a quarter of what we got, uh. Really raw raps, risin\' up rapidly. Riding the rushing radioactivity. Super scientifical sound search sought. Silencing super fire saps that are soft. Tales ten times talented, they\'re too tough. Take that, challengers, get a tune up. Universal, unique untouched. Unadulterated, the raw uncut. Verb vice Lord victorious valid. Violate vibes that are vain make \'em vanished. Why I\'m all well, would a wise wordsmith. Just weaving up words weeded up, on my work shift. Xerox, my X-ray-diation holes extra large. X-height letters and xylophone tones.'

SHAKE_IT_OFF = "I stay out too late Got nothing in my brain That\'s what people say, mmm-mmm That\'s what people say, mmm-mmm I go on too many dates But I can\'t make them stay At least that\'s what people say, mmm-mmm That\'s what people say, mmm-mmm But I keep cruisingCan\'t stop, won\'t stop moving It\'s like I got this music In my mind Saying, It\'s gonna be alright. Cause the players gonna play, play, play, play, play And the haters gonna hate, hate, hate, hate, hate Baby, I\'m just gonna shake, shake, shake, shake, shake I shake it off, I shake it off Heart-breakers gonna break, break, break, break, break And the fakers gonna fake, fake, fake, fake, fake Baby, I\'m just gonna shake, shake, shake, shake, shake I shake it off, I shake it off I never miss a beat I\'m lightning on my feet And that\'s what they don't see, mmm-mmm That\'s what they don't see, mmm-mmm I\'m dancing on my own (dancing on my own) I make the moves up as I go (moves up as I go) And that\'s what they don\'t know, mmm-mmm That\'s what they don\'t know, mmm-mmm But I keep cruising Can\'t stop, won't stop grooving It\'s like I got this music In my mind Saying, It\'s gonna be alright. 'Cause the players gonna play, play, play, play, play And the haters gonna hate, hate, hate, hate, hate Baby, I\'m just gonna shake, shake, shake, shake, shake I shake it off, I shake it off Heart-breakers gonna break, break, break, break, break And the fakers gonna fake, fake, fake, fake, fake Baby, I\'m just gonna shake, shake, shake, shake, shake I shake it off, I shake it off Shake it off, I shake it off, I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off Hey, hey, hey Just think while you\'ve been getting down and out about the liars and the dirty, dirty cheats of the world, You could\'ve been getting down to this sick beat. My ex-man brought his new girlfriend She\'s \'like Oh, my God!\' but I\'m just gonna shake. And to the fella over there with the hella good hair Won\'t you come on over, baby? We can shake, shake, shake Yeah ohhh Cause the players gonna play, play, play, play, play And the haters gonna hate, hate, hate, hate, hate I'm just gonna shake, shake, shake, shake, shake I shake it off, I shake it off Heart-breakers gonna break, break, break, break, break And the fakers gonna fake, fake, fake, fake, fake Baby, I\'m just gonna shake, shake, shake, shake, shake I shake it off, I shake it off Shake it off, I shake it off, I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off I, I, I shake it off, I shake it off Shake it off, I shake it off, I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off Shake it off, I shake it off, I, I, I shake it off, I shake it off (you've got to), I, I, I shake it off, I shake it off, I, I, I shake it off, I shake it off"
CANT_HOLD_US = "Ay, ay, ay Good to see you, come on in, let's go Yeah, let's go Ha-ha-ha-ha Alright, alright OK, uh, alright, OK Alright, OK Return of the Mack, get up! What it is, what it does, what it is, what it isn't Looking for a better way to get up out of bed Instead of getting on the Internet and checking on who hit me Get up! Thrift shop, pimp-strut walking, little bit of humble, little bit of cautious Somewhere between like Rocky and Cosby. Sweater game, nope, nope y'all can't copy Yup. Bad, moon-walking, this here is our party, my posse's been on Broadway And we did it our way Grown music, I shed my skin and put my bones into everything I record to it And yet I'm on Let that stage light go and shine on down Got that Bob Barker suit game and Plinko in my style Money, stay on my craft and stick around for those pounds But I do that to pass the torch and put on for my town Trust me. On my I-N-D-E-P-E-N-D-E-N-T shit, hustling Chasing dreams since I was fourteen with the four-track bussing Halfway cross that city with the backpack, fat cat, crush shit Labels out here Nah, they can't tell me nothing (Hey, hey, hey) We give that to the people Spread it across the country (Hey, hey, hey) Labels out here Nah, they can't tell me nothing (Hey, hey, hey) We give it to the people Spread it across the country (Hey, hey, hey) Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Nah, can I kick it? Thank you. Yeah I'm so damn grateful I grew up, really wanted gold fronts But that's what you get when Wu-Tang raised you Y'all can't stop me, go hard like I got a 808 in my heart beat And I'm eating at the beat like you give a little speed to a great white shark on Shark Week Raw. Time to go off. I'm gone Deuces goodbye. I got a world to see, and my girl she wanna see Rome Caesar'll make you a believer Nah I never ever did it for a throne That validation comes from giving it back to the people Nah sing this song and it goes like 'Raise those hands, this is our party We came here to live life like nobody was watching' I got my city right behind me If I fall, they got me Learn from that failure gain humility and then we keep marching. I said Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us And so we put our hands up And so we put our hands up Wa oh oh oh wa oh oh oh wa oh oh Let's go! Na na na na na na na na (aha) Hey And all my people say Na na na na na na na na (that's right, feels good) Hey And all my people say Na na na na na na na na (it's alright) (Oh oh oh oh oh oh oh oh) And all my people say Na na na na na na na na Mack-le-le-le-le-le-more Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us Can we go back? This is the moment Tonight is the night, we'll fight 'til it's over So we put our hands up like the ceiling can't hold us Like the ceiling can't hold us"
CURE_FOR_ME = "I run from the liars The fuel on the fire I know I created myself I know I can't fight The sad days and bad nights But I never asked for your help You got hurt No, we don't belong together So you took the love from my arms Into the arms of yours But I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it No, I don't need a cure for me I don't like the tension The misapprehensions About our nature in love The glorious teachers Are no use for creatures Who knows how to play with the gods? You got nerves but they never show Unless they hurt, so you blamed it all On my love, the moving Heart I got But I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it No, I don't need a cure for me I don't need it I don't need it Please, no cure for me Please, no cure for me Cure for me Cure for me Please, no cure for me Cure for me Please, no cure for me Cure for me Cure for me (And you need to know I don't need it) I don't need it (And you should know) I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me (And you need to know I don't need it) I don't need it (And you should know) No, I don't need a cure for me"

# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

SAILOR_MOON = 'I swear by the moon and the stars in the sky, I\'ll be there to make you shine.'
AVATAR_INTRO = 'Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, an airbender named Aang, and although his airbending skills are great, he has a lot to learn before he\'s ready to save anyone. But I believe Aang can save the world.'
PLEDGE_OF_ALLEGIANCE = "I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all."

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

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


    # STEP 0
    ## defining our data structures
    ## defining operations
    class Node: # NOT given to students
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
        if v.letter != None: 
            coding[v.letter] = path 
        else:
            retrieve_codes(v.left, path + '0') 
            retrieve_codes(v.right, path + '1') 

    # STEP 1
    ## counting the frequencies
    for letter in message:
        if letter not in freq:
            freq[letter] =1
        else:
            freq[letter] += 1

    # STEP 2
    ## initialize the nodes
  
    for letter, count in freq.items():
        single_node = Node(letter, count, l=None, r=None)
        nodes.append(single_node)

    # STEP 3
    ## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
        ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

        ## get the first min
        min_a: Node = nodes.pop()

        ## get the second min
        min_b: Node = nodes.pop()

        ## combine the two
        combined: Node = Node(letter= None, w=min_a.weight+min_b.weight, l = min_a, r= min_b) 

        ## put the combined nodes back in the list of nodes
        nodes.append(combined)

    # STEP 4
    ## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    for letter in message:
        result += coding[letter]

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Freije Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)


# PLOT 1
## POKEMON
# ratios: list = list()
# data = POKEMON_LYRICS
# for i in range(1, len(data)):
#     sub_message = POKEMON_LYRICS[0:i]
#     _, _, ratio = huffman(sub_message)
#     ratios.append(ratio)

# plt.plot(ratios[:MAX_N], color='red', label= "Pokemon",  linestyle ="-.")

# ## JIGGLE JIGGLE
# ratios: list = list()
# data = JIGGLE_JIGGLE
# for i in range(1, len(data)):
#     sub_message = JIGGLE_JIGGLE[0:i]
#     _, _, ratio = huffman(sub_message)
#     ratios.append(ratio)

# plt.plot(ratios[:MAX_N], color='green', label= "Green",  linestyle ="-.")

# ## ALPHABET
# ratios: list = list()
# data = ALPHABET
# for i in range(1, len(data)):
#     sub_message = ALPHABET[0:i]
#     _, _, ratio = huffman(sub_message)
#     ratios.append(ratio)

# plt.plot(ratios[:MAX_N], color='blue', label= "Al",  linestyle ="-.")
# plt.legend()


ratios: list = list()
data = CANT_HOLD_US
for i in range(1, len(data)):
    sub_message = CANT_HOLD_US[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios[:MAX_N], color='orange', label= "Can't Hold Us Now",  linestyle ="-.")

ratios: list = list()
data = SHAKE_IT_OFF
for i in range(1, len(data)):
    sub_message = SHAKE_IT_OFF[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios[:MAX_N], color='purple', label= "Shake it Off",  linestyle ="-.")

ratios: list = list()
data = CURE_FOR_ME
for i in range(1, len(data)):
    sub_message = CURE_FOR_ME[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios[:MAX_N], color='green', label= "Cure for Me",  linestyle ="-.")
plt.legend()


# PLOT 2
plt.subplot(2, 1, 2)

ratios: list = list()
data = SAILOR_MOON
for i in range(1, len(data)):
    sub_message = SAILOR_MOON[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios[:MAX_N], color='red', label= "Sailor Moon",  linestyle ="-.")


ratios: list = list()
data = PLEDGE_OF_ALLEGIANCE
for i in range(1, len(data)):
    sub_message = PLEDGE_OF_ALLEGIANCE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios[:MAX_N], color='green', label= "Pledge of Allegiance",  linestyle ="-.")


ratios: list = list()
data = AVATAR_INTRO
for i in range(1, len(data)):
    sub_message = AVATAR_INTRO[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios[:MAX_N], color='blue', label= "Avatar Intro",  linestyle ="-.")
    

plt.xlabel("Length of Message")
plt.ylabel("Compression %")
plt.legend()
plt.savefig("./figs/lab7_Freije.png")
plt.show()