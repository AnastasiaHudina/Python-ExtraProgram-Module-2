# TODO: Подробно описать три произвольных класса
import doctest


# TODO: описать класс
class AngelCastiel:
    def __init__(self, demons_incoming: int, irritation_level: int):
        """
        Создание и подготовка к работе объекта "AngelCastiel".

        :param demons_incoming: Количество приближающихся демонов.
        :param irritation_level: Уровень раздраженности по шкале от 0 до 10.

        Примеры:
        Cass = AngelCastiel(37,7)  # инициализация экземпляра класса
        """
        if not isinstance(demons_incoming, int):
            raise TypeError("Количество приближающихся демонов должно быть типа int.")
        if demons_incoming <= 0:
            raise ValueError("Количество приближающихся демонов не может быть отрицательным числом - они всегда "
                             "наступают.")
        self.demons_incoming = demons_incoming

        if not isinstance(irritation_level, int):
            raise TypeError("Уровень раздраженности должен быть типа int.")
        if irritation_level < 0 or irritation_level > 10:
            raise ValueError("Уровень раздраженности должен быть отмечен по шкале от 0 до 10.")
        self.irritation_level = irritation_level

    def slain_demons(self, killed_demons: int) -> None:
        """
        Уничтожение демонов.

        :param killed_demons: Количество убитых демонов.
        :raise ValueError: Если количество убитых демонов отрицательно или превышает количество приближающихся,
        то возвращается ошибка.

        Примеры:
        >>> Cass = AngelCastiel(37,7)
        >>> Cass.slain_demons(5)
        """
        if not isinstance(killed_demons, int):
            raise TypeError("Количество убитых демонов должно быть типа int.")
        if killed_demons < 0 or killed_demons > self.demons_incoming:
            raise ValueError("Количество убитых демонов должно быть положительным и не должно превышать количество "
                             "приближающихся.")
        self.demons_incoming -= killed_demons

    def is_irritated(self) -> bool:
        """
        Функция, которая проверяет раздражен ли Кастиэль.

        :return: Раздражен ли Кастиэль.

        Примеры:
        Cass = AngelCastiel(37,7)
        Сass.is_irritated()
        """
        if self.irritation_level > 5:
            print('Кастиэль очень раздражен. Ожидайте саркастического ответа.')
            return True
        else:
            return False

    def sarcastic_comment(self) -> None:
        """
        Саркастичный комментарий. Помогает выпустить пар и обнулить уровень раздраженности.

        Примеры:
        Cass = AngelCastiel(37,7)
        Cass.sarcastic_comment()
        """

        print('Hey, assbutt!')
        self.irritation_level = 0


# TODO: описать ещё класс
class DeanWinchester:
    def __init__(self, pies_cont: int, trouble_sense_tingling: int):
        """
        Создание и подготовка к работе объекта "Dean_Winchester".

        :param pies_cont: Количество пирогов, находящихся в досягаемости.
        :param trouble_sense_tingling: Уровень тревоги по шкале от 0 до 10.

        Примеры:
        sassy_hunter = DeanWinchester(3,6)  # инициализация экземпляра класса
        """
        if not isinstance(pies_cont, int):
            raise TypeError("Количество пирогов, находящихся в досягаемости, должно быть типа int.")
        if pies_cont <= 0:
            raise ValueError("Количество пирогов, находящихся в досягаемости, должно быть положительным числом.")
        self.pies_cont = pies_cont

        if not isinstance(trouble_sense_tingling, int):
            raise TypeError("Уровень раздраженности должен быть типа int.")
        if trouble_sense_tingling < 0 or trouble_sense_tingling > 10:
            raise ValueError("Уровень ощущения опасности должен быть отмечен по шкале от 0 до 10.")
        self.trouble_sense_tingling = trouble_sense_tingling

    def eat_all_pies(self, pies_to_be_consumed: int) -> None:
        """
        Уничтожение пирогов. Будут съедены все. Но парочка брату всё же останется.

        :param pies_to_be_consumed: Сколько пирогов поглотит Дин.
        :raise ValueError: Если количество съеденных пирогов будет отрицательно, будет превышать количество имеющихся
        поблизости или ни один из пирогов не был оставлен Сэму, то возвращается ошибка.

        Примеры:
        >>> sassy_hunter = DeanWinchester(5,6)
        >>> sassy_hunter.eat_all_pies(3)
        """
        if not isinstance(pies_to_be_consumed, int):
            raise TypeError("Количество съеденных пирогов должно быть типа int.")
        if pies_to_be_consumed < 0 or (pies_to_be_consumed > (self.pies_cont - 1)):
            raise ValueError("Количество съеденных пирогов должно быть положительным и не должно превышать количество "
                             "имеющихся поблизости. Необходимо также оставить минимум один пирог Сэму.")
        self.pies_cont -= pies_to_be_consumed

    def is_in_danger(self) -> bool:
        """
        Функция, которая проверяет в опасности ли Дин и Сэм.

        :return: В опасности ли Дин и Сэм.

        Примеры:
        sassy_hunter = DeanWinchester(5,6)
        sassy_hunter.is_in_danger()
        """
        if self.trouble_sense_tingling > 5:
            print('Винчестеры в опасности.')
            return True
        else:
            return False

    def save_Sammy(self) -> None:
        """
        Спасение Сэмми и спешное отступление в безопасность. Обнуляет уровень тревоги.

        Примеры:
        sassy_hunter = DeanWinchester(5,6)
        sassy_hunter.save_Sammy()
        """

        print('The "Sammy rescue" protocol is being implemented.')
        self.trouble_sense_tingling = 0


# TODO: и ещё один
class SamWinchester:
    def __init__(self, creatures_approaching: int, disapproval_level: int):
        """
        Создание и подготовка к работе объекта "Angel_Castiel".

        :param creatures_approaching: Количество приближающихся вампиров, призраков и оборотней.
        :param disapproval_level: Уровень неодобрения по шкале от 0 до 10.

        Примеры:
        sane_hunter = SamWinchester(28,8)  # инициализация экземпляра класса
        """
        if not isinstance(creatures_approaching, int):
            raise TypeError("Количество приближающихся тварей должно быть типа int.")
        if creatures_approaching <= 0:
            raise ValueError("Количество приближающихся тварей не может быть отрицательным числом - "
                             "они всегда наступают.")
        self.creatures_approaching = creatures_approaching

        if not isinstance(disapproval_level, int):
            raise TypeError("Уровень раздраженности должен быть типа int.")
        if disapproval_level < 0 or disapproval_level > 10:
            raise ValueError("Уровень неодобрения должен быть отмечен по шкале от 0 до 10.")
        self.disapproval_level = disapproval_level

    def hunt_things(self, killed_creatures: int) -> None:
        """
        Уничтожение тварей.

        :param killed_creatures: Количество убитых тварей.
        :raise ValueError: Если количество убитых тварей отрицательно или превышает количество приближающихся,
        то возвращается ошибка.

        Примеры:
        >>> sane_hunter = SamWinchester(28,8)
        >>> sane_hunter.hunt_things(5)
        """
        if not isinstance(killed_creatures, int):
            raise TypeError("Количество убитых тварей должно быть типа int.")
        if killed_creatures < 0 or killed_creatures > self.creatures_approaching:
            raise ValueError("Количество убитых тварей должно быть положительным и не должно превышать количество "
                             "приближающихся.")
        self.creatures_approaching -= killed_creatures

    def is_disapproving(self) -> bool:
        """
        Функция, которая проверяет одобряет ли Сэм ваши действия.

        :return: Одобряет ли Сэм ваши действия.

        Примеры:
        sane_hunter = SamWinchester(28,8)
        sane_hunter.is_disapproving()
        """
        if self.disapproval_level > 5:
            print('Сэм неодобряет ваши действия. Ожидайте нравоучений.')
            return True
        else:
            return False

    def moose_lecture(self) -> None:
        """
        Нравоучения и назидания, призванные переубедить и наставить вас на путь истинный.
        Позволяет очистить совесть и обнулить уровень неодобрения.

        Примеры:
        sane_hunter = SamWinchester(28,8)
        sane_hunter.moose_lecture()
        """

        print('We have guns and we will find you.')
        self.disapproval_level = 0


if __name__ == "__main__":
    doctest.testmod()
