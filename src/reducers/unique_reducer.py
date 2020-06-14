class UniqueReducer(object):

    def __init__(self):
        self.input_strings = None
        self.max_length = None
        self.count_strings = None
        self._strings = None
        self.results = []
        self.DOTS = [3, 2, 1]

    def enter_strings(self):
        self.count_strings = int(input("Enter count strings."))
        self.input_strings = [[] for y in range(self.count_strings)]
        self._strings = []
        for i in range(self.count_strings):
            current_string = input("Enter current string.")
            self.input_strings[i].append(current_string)
            self._strings.append(current_string)

    def input_max_length(self):
        self.max_length = int(input("Enter limit max_length"))

    def reduce_strings(self):
        self.input_strings = self._check_duplicates()
        self.input_strings = self._sort()
        for s in self.input_strings:
            self._reduce_string(s)

    def _reduce_string(self, line):
        is_valid_line = self._check_valid_line(line)
        possible_result_unique_string = line[0]
        is_possible = True
        if is_valid_line:
            possible_reduction = len(line[0]) - self.max_length
            for dot in self.DOTS:
                is_unique = False
                end = len(line[0]) - (possible_reduction + dot)
                for start in range(1, end):
                    possible_result_unique_string = self._form_possible_string(line, possible_reduction, dot, start)
                    is_unique = self._check_unique(possible_result_unique_string)
                    if is_unique:
                        break
                if is_unique:
                    break
                elif dot == self.DOTS[len(self.DOTS) - 1]:
                    is_possible = False
                    self._print_impossible_line(line)

        if is_possible:
            self.results.append(possible_result_unique_string)

    @staticmethod
    def _print_impossible_line(line):
        if line[1] == 0:
            print("Impossible make unique string - {}".format(line[0]))
        else:
            print("Impossible make unique string - {}({})".format(line[0], line[1]))

    def _check_duplicates(self):
        duplicate = []
        copy_input_string = list.copy(self.input_strings)
        for i in range(len(copy_input_string)):
            current_string = copy_input_string[i][0]
            duplicate.append(current_string)
            if self._strings.count(current_string) > 1:
                copy_input_string[i].append(duplicate.count(current_string))
            else:
                copy_input_string[i].append(0)
        return copy_input_string

    @staticmethod
    def _form_possible_string(line, possible_reduction, dot, start):
        string = line[0]
        possible_result_string = string[:start] + "." * dot + string[possible_reduction + dot + start:]
        return possible_result_string

    def _check_unique(self, possible_result_unique_line):
        return possible_result_unique_line not in self.results

    def _check_valid_line(self, line):
        valid = [self._check_max_length(line)]
        return all(valid)

    def _check_max_length(self, line):
        return len(line[0]) >= self.max_length

    def _sort(self):
        return sorted(self.input_strings, key=self._sort_by_max_length)

    @staticmethod
    def _sort_by_max_length(input_str):
        return len(input_str[0])

    def get_results(self):
        for i in range(len(self.results)):
            if self.input_strings[i][1] == 0:
                print(self.results[i])
            else:
                print(self.results[i] + "({})".format(self.input_strings[i][1]))
