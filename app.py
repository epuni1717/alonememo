from flask import Flask, render_template, request

# 플라스크 웹 서버 생성하기
app = Flask(__name__)


# API 추가
@app.route('/', methods=['GET'])    # 데코레이터 문법
def index():   # 함수 이름은 고유해야 한다
    return render_template('index.html', test='테스트')


# app.py 파일을 직접 실행시킬 때 동작시킴
# 이 코드가 가장 아랫부분
if __name__ == '__main__'
    app.run(
        '0.0.0.0',  # 모든 IP에서 오는 요청을 허용
        7000,  # 플라스크 웹 서버는 7000번 포트 사용
        debug=True,  # 에버 발생 시 에러 로그 보여줌
    )

# app.py
# 로그인
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

```python
# app.py
# 가입
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


def save_memo(url_receive=None):
    from = request.form
    url_receive = form['url_give']
    comment_receive = form['comment_give']

    headers = {
        'User-Agent':
    }
    response = requests.get(
        url_receive,
        headers=headers
    )
    soup = BeautifulSoup(response.text,'html.parser')

    title = soup.select_one('meta[property="og:title"]')
    url = soup.select_one('meta[property="og:description"]')
    image = soup.select_one('meta[property')
    print(description)
    print(title['content'])
    print(url['content'])


    document = {
        'url': url_receive,
        'comment': comment_receive,
    }
    db.articles.insert_one(document)
    return jsonify(
        {'result': 'success', 'msg': '저장했습니다.'}
    )






# mongodb 추가
client = MongoClient('localhost', 27017)
db = client.

    
    