class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating(0)


class VideoRating:
    def __init__(self, rating=0):
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if 0 <= rating < 6:
            self.__rating = rating
        else:
            raise ValueError('неверное присваиваемое значение')

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
