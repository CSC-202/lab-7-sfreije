For your (i) songs and (ii) mantras, how can you describe compression performance from Huffman?

"Can't Hold Us" was my longest song and was my choice for a rap song. Despite its length and wide variety of words this song was the fastest to initially compress since the introduction of the song is very repetitive with only simple words, making the initial tree very short. Later on, this song had a very similar final compression percentage to "Cure for Me", even though "Cure for Me" was only about half its length. This is likely because the songs had a similar number of unique vocab words and characters. Finally for the last song I chose one of the most repetitive pop songs I could think of, “Shake it Off”. This song had the best final compression percentage, mostly likely because of its continuous redundancy even outside of the chorus. In general, more repetitive messages will have more efficient compressions especially considering the words that are repeated often have shorter codes. These shorter codes result in faster searching and will likely have shorter trees with better compression percentages. 
Furthermore, songs with a smaller number of characters will have faster compression times because huffman trees have a time complexity of O(nlogn) where n = number of unique letters. This is why the other two songs had worse compression rates because they had a wider variety of symbols.


The Sailor Moon quote was the shortest mantra by far, and had the smallest tree since it had very few characters. Its short size in combination with the fact that it had less unique letters compared to the other mantras, allowed it to have the highest final compression percentage. Next, even though the Avatar introduction was longer than the Pledge of Allegiance, the two had very similar final compression rates. Both had a similar frequency of unique words and very little repetition. For the pledge, the only words repeated are "to" and "the" so every word had a different code of varying length. Then, although not by much, the Avatar intro had slightly more words repeated which helped compensate for its longer length and resulted in nearly identical final compression percentages between Avatar and the Pledge.






