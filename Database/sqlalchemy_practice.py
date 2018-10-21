# sqlalchemy practice

from sqlalchemy.ext.automap import automap_base

from sqlalchemy import create_engine, inspect, Table, MetaData, Column 

from sqlalchemy.orm import mapper, sessionmaker, session



from sqlalchemy.ext.automap import automap_base

from sqlalchemy import create_engine, inspect, Table, MetaData 

from sqlalchemy.orm import mapper, sessionmaker, session


Base = automap_base()


engine = create_engine('sqlite:///reddit_politics.db')

Base.prepare(engine, reflect = True)

metadata = MetaData()

metadata.bind = engine

metadata.create_all(engine)

reddit_posts = Table('reddit_posts', metadata, autoload = True, autoload_with = engine)

# print(repr(reddit_posts))

posts = Base.classes.reddit_posts

session = Session(engine)

