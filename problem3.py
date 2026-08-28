'''Given a dictionary of student roll numbers with the list of courses they chose,
 find the courses sorted from the most number of enrollments to the least.'''
def courses_sorted_by_enrollment(student_courses: dict) -> list:
    course_count = {}

    for courses in student_courses.values():
        for course in courses:
            if course not in course_count:
                course_count[course] = 1
            else:
                course_count[course] += 1

    return sorted(course_count, key=course_count.get, reverse=True)