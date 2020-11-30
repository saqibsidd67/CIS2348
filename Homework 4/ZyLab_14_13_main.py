# Global variable
num_calls = 0



# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary



def partition(user_ids, i, k):
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h]
        while pivot < user_ids[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h

def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return
        # pi is partitioning index, arr[p] is now
        # at right place
    pi = partition(user_ids, i, k)

        # Separately sort elements before
        # partition and after partition
    quicksort(user_ids, i, pi)
    quicksort(user_ids, pi + 1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)


