class Car:
    """
    Базовый класс для автомобилей.
    """

    def __init__(self, model: str, color: str, engine_type: str, price: float):
        """
        Инициализирует объект автомобиля.

        Args:
            model (str): Модель автомобиля.
            color (str): Цвет автомобиля.
            engine_type (str): Тип двигателя (бензин, дизель, электрический).
            price (float): Цена автомобиля.
        """
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.price = price  #цена инкапслулирована т.к. есть потребность в проверке данных на правильность при установке нового значения цены

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.
        """
        return f"{self.color} {self.model} ({self.engine_type}), Price: {self.price}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Car для отладки.
        """
        return f"Car(model='{self.model}', color='{self.color}', engine_type='{self.engine_type}', price={self.price})"

    @property
    def price(self) -> float:
        """
        Возвращает цену автомобиля.
        """
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Устанавливает цену автомобиля.

        Raises:
            ValueError: Если цена отрицательна.
        """
        if not isinstance(new_price, float):
            raise TypeError("Цена должна быть типа float")
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = new_price


    def honk(self) -> str:
        """
        Возвращает звук клаксона.
        """
        return "Beep! Beep!"

    def start_engine(self) -> str:
        """
        Возвращает звук запуска двигателя.
        """
        return "Vroom! Vroom!"

class Truck(Car):
    """
    Класс для грузовых автомобилей. Наследует от Car.
    """

    def __init__(self, model: str, color: str, engine_type: str, price: float, load_capacity: float):
        """
        Инициализирует объект грузового автомобиля.

        Args:
            model (str): Модель автомобиля.
            color (str): Цвет автомобиля.
            engine_type (str): Тип двигателя.
            price (float): Цена автомобиля.
            load_capacity (float): Грузоподъемность (в тоннах).
        """
        super().__init__(model, color, engine_type, price)
        self.load_capacity = load_capacity  # Инкапсуляция, причина та же что и с ценой

    def __str__(self) -> str:
        """
        Перегружает строковое представление объекта Truck.
        Т.к. появилась load_capacity
        """
        return f"{super().__str__()} - Load Capacity: {self.load_capacity} tons"

    def __repr__(self) -> str:
        """
        Перегружает строковое представление объекта Truck для отладки.
        """
        return f"Truck(model='{self.model}', color='{self.color}', engine_type='{self.engine_type}', price={self.price}, load_capacity={self.load_capacity})"

    @property
    def load_capacity(self) -> float:
        """
        Возвращает грузоподъемность грузовика.
        """
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, new_load_capacity: float) -> None:
        """
        Устанавливает грузоподъемность грузовика.

        Raises:
            ValueError: Если грузоподъемность отрицательна или слишком велика.
        """
        if not isinstance(new_load_capacity, float):
            raise TypeError("Грузоподьемность должна быть типа float")
        if new_load_capacity <= 0:
            raise ValueError("Грузоподъемность должна быть больше нуля.")
        self._load_capacity = new_load_capacity

    def start_engine(self) -> str:
        """
        Перегружает метод start_engine().

        Возвращает специфический звук запуска двигателя грузовика.
        Причина перегрузки: Грузовики обычно имеют более мощные двигатели и издают другой звук при запуске.
        """
        return "RrrrrrrrrrrrrrRRRRRRRRRRRRRRR!"

    def load_cargo(self, weight: float) -> str:
        """
        Унаследованный метод.
        Возвращает сообщение о загрузке груза.

        Args:
            weight (float): Вес груза (в тоннах).

        Returns:
            str: Сообщение о загрузке груза.
        """
        if weight > self.load_capacity:
            return f"Превышена грузоподъемность! Максимальная загрузка: {self.load_capacity} тонн."
        return f"Загружено {weight} тонн груза."