import copy


class PermutationGenerator:
    list_of_elements = []
    permutation_indices = None
    tot_num_permutations = 0
    remaining_permutations = 0


    def __init__(self, list_of_elements):
        self.list_of_elements = copy.deepcopy(list_of_elements)
        self.permutation_indices = [None] * len(self.list_of_elements)
        self.tot_num_permutations = self.calculate_factorial(len(self.list_of_elements))
        self.reset_permutation_generator()


    def __iter__(self):
        return self

    def __next__(self):
        return self.trigger_permutation()

    def calculate_factorial(self, limit):
        if limit == 0:
            return 1
        return limit * self.calculate_factorial(limit - 1)

    def reset_permutation_generator(self):
        for i in range(len(self.permutation_indices)):
            self.permutation_indices[i] = i
        self.remaining_permutations = self.tot_num_permutations

    def trigger_permutation(self):
        permutation = [None] * len(self.permutation_indices)
        return self.generate_permutation(permutation)

    def generate_permutation(self, permutation):
        if len(permutation) != len(self.list_of_elements):
            raise ValueError("Size of current permutation array must be equal to the size of list of elements ")

        self.generate_next_permuation_indices_lexicographic()

        for i in range(len(self.permutation_indices)):
            permutation[i] = self.list_of_elements[self.permutation_indices[i]]

        return permutation


    """ https://www.nayuki.io/page/next-lexicographical-permutation-algorithm """
    def generate_next_permuation_indices_lexicographic(self):

        if self.remaining_permutations == 0:
            #raise ValueError('No permutations left')
            raise StopIteration
        elif self.remaining_permutations < self.tot_num_permutations:

            j = len(self.permutation_indices) - 2

            while self.permutation_indices[j] > self.permutation_indices[j + 1]:
                j -= 1

            k = len(self.permutation_indices) - 1
            while (self.permutation_indices[j] > self.permutation_indices[k]):
                k -= 1

            self.permutation_indices[j], self.permutation_indices[k] = self.permutation_indices[k], \
                                                                       self.permutation_indices[j]

            r = len(self.permutation_indices) - 1
            s = j + 1

            while r > s:
                self.permutation_indices[r], self.permutation_indices[s] = self.permutation_indices[s], \
                                                                           self.permutation_indices[r]
                r -= 1
                s += 1


        self.remaining_permutations -= 1


    """https://en.wikipedia.org/wiki/Heap%27s_algorithm"""
    def generate_permutation_heap(self, k_heap, list_of_elements):

        if k_heap == 1:
            print(list_of_elements)
        else:
            self.generate_permutation_heap(k_heap - 1, list_of_elements)

            for i in range(k_heap-1):
                if k_heap % 2 == 0:
                    list_of_elements[i], list_of_elements[k_heap-1] = list_of_elements[k_heap-1], list_of_elements[i]
                else:
                    list_of_elements[0], list_of_elements[k_heap-1] = list_of_elements[k_heap-1], list_of_elements[0]

                self.generate_permutation_heap(k_heap - 1, list_of_elements)






list_of_elements = ["1", "2", "3"]

permutations = PermutationGenerator(list_of_elements)

print("Heap algorithm: ")
permutations.generate_permutation_heap(len(list_of_elements), list_of_elements)

print("Lexicographic next permutation algorithm: ")
for permutation in iter(permutations):
    print(permutation)
