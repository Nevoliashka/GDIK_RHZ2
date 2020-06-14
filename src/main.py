from src.reducers import UniqueReducer

if __name__ == "__main__":
    a = UniqueReducer()
    a.enter_strings()
    a.input_max_length()
    a.reduce_strings()
    a.get_results()