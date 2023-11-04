class Library:
    def books(self):
        print("Wings of Fire")
class News(Library):
    def manorama(paper):
        print("Malayala Manorama")
class Stories:
    def english(story):
        print("this is an english story")

class Magazine(News,Stories):
    def digest(quiz):
        print("this is a digest")


x=Magazine()
x.manorama()
x.books()
x.digest()
x.english()