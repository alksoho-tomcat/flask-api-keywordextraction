import json
import threading
from keywordextraction import keywords_extraction
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify, make_response, request, Response


app = Flask(__name__)
# 文字化け防止
app.config['JSON_AS_ASCII'] = False 


@app.route('/post', methods=['POST'])
def post_json():
  json = request.get_json()  # Get POST JSON
  BODY = json['body']

  # スレッド実行プールを作成
  pool = ThreadPoolExecutor(max_workers = 1)
  # スレッド実行
  future = pool.submit(keywords_extraction, BODY)
  # スレッドの戻り値取得
  result_keywords = future.result()

  result =  {
    "data": {
      "resutl":result_keywords 
      }
    }
  return jsonify(result) 

if __name__ == "__main__":
  app.run()

# テストコマンド
#  curl -X POST -H "Content-Type: application/json" -d '{"body":"吾輩は猫である。名前はまだない。飼い主はそこらへんの小作農だ。"}' http://localhost:5000/post


