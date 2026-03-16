Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1={'Math','Physics','Chemistry'}
>>> s2={'Physics','Biology','Math'}
>>> print(s1&s2)
{'Math', 'Physics'}
>>> print(s1-s2)
{'Chemistry'}
>>> print(s2-s1)
{'Biology'}
>>> print(s1|s2)
{'Chemistry', 'Biology', 'Physics', 'Math'}
