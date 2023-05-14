def len_of_list(some_list):
    list_len = 0
    for elem in some_list:
        list_len += 1
    return list_len


def fitst_remote_func():
    pass


def count_elem_in_list(c_elem, some_list):
    counter = 0
    for elem in some_list:
        if elem == c_elem:
            counter += 1
    return counter


def prepare_list_to_print(some_list):
    result = ''
    index = 1
    for elem in some_list:
        result += '{}. {}\n'.format(index, elem)
        index += 1
    return result


def start_voting(cars_list):
    str_cars_list = prepare_list_to_print(cars_list)
    voting_result = dict()
    print('\nЧтобы проголосаовать выберите номер модели из списка:\n{}'
            'Для подсчета голосов введите 0.'.format(str_cars_list))
    while True:
        choice = int(input('\nВаш выбор: '))
        if choice == 0:
            return voting_result
        elif choice <= len_of_list(cars_list):
            if cars_list[choice-1] not in voting_result.keys():
                voting_result[cars_list[choice-1]] = 1
                print('Ваш голос принят.')
            else:
                voting_result[cars_list[choice-1]] += 1
                print('Ваш голос принят!')
        else:
            print('Ошибка ввода! Результат не будет учтен.\n')


def finish_voting(v_result):
    w_votes = 0
    for key, value in v_result.items():
        if value > w_votes:
            w_votes = value
            w_key = key
    if count_elem_in_list(w_votes, v_result.values()) > 1:
        print('\nПобедителя выявить не удалось, несколько авто набрали одинаковое количество голосов.')
    else:
        print('\nГолосование завершено!\nЛучший автомобиль года: {}\nКоличество голосов {}'.format(
            w_key, w_votes
        ))


def make_voting():
    temp = 0
    cars = []
    num_of_cars = int(input('Введите количество автомобилей, участвующих в голосовании: '))
    for num in range(1, num_of_cars + 1):
        new_car = input('Введите модель {}-го автомобиля: '.format(num))
        cars.append(new_car)
    print('\nГолосование создано!')
    result = start_voting(cars)
    finish_voting(result)


make_voting()
