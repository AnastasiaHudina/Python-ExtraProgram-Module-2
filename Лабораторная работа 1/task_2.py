from task_1 import AngelCastiel, SamWinchester, DeanWinchester
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    Cass = AngelCastiel(37, 7)
    sassy_hunter = DeanWinchester(5, 6)
    sane_hunter = SamWinchester(28, 8)

    try:
        a = []
        Cass.slain_demons(a)
    except TypeError:
        print('TypeError: Количество убитых демонов должно быть типа int.')
    except ValueError:
        print('ValueError: Количество убитых демонов должно быть положительным и не должно превышать '
              'количество приближающихся')

    try:
        sassy_hunter.eat_all_pies('h')
    except TypeError:
        print('TypeError: Количество съеденных пирогов должно быть типа int.')
    except ValueError:
        print('ValueError: Количество съеденных пирогов должно быть положительным и не должно превышать '
              'количество имеющихся поблизости. Необходимо также оставить минимум один пирог Сэму.')

    try:
        sane_hunter.hunt_things(29)
    except TypeError:
        print('TypeError: Количество приближающихся тварей должно быть типа int.')
    except ValueError:
        print('ValueError: Количество приближающихся тварей не может быть отрицательным числом - '
              'они всегда наступают.')
