

class Product:

    def __init__(self, category_code, cls, display_nr, line, line_id, match_id,
                 name, number, operator_code, route_idx_from, route_idx_to):
        self._category_code: str = category_code
        self._cls: str = cls
        self._display_nr: str = display_nr
        self._line: str = line
        self._line_id: str = line_id
        self._match_id: str = match_id
        self._name: str = name
        self._number: str = number
        self._operator_code: str = operator_code
        self._route_idx_from: str = route_idx_from
        self._route_idx_to: str = route_idx_to

    @property
    def category(self):
        return self._category_code

    @property
    def cls(self):
        return self._cls

    @property
    def display_number(self):
        return self._display_nr

    @property
    def line(self):
        return self._line

    @property
    def line_id(self):
        return self._line_id

    @property
    def match_id(self):
        return self._match_id

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def operator_code(self):
        return self._operator_code

    @property
    def route_idx_from(self):
        return self._route_idx_from

    @property
    def route_idx_to(self):
        return self._route_idx_to

    def __repr__(self):
        return f'<{self.name}>'

    def __str__(self):
        return f'<{self.__module__}> {self.name}'
