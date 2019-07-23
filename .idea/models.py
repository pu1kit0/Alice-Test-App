if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    created_at = Column(String(50))
    created_by = Column(String(50))
    priority = Column(Integer)