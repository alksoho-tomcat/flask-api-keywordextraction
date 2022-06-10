import MeCab
from yake import KeywordExtractor

m = MeCab.Tagger("-Ochasen")

def sep_by_mecab(text):
     return " ".join([t.split("\t")[0] for t in m.parse(text).split('\n')][:-2])

def text_pretrained(text):
    array_text = []
    for line in text.split("\n"):
        if len(line) == 0:
            continue
        sp_text = sep_by_mecab(line)
        array_text.append(sp_text)
    return "\n".join(array_text).replace("。", ".").replace("、", ",")




# 本記事の文章を貼り付け
text = f"""
内閣不信任案、否決へ　午後採決、終盤国会攻防ヤマ場
衆院は9日午後の本会議で、立憲民主党が提出した岸田内閣に対する不信任決議案と細田博之衆院議長への不信任決議案を採決する。いずれも与党などの反対多数で否決される見通しだ。参院選をにらんだ今国会最終盤の与野党攻防は大きなヤマ場を迎えた。

【写真】衆院事務総長に岸田内閣に対する不信任決議案を提出する立憲民主党の西村幹事長ら＝8日午後

　本会議に先立ち、自民党の高木毅国対委員長は政権運営や国会運営に関し「何ら瑕疵はなく、不信任には当たらない」などと記者団に主張。「一致結束して否決する」と語った。立民の小川淳也政調会長は記者会見で「相当数の国民が不安や不満を持っているのは事実だ。代弁する責任がある。岸田文雄首相や細田氏に反省してもらう重要な機会だ」と訴えた。
.
.
.
"""

print(sep_by_mecab(text))
print("\n")
print(text_pretrained(text))


kw_extractor = KeywordExtractor(lan="ja", n=3, top=10)
keywords = kw_extractor.extract_keywords(text=text_pretrained(text))
print(keywords)