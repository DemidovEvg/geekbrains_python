import time


TEST_CASES = (
    ('a', 1,),
    ('aaaa', 1,),
    ('aaaabbb', 2,),
    ('aaabacac', 4,),
    ('aabaab', 3,),
    ('aaaacaacaacaa', 4,),
)


def run(string: str) -> int:
    if not string:
        return 0

    the_best_sub_str = string[0]
    the_best_letters = 1
    the_best_last_index = 1

    for size in range(1, len(string) // 2 + 1):
        sub_str = string[:size]

        for start_index in range(size, len(string) + 1, size):
            if string[start_index:start_index + size] != sub_str:
                break

            if the_best_letters < start_index + size:
                the_best_sub_str = sub_str
                the_best_letters = start_index + size
                the_best_last_index = start_index + size

        if the_best_last_index == len(string):
            break

    print(f'{the_best_sub_str=} {the_best_letters=} {the_best_last_index=}')

    if the_best_last_index == len(string):
        return len(the_best_sub_str)

    return len(the_best_sub_str) + run(string[the_best_last_index:])


if __name__ == '__main__':
    start = time.perf_counter()
    result = run('aabaab')
    print(time.perf_counter() - start)
        # assert result == test_case[1], f'{test_case[0]}: {result} != {test_case[1]}'