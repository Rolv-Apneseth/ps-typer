# rolvs-typing-speedtest
 A program to test the speed at which you can type. Choose a difficulty, type out the word, sentence or paragraph and be told how long you took to do it and your average w.p.m. The program will also keep track of your daily and overall highscores.

 Gui built using pyqt5.

 To start the program, run main.py.

 On startup, you can choose your difficulty, then press begin.

What you will type with each difficulty (randomly chosen from a list for each):
    Easy - One common English word
    Medium - One common English phrase/expression
    Hard - A paragraph from a book or a famous quotation (varying in length)

To be given a different word/sentence/paragraph on each difficulty screen, click the restart button. This will also restart your timer.

Your w.p.m. is worked out using (characters typed/5)/minutes so that larger words will not count the same as small words. However, this also means it will not necessarily be easier to get highscores by choosing the easiesty difficulty.

Your highscores are stored in today.txt and highscore.txt (generated on startup if they don't exist) so to reset your highscores, simply delete those files.

