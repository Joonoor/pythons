from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


db_connection_string = 'postgresql://postgres:PolareulE!342967@localhost:5432/postgres'
db = create_engine(db_connection_string)
Base = declarative_base()
Session = sessionmaker(bind=db)


class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)


def test_add_subject():
    sh = Session()
    subject = Subject(subject_id=100, subject_title="french")
    sh.add(subject)
    sh.commit()
    saved = sh.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "french"
    sh.delete(saved)
    sh.commit()
    sh.close()


def test_update_subject():
    sh = Session()
    subject = Subject(subject_id=100, subject_title="french")
    sh.add(subject)
    sh.commit()
    saved = sh.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "french"

    subject.subject_title = 'english'
    sh.commit()
    saved = sh.query(Subject).filter_by(subject_id=100).first()

    sh.delete(saved)
    sh.commit()
    sh.close()
