"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_grades = []
    for grade in student_scores:
        rounded_grades.append(int(round(grade)))
    return rounded_grades


round_scores([90.33, 40.5, 55.44, 70.05,
                  30.55, 25.45, 80.45, 95.3, 38.7, 40.3])


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    fail_counter = 0

    for grade in student_scores:
        if grade < 0 or grade > 100:
            continue
        elif grade <= 40:
            fail_counter += 1
    return fail_counter


count_failed_students([99, 40, 111, -1])


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    the_best = []

    for grade in student_scores:
        if grade >= threshold:
            the_best.append(grade)
    return the_best


above_threshold([90, 40, 55, 70, 30, 68, 70, 75, 83, 96], threshold=75)


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    new_grade_thresholds = []

    grade_step = (highest - 40) // 4

    for i in range(41, highest, grade_step):
        new_grade_thresholds.append(i)
    return new_grade_thresholds


letter_grades(highest=96)


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_list = []

    for i, name in enumerate(student_names):
        score = student_scores[i]
        ranked_list.append(str(f'{i + 1}. {name}: {score}'))
    return ranked_list


student_ranking([100, 99, 90, 84, 66, 53, 47],
                    ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred'])

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_exam = []
    perfect = 100

    for sublist in student_info:
        score = sublist[1]
        if score == perfect:
            perfect_exam = sublist
            return perfect_exam

    return perfect_exam



perfect_score(student_info=[['Charles', 90], ['Tony', 80], ['Alex', 100]])
