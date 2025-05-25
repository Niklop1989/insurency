from sqlalchemy import create_engine,text

engine = create_engine("sqlite:///python.db")
with engine.connect() as connection:
    create_user_table = text( """
    CREATE TABLE IF not EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL 
    )
    """)
    connection.execute(create_user_table)

    insert_user = text( """
    INSERT INTO user(name) VALUES('Nikita') 
    """)
    connection.execute(insert_user)

    filter_query = text("SELECT * FROM user WHERE id =:user_id")
    cursor = connection.execute(filter_query,dict(user_id =1))
    res = cursor.fetchone()
    print(res)