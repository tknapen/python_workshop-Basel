def test_list_indexing(todo_list):
    return todo_list == [1, 'B', 'REPLACED', [5, 3, 1038, 'C'], [1, 3, 5, [9, 3, 1, 'REPLACED']]]


def test_slicing_1(my_new_list):
    return my_new_list == [2, 3, 4, 5, 6]