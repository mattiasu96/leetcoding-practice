from random_problems.course_schedule.course_schedule import Solution


def test_course_schedule():
    num_courses = 3
    prerequisites = [[1, 0], [2, 1]]

    result = Solution().canFinish(num_courses, prerequisites)

    assert result == True


def test_course_single_schedule():
    num_courses = 3
    prerequisites = [[0, 2], [1, 2], [2, 0]]

    result = Solution().canFinish(num_courses, prerequisites)

    assert result == False


def test_course_false_schedule():
    num_courses = 2
    prerequisites = [[1, 0], [0, 1]]

    result = Solution().canFinish(num_courses, prerequisites)

    assert result == False
