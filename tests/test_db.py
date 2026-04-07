from dataclasses import asdict

from sqlalchemy import select

from fastapizero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(user='joao', email='joao@test.com', password='test123')

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.user == 'joao'))
        assert asdict(user) == {
            'id': 1,
            'user': 'joao',
            'email': 'joao@test.com',
            'password': 'test123',
            'created_at': time,
        }
