import bubble_insert
import time

start = time.time()


machine0 = bubble_insert.Sorting_machine()

machine0.make_array_suffled(1000)
# machine0.make_random_array(0, 100, 15)
machine0.printing()

# machine0.bubble_sort()
# machine0.bubblesort_reverse()
machine0.insertion_sort()


machine0.printing()

end = time.time() - start

print(end)
