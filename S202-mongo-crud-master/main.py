from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "Colecao")

db.create("Harry Potter e a ordem da fenix", "J.K. Rowling", 2003, 50.0)
db.create("Harry Potter e o calice de fogo", "J.K. Rowling", 2000, 35.0)
db.create("Harry Potter e a pedra filosofal", "J.K. Rowling", 1997, 23.50)

Colecao = db.read()

writeAJson(Colecao, "Livros")


