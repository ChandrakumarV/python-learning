from dataclasses import dataclass


@dataclass
class Article:
    """A class for holding an article content"""

    # Attributes Declaration
    # using Type Hints

    title: str
    author: str
    language: str
    upvotes: int


class NormalArticle:
    """A class for holding an article content"""

    # Equivalent Constructor
    def __init__(self, title, author, language, upvotes):
        self.title = title
        self.author = author
        self.language = language
        self.upvotes = upvotes


# Two DataClass objects
dClassArticle1 = Article("DataClasses", "vibhu4agarwal", "Python", 0)
dClassArticle2 = Article("DataClasses", "vibhu4agarwal", "Python", 0)

# Two objects of a normal class
article1 = NormalArticle("DataClasses", "vibhu4agarwal", "Python", 0)
article2 = NormalArticle("DataClasses", "vibhu4agarwal", "Python", 0)

print("DataClass Equal:", dClassArticle1 == dClassArticle2)
print("Normal Class Equal:", article1 == article2)
