import nltk
import pke
from spacy.lang.ja import stop_words
 
# ファイルパス
file_path = "news.txt"
 
# 日本語のストップワードを設定
# これではエラーが出る
# pke.base.lang_stopwords['ja_ginza'] = 'japanese'
pke.lang.stopwords['ja_ginza'] = 'japanese'
 
# テキストの読み込み
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()
 
    # NLTKの処理
    stopwords = list(stop_words.STOP_WORDS)
    nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
    nltk.corpus.stopwords.words = lambda lang: stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_org(
        lang)
 
    # pkeの処理
    extractor = pke.unsupervised.MultipartiteRank()
	
	# 下記ではERROR:root:No spacy model for 'ja_ginza' language.とエラーが出る
	# extractor.load_document(input=text, language='ja_ginza', normalization=None)

    extractor.load_document(input=text, language='ja', normalization=None)
    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
    extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)
 
    # 結果表示（上位10）
    result = extractor.get_n_best(n=10)
    print(type(result))
    for value in result:
    	
    	# 単語を成形したタプルを生成
    	keywords = value[0].replace(' ','')
    	out_value = (keywords, value[1])

    	print(out_value)