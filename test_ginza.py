import spacy
 
nlp = spacy.load('ja_ginza')
doc = nlp('DOS窓では、基本的には日本語がアウトです')
 
for sent in doc.sents:
    for token in sent:
        print(token.i, token.orth_, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.i)
    print('EOS')