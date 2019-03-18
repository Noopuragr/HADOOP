--1

A = LOAD '/home/cloudera/ABD/PIG_TEST/sample.txt' USING TextLoader()  AS (Words:chararray);
B = FOREACH A GENERATE FLATTEN (TOKENIZE(*)) ;
C = GROUP B BY $0 ;
D = FOREACH C GENERATE group, COUNT(B) ;
STORE D INTO '/home/cloudera/ABD/PIG_TEST/wordcount1output';


--2


E = FOREACH A GENERATE FLATTEN (TOKENIZE(*)) as word ;

filtered_words= FILTER E by (word =='Prejudice') OR (word == 'the');

grouped = GROUP filtered_words BY word;

wrd_count = FOREACH grouped GENERATE group, COUNT(filtered_words);

STORE wrd_count INTO '/home/cloudera/ABD/PIG_TEST/wordcount2output';



--3

filtered_pride= FILTER E by (word == 'Pride');

grouped_pride = GROUP filtered_pride BY word;

wrd_count_pride = FOREACH grouped_pride GENERATE group, COUNT(filtered_pride);

STORE wrd_count_pride INTO '/home/cloudera/ABD/PIG_TEST/wordcount3output';



