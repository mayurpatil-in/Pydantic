# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    lesson_id: int
    topics: str

class Modules(BaseModel):
    module_id: int
    name: str
    lesson: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Modules]

course = Course(
    course_id=1,
    title="Python Mastery",
    modules=[
        Modules(
            module_id=101,
            name="Basics",
            lesson=[
                Lesson(lesson_id=1, topics="Variables & Data Types"),
                Lesson(lesson_id=2, topics="Control Flow"),
            ],
        ),
        Modules(
            module_id=102,
            name="Advanced",
            lesson=[
                Lesson(lesson_id=3, topics="Decorators"),
                Lesson(lesson_id=4, topics="Generators"),
            ],
        ),
    ],
)

# ✅ Print in different ways
print("Default print:")
print(course)