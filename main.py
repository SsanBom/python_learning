import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def __generate_random_sequence():
    return np.random.randint(-10000, 10001, 1000)


def save_to_file(file, save_object):
    with open(file, 'w') as f:
        for element in save_object:
            f.write(str(element) + "\n")


def __convert_line_to_int_sequence(line):
    clean_fragmented_line = line.strip().split(' ')
    number_sequence = []
    for element in clean_fragmented_line:
        try:
            number_sequence.append(int(element))
        except ValueError:
            continue
    return number_sequence


def read_int_file(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            for element in __convert_line_to_int_sequence(line):
                data.append(element)
    return data


def __print_data_characteristics(seq_min, seq_max, seq_duplicate_number, seq_sum, seq_std):
    print(f"Минимальное значение числовой последовательности = {seq_min}")
    print(f"Максимальное значение числовой последовательности = {seq_max}")
    print(f"Количество повторяющихся значений числовой последовательности = {seq_duplicate_number}")
    print(f"Сумма всех чисел числовой последовательности = {seq_sum}")
    print(f"Срендеквадратическое отклонение числовой последовательности = {seq_std}")


def __construct_dataframe(series):
    dataframe = pd.DataFrame({"original": series})
    dataframe["sorted_ascending"] = dataframe["original"].sort_values().values
    dataframe["sorted_descending"] = dataframe["original"].sort_values(ascending=False).values
    return dataframe


def construct_plot(number_sequence, plot_title):
    plt.plot(number_sequence)
    plt.title(plot_title)
    plt.show()


def construct_double_plot(dataframe, title):
    plt.plot(dataframe["sorted_ascending"], label="по возрастанию")
    plt.plot(dataframe["sorted_descending"], label="по убыванию")
    plt.title(title)
    plt.legend()
    plt.show()


def construct_histogram(series, hist_title):
    rounded_series = series.round(-2)
    plt.hist(rounded_series)
    plt.title(hist_title)
    plt.show()


save_to_file("dataset.txt", __generate_random_sequence())
data_number_sequence = read_int_file("dataset.txt")
series = pd.Series(data_number_sequence)

data_min = series.min()
data_max = series.max()
data_duplicate_number = series.duplicated().sum()
data_sum = series.sum()
data_std = series.std()

__print_data_characteristics(data_min,
                             data_max,
                             data_duplicate_number,
                             data_sum,
                             data_std)

construct_plot(series, "График несортированных чисел датасета")
construct_histogram(series, "Гистограмма округленных до сотен чисел датасета")

dataframe = __construct_dataframe(series)

construct_double_plot(dataframe, "График отсортированных чисел датасета")
