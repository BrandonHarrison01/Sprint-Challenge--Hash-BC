#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    for i in range(length):

        print('from hash', i, hash_table_retrieve(ht, limit - weights[i]))

        if hash_table_retrieve(ht, limit - weights[i]) is not None:
            return [i, hash_table_retrieve(ht, limit - weights[i])]

        hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [2, 3, 4, 9]
print(get_indices_of_item_weights(weights, 4, 6))