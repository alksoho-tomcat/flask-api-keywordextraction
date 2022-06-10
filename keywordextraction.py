import nltk
import pke
from spacy.lang.ja import stop_words
 
 
# 日本語のストップワードを設定
# これではエラーが出る
# pke.base.lang_stopwords['ja_ginza'] = 'japanese'
pke.lang.stopwords['ja_ginza'] = 'japanese'
 
# テキストの読み込み
def keywords_extraction(input_text):
    text = input_text
 
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

    out_result = []

    for value in result:
        
        # 単語を成形したタプルを生成
        keywords = value[0].replace(' ','')
        out_value = (keywords, value[1])
        out_result.append(out_value)


    return out_result


# テストコマンド
#  curl -X POST -H "Content-Type: application/json" -d '{"body":"吾輩は猫である。名前はまだない。飼い主はそこらへんの小作農だ。"}' http://localhost:5000/post

