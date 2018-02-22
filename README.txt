The required libraries for this are Counter from the collections library and the codecs library.

This function requires no file name input, and just requires running the function find_ttr(). The function uses block sizes of 1000 words to calculate the TTR, based on the method used in the van Velzen and Garrard paper, “From hindsight to insight – retrospective analysis of language written by a renowned Alzheimer's patient”. 

Rubric 

30%: Use of quotes/textual evidence. Based on having at least three quotes per paragraph.
25% Type-token ratio. 
15% Use of strong vs. weak words. Score decreases with a higher use of weak words (adjectives, nouns, and verbs). The grade depends on the ratio of weak words to total words in the paragraph. 
15% Paragraph length. Based on an ideal length of 5-10 sentences. The score is dependent on the deviation from this length, which is calculated by and depends on if the paragraph contains either fewer than 5 or more than 10 sentences. 
15% Use of active voice vs. passive voice. Score is negatively impacted by the use of the passive voice. Based on ratio of uses of the passive voice to the number of sentences in the paper. 

The required libraries for this are codecs, the sent_tokenize function from NLTK, spaCy, the Counter function from the collections library, and a list of weak words, which I found at http://students.washington.edu/adelak/wordpress/wp-content/uploads/2017/09/weak_words.txt. 

My rubric is meant to grade essays that involve close textual readings, such as essays for literature or history classes. 

