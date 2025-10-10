from book.schemas import Book

books: list[Book] = [
    Book(id=1,
         title="Dune",
         author="Frank Herbert",
         publisher="Chilton Books",
         published_date="1965-8-1",
         page_count=412,
         language="English"
         ),
    Book(id=2,
         title="The Name of the Wind",
         author="Patrick Rothfuss",
         publisher="DAW Books",
         published_date="2007-3-27",
         page_count=662,
         language="English"
         )
]
