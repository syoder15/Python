#Sam Yoder
#This is just a little quicksort function

def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp


def compare_ints(a, b):
    return a <= b


def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1
    j = p
    while j < r:
        #increments i, then swaps the position of j and i, then increments j if the function that is used/called
        #winds up returning true
        if compare_func (the_list[j], pivot) :
            i += 1
            swap (the_list, i ,j)
            j += 1
        #otherwise increments j
        else:
            j += 1
    swap(the_list, r, (i+ 1))
    # return the index where the pivot is now located, which should be
    #  the index i + 1
    return i+1



l = [2, 8, 12, 45, 9, 1, 3]


# should print [2, 1, 3, 4, 7, 5, 6, 8]

def quicksort (the_list, p, r, compare_func):
    if p < r:
        #return a variable q which is where the partition function placed pivot
        q = partition(the_list, p, r, compare_func)
        #recursively quicksort the list starting at index p and going up to but not including index q
        quicksort(the_list, p, (q - 1), compare_func)
        #recursively quicksort the list starting at index just past q up to and including index r
        quicksort (the_list, (q + 1), r, compare_func)
    
    return the_list

print quicksort(l, 0, (len(l) - 1), compare_ints)

def sort (the_list, compare_func):
    p = 0
    r = (len(the_list) - 1)
    return quicksort (the_list, p, r, compare_func)
    

