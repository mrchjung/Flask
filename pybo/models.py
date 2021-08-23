from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)


answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(),nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


    #db.Column(자료형, 속성.)
    # primary key = 기본키
    # nullable = 빈 값을 허용할 것인지.
    #server_default 는 이전 데이터에도 적용. default는 추가데이터에만 적용

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable = True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
    # 기존 모델과 연결된 속성 = foreign key
    # db.Foreignkey('기존키.id') => 테이블명,컬럼명 이 전달됨.
    # db.Foreignkey('기존키.id', ondelete = 삭제옵션) => CASADE의 경우 기존것 삭제시 동기화.
    # question 속성은 답변모델에서 질문 보델을 참조하기 위해 추가. answer.question.subject 처럼 답변모델에서 질문모델의 속성을 불러올 수 있다.
    # backref = 역참조를 의미. a.question.answer_set 을 하면 질문모델에 연결된 답변모델들로 역참조 가능.
    # cascade='all, delete-orphan' 은 역참조대상이 삭제되면 함께 딸린 것들이 삭제되도독 한거.



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))

