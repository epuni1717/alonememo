import hashlib
from urllib import response

from app import db


def test_로그인(client):


    def test_회원가입(client):
        data = {
            'id_give': 'tester01'
            'pw_give': 'test'
        }

        response: object = client.post(
            '/api/register',
            data=data
        )


    assert response.status_code == 200

    user = db.users.find_one(
        {'id': 'tester01'},
        {'_id': False}
    )
    # 패스워드 평문저장하지 않음
    assert user['pw'] != 'test'
    pw_hash = hashlib.sha256('test'.encode()).hexdigest()
    assert user['pw'] == pw_hash