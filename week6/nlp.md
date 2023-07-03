# NLP (Natural Language Processing)
AI에서 중요한 필드임. 자연어를 통해 사람과 컴퓨터가 상호작용하는 걸 해결한다.
NLP의 궁극적인 목적은 인간의 언어를 유용한 방식으로 읽고, 해독하고. 이해하는 것에 있다.

1. Text Cleaning and PreProcessing
대/소문자를 통일하고 특수문자, 숫자 등을 제거.
이 단계에서의 목표는 텍스트의 뜻을 이해하는데 있어 필요없는 정보를 제거하는 것이다.
(그렇다고 무지성으로 대소문자 통일하고 한다는게 아니라, 이걸 기게어로 변환하던가 하는 듯)

2. Tokenization
주어진 텍스트를을 개별 단어 혹은 절로 쪼갠다. 이 쪼개진 각각의 단어/절을 토큰이라고 한다. 

3. Stop words removal 
`Stop words`란 'is', 'the' 등 텍스트의 뜻을 이해하는데 별로 유용하지 않은 일반적인 단어들을 의미한다.

4. Stemming and Lemmatization (어간, 형태소)
두 처리 과정 모두 단어의 굴절 형태를 공통 기본 형태로 줄이는 것을 목표로 한다.
(e.g. running > run)
단, stemming(어간화)은 실제 단어가 아닌 단어를 생성할 수 있는 반면, lemmatization(형태소화)은 항상 실제 단어를 생성한다.

5. Word Embeddings/Text vectors
Word embedding은 텍스트를 벡터 형태로 표현하는 것이다. 
유사한 단어는 벡터 사이에 최소한의 거리를 둔다는 것이 핵심.
word embedding에 사용되는 모델로는 Word2Vec, GloVe가 있다.

6. Bag of Words, TF-IDF
벡스트 데이터를 숫자 벡터로 변환하는 method이다. Bag of Words는 문서에서 각 단어의 출현 횟수를 계산한다.
TF-IDF는 다른 모든 문서와 비교해 문서에서 용어의 중요도를 고려한다.

7. Sequence Models like RNN, LSTM, GRU
시계열 데이터를 다룰 때 효과적인 특수한 타입의 신경망 네트워크이다.
NLP task에 널리 사용되는데, 이는 이전의 정보를 기억해야 하기 때문.

8. Transformer Models
약간 더 최신의 모델로 `Attention is All You need` 논문에서 소개되었다.
이 개념은 GPT(Generative Pre-trained Transformer, 생성형 사전 학습 트랜스포머) 및 
BERT (Bidirectional Encoder Representations from Transformers, 양방향 인코더 표현)와 같은
모델의 기반이 되는 개념이다. 자연어 처리에서 매우 효과적인 모델..

9. NLP Libraries
NLP 작업을 위해 사용할 수 있는 몇 가지 라이브러리가 있음.
e.g. NLTK, Gensim, Spacy, Transformer lib (by Hugging Face) 등..

10. Applications of NLP
감정 분석, 언어 번역, 텍스트 요약 등이 포함되어 있다.