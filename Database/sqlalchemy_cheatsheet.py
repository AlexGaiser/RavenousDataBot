#sqlalchemy cheatsheet


from sqlalchemy.ext.automap import automap_base

from sqlalchemy import create_engine, inspect, Table, MetaData 

from sqlalchemy.orm import mapper, sessionmaker, session

engine = create_engine('sqlite:///pitchfork.sqlite')

# connection = engine.connect()

print(engine.table_names())



from sqlalchemy import MetaData, Table

metadata = MetaData()




reviews = Table('reviews', metadata, autoload = True, autoload_with = engine)

print(repr(reviews))

inspect = inspect(engine)



Base = automap_base()

