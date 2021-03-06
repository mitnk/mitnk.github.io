"Code" is a book [1] about how computers work. It can answer some question like "What's the difference between storage and memory?", "Why can't you run Linux programs under Windows?", and answer them not in some abstract way, but with a depth that just might even rival that of electrical engineers and programmers. It's not as hard as most people might think.

Although computers today are more complex than the computers of 25 years ago, they are still fundamentally the same. In this book, the word code usually means a system for transferring information among people and machines.

Chapter 1. Best Friends
--------------------

... So you first devise a simple technique. Each letter of the alphabet corresponds to a series of flashlight blinks. An A is 1 blink, a B is 2 blinks, a C is 3 blinks, and so on to 26 blinks for Z. The word BAD is 2 blinks, 1 blink, and 4 blinks with little pauses between the letters so you won't mistake the 7 blinks for a G. You'll pause a bit longer between words.

Morse code, you have two kinds of blinks -- Dots and Dashes.

![code notes image](/site_media/images/article/2012/code001.png)

Although Morse code has absolutely nothing to do with computers, becoming familiar with the nature of codes is an essential preliminary to achieving a deep understanding of the hidden languages and inner structures of computer hardware and software. 

The simpler and shorter codes are assigned to the more frequently used letters of the alphabet, such as E and T. The less common letters, such as Q and Z have long codes. Almost everyone knows SOS, the international distress signal. It isn't an abbreviation for anything -- it's simply an easy-to-remember Morse code sequence.

The key word here is two. Two types of blinks, two vowel sounds, two different anything, really, can with suitable combinations convey all types of information.

Chapter 2. Codes and Combinations
-------------------------------

A better approach to organizing Morse codes might be to group them depending on how many dots and dashes they have. Contains either one dot or one dash can represent only two letters, E and T.

![code notes image](/site_media/images/article/2012/code002.png)

A combination of exactly two dots or dashes gives us four more letters -- I,  A, N, and M.

![code notes image](/site_media/images/article/2012/code003.png)

A pattern of three dots or dashes gives us eight more letters.

![code notes image](/site_media/images/article/2012/code004.png)

And finally (if we want to stop this exercise before dealing with numbers and punctuation marks), sequences of four dots and dashes give us 16 more characters.

![code notes image](/site_media/images/article/2012/code005.png)

Each of the four tables has twice as many codes as the table before it. The letter numbers of these tables are 2^1, 2^2, 2^3, and 2^4. To make the process of decoding Morse code even easier, we might want to draw something like the big treelike table:

![code notes image](/site_media/images/article/2012/code006.png)

To decode a particular sequence, follow the arrows from left to right. This table assured of using all the possible codes without making the sequences of dots and dashes unnecessarily long. To include all the punctuation marks, the system must be expanded to six dots and dashes, which gives us 2 + 4 + 8 + 16 + 32 + 64, or 126, characters. That's overkill for Morse code, which leaves many of these long codes "undefined".

What we're doing by analyzing binary codes is a simple exercise in the branch of mathematics knows as combinatorics or combinatorial analysis. Traditionally, combinatorial analysis is used most often in the fields of probability and statistics because it involves determining the number of ways that things, like coins and dice, can be combined. But it also helps us understand how codes can be put together and taken apart.

Chapter 3. Braille and Binary Codes
-------------------------------

Samuel Morse wasn't the first person to successfully translate the letters of written language to an interpretable code. Nor was he the first person to be remembered more as the name of his code than as himself. That honor must go to a blind French teenager born some 18 years after Samuel Morse but who made his mark much more precociously. Little is known of his life, but what is known makes a compelling story.

In Braille, every symbol used in normal written language is encoded as one or more raised dots within a two-by-three cell. The dots of the cell are commonly numbered 1 through 6.

![code notes image](/site_media/images/article/2012/code007.png)

What should be interesting to us is that the dots are binary. the total number of combinations of 6 flat and raised dots is 2^6, or 64. Here they are -- all 64 possible Braille codes:

![code notes image](/site_media/images/article/2012/code008.png)

To begin dissecting the code of Braille, let's look at the basic lowercase alphabet.

![code notes image](/site_media/images/article/2012/code009.png)

For example, the phrase "you and me" in Braille looks like this:

![code notes image](/site_media/images/article/2012/code010.png)

At this point, only 25 of 64 possible codes have been accounted for. Here are some pattern: the first row uses only the top four spots and the second row duplicates the first row except that dot 3 is also raised, the third row is the same except that dots 3 and 6 are raised.

Since the days of Louis Braille, the Braille code has been expanded in various ways. The one used most often in English is called Grade 2 Braille. It uses many contractions in order to save trees and to speed reading.

![code notes image](/site_media/images/article/2012/code011.png)

So far, We've described 31 codes. In Grade 2 Braille, as we shall see, nothing is wasted.

Contractions of letters within a words as well as the letter `w`.

![code notes image](/site_media/images/article/2012/code012.png)

Second, we can take codes for some punctuation marks and contractions, depending on context:

![code notes image](/site_media/images/article/2012/code013.png)

We're up to 51 codes so far. Here are some for contractions and some additional punctuation:

![code notes image](/site_media/images/article/2012/code014.png)

The code for "ble" is very important because when it's not part of word, it means that the code following should be interpreted as numbers.

![code notes image](/site_media/images/article/2012/code015.png)

Now only 7 codes left. They are using for some indicators.

![code notes image](/site_media/images/article/2012/code016.png)

[1] [http://book.douban.com/subject/1494026/](http://book.douban.com/subject/1494026/)

(つづく)