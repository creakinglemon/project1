import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://hllfkmecxpxvsh:00ccb6912b1258dffe7674c10403a980e6351dcc574445fd1e8fac6468a9d11b@ec2-3-224-165-85.compute-1.amazonaws.com:5432/dbjo3vq13g5nhl")
db = scoped_session(sessionmaker(bind=engine))

with open ('books.csv') as file:
    reader = csv.reader(file, delimiter=',')

    # skip headers
    reader.__next__()

    for line in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", 
            {"isbn": line[0], "title": line[1], "author": line[2], "year": int(line[3])})
    db.commit()