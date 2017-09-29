# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = kwargs.get('ignore_case', False)
        if isinstance(items, list):
            self.items = (x for x in items)
        else:
            self.items = items
        self._s = set()

    def __next__(self):
        for a in self.items:
            if self.ignore_case and isinstance(a, str):
                if a.lower() not in map(lambda s: s.lower(), self._s):
                    self._s.add(a)
                    return a
            elif a not in self._s:
                self._s.add(a)
                return a
        else:
            raise StopIteration

    def __iter__(self):
        return self