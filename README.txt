Part 1:

To prepare the file for parsing it to find the type-token ratio, I simply copied and pasted the HTML file into a plain text file and removed the title, table of contents, and chapter titles. 

The required libraries for this are Counter from the collections library (to calculate the number of instances of each word) and the codecs library (to parse through the text file bypassing any encoding errors).

This function requires no file name input, and just requires running the function find_ttr(). The function uses block sizes of 1000 words to calculate the TTR, based on the method used in the van Velzen and Garrard paper, “From hindsight to insight – retrospective analysis of language written by a renowned Alzheimer's patient”. 


Part 2:

Rubric 

30%: Use of quotes/textual evidence. Based on having at least three quotes per paragraph.
25% Type-token ratio. 
15% Use of strong vs. weak words. Score decreases with a higher use of weak words (adjectives, nouns, and verbs). The grade depends on the ratio of weak words to total words in the paragraph. 
15% Paragraph length. Based on an ideal length of 5-10 sentences. The score is dependent on the deviation from this length, which is calculated by and depends on if the paragraph contains either fewer than 5 or more than 10 sentences. 
15% Use of active voice vs. passive voice. Score is negatively impacted by the use of the passive voice. Based on ratio of uses of the passive voice to the number of sentences in the paper. 

The required libraries for this are codecs, the sent_tokenize function from NLTK, spaCy, the Counter function from the collections library, and a list of weak words, which I found at http://students.washington.edu/adelak/wordpress/wp-content/uploads/2017/09/weak_words.txt. 

My rubric is meant to grade essays that involve close textual readings, such as essays for literature or history classes. 

The format_text function uses spaCy to create a list of tokens, which I will need in order to use spaCy’s dependency finder in the passive_voice function.  

The first category of my rubric is the use of quotes, which is a crucial aspect of close readings. This makes up the largest portion of the essay grade. In previous classes, I have been told that a paragraph should not have less than three direct quotes. The function parses through each paragraph and counts the number of quotes, based on the presence of an opening parentheses (‘(‘). I decided to use this because it corresponds to an in-text citation, whereas I often use quotation marks in my essays to format titles, which should not be counted as a quote. I also exclude the introduction and conclusion from the grade for this portion of the rubric. For each paragraph that does not contain at least 3 quotes, I deduct 30% of the 30 points. However, I anticipate that this might cause problems, particularly if parentheses are used outside of an in-text citation. The essays I have run through the program aren’t affected by this because they don’t contain other parentheses, but I would like to find a better way to identify quotations that understands the difference between titles and textual evidence. I would also like to make the function more robust by changing the score in relation to how many fewer quotes than 3 there are. 

The second category of my rubric is the type-token ratio. I chose a block size of 500 words, given that essays are usually between 5 and 10 pages, or around 2000-4000 words. The TTR counts for 25% of the grade, as using varied language is important for an engaging essay, and it demonstrates linguistic maturity. I calculate a score for each 500-word block based on the TTR. If it is over 0.5, I give full credit (a score of 1). If it is between 0.4 and 0.5, I give 80%, and if it is below 0.4, I give 60%. I could not find information on what a good TTR is, so I based this criteria on what I have seen when going through my papers. 

The third category, which counts for 15% of the grade, is the use of strong words vs. weak words. In Orwell’s essay, on page 132, he talks about meaningless words and the importance of only using words that add richness to the argument. So, I found a text file that lists weak verbs, nouns, and adjectives (cited above). In this function, I parse through each paragraph and find the number of weak words used. I calculate a score for each paragraph based on the ratio of weak words to total words in the paragraph, and add each score to find the average score, which is dependent on the number of paragraphs in the essay. 

The fourth category in my rubric, which counts for 15% of the grade, is the paragraph length. I decided this based on Orwell’s essay, which states the importance of cutting out unnecessary words (and therefore decreasing length). I used the sent_tokenize function from NLTK to break each paragraph into sentences. I gave a broad range (between 5 and 10 sentences) for this category, given that the number of sentences in a paragraph will depend on the length of the essay. Because there is no exact answer for how long a paragraph should be, I thought this range was appropriate. However, I anticipate there being some problems with the difference in an introduction and/or conclusion paragraph, which I could have accounted for by excluding them from the overall grade. However, I did try to account for the 5 sentence range by calculating the score differently based on whether the paragraph was under 5 sentences or over 10. The function calculates the deviation from either 5 or 10 sentences. If the paragraph is between 5 and 10 sentences, the author receives full credit. I then calculate the average score over all the  paragraphs. 

The last category, also worth 15%, is the use of the passive voice, which is typically frowned upon in non-scientific writing. Orwell mentions on page 139 of his essay that a writer should never use the passive voice. I call the format_text function to clean the essay, since I need lowercase words and words without punctuation to identify the passive voice. I used spaCy’s .dep_ method to find all words marked with a “nsubjpass” dependency, meaning that it is an instance of the passive voice. To calculate the score, I find the ratio of the number of uses of the passive voice in relation to the number of sentences in the essay. 

The final grade_paper function can take a list of file names, denoted by the variable-length-positional args list. I first use open() to create a new file called ‘grades.txt’, in which the function will write the paper title and grade. For each paper listed in the function call, I call the 5 scoring functions, add each of the 5 scores, and multiply by 100 to get a grade out of 100. Using write(), the function writes the paper’s title and the corresponding score (with 2 decimal places) to grades.text. After it loops through all the files, it closes grades.txt.


