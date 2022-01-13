from sqlalchemy import(
    create_engine, Table, column, Float, ForeignKey, Integar, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create veriable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistID", Integar, primary_key=True),
    Column("Name", String)
)

# create veriable for our "album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integar, primary_key=True),
    Column("Title", String),
    Column("ArtistID", Integar, ForeignKey("artist_table.ArtistId"))

)

# create veriable for our "Track" table 
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Making the connection
with db.connect() as connection:
    # Query 1 - select all records from the "Artist" table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)