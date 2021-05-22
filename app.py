(    import hashlib
    from datetime import datetime

    from flask import Flask, render_template, request

    # 플라스크 웹 서버 생성하기
    app = Flask(__name__)




    # API 추가
    @app.route('/', methods=['GET'])    # 데코레이터 문법
    def index():   # 함수 이름은 고유해야 한다
        return render_template('index.html', test='테스트')

    # mongodb 추가
    client = MongoClient('localhost', 27017)
    db = client.get_database('sparta')

    # .env 파일을 환경변수로 설정
    load_dotenv()
    # 환경변수 읽어오기
    JWT_SECRET = os.environ['JWT_SECRET']



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
    from flask import Blueprint, render_template

bp = Blueprint
    'api',  #블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/api'


    @app.route('/api/login', methods=['POST'])
    def api_login()
        id = request.form['id_give']
        pw = request.form['pw_give']

       pw_hash = hashlib.sha3_256(pw.encode()).hexdigest()

       user = db.users.find_one({'id': id, 'pw': pw_hash}, {'_id': False})

       # 만약 가입했다면?
       if user:
        # 로그인 성공이기 때문에 JWT 생성
        expiration_time = datetime.timedelta(hours=1)
        payload = {
            'id': id,
            'exp': datetime.datetime.utcnow() + expiration_time
      }
        token = jwt.encode(payload, 'secret')
        print(token)

        try:
            payload = jwt.encode(token, JWT_SECRET, algorithms=['HS256'])
            print(payload)
            return jsonify({'result': 'success', 'id': paylaod['id']})

        except jwt.exceptions.ExpiredSignatureError:
            # Try부분을 실행했지만 위와 같은 에러가 난다면
            return jsonify({'result': 'fail'})


    @app.route('/api/register', methods=['POST'])
    def api_register():
        id = request.form['id_give']
        pw = request.form['pw_give']

        # 회원가입
        hashlib.sha3_256(pw.encode()).hexdigest()

        # salting
        # 1. pw + 랜덤 문자열 추가(솔트)
        # 솔트 추가된 비밀번호 해시
        # DB에 저장할 때는 해시 결과물 + 적용한 솔트) 묶어서 저장


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











)