# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Definir la estructura de la tabla
Base = declarative_base()

class Oferta(Base):
    __tablename__ = 'ofertas'
    id = Column(Integer, primary_key=True)
    trabajo_nombre = Column(String)
    empresa = Column(String)
    lugar_trabajo = Column(String)
    tipo_empleo = Column(String)
    link_empleo = Column(String)

class SqlitePipeline:
    def __init__(self, db_url):
        self.db_url = db_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(db_url=crawler.settings.get('SQLITE_DB_URL'))

    def open_spider(self, spider):
        engine = create_engine(self.db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        session = self.Session()
        oferta = Oferta(**item)
        session.add(oferta)
        session.commit()
        session.close()
        return item
