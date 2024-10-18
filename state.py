from typing import List, Self


def intersection(lst1, lst2) -> bool:
    result = False
    if len(list(set(lst1) & set(lst2))) > 0:
        result = True
    return result


class State:
    def __init__(self, name: str,
                 has_trigger: bool = False,
                 is_evening: bool = False,
                 is_perm: bool = False,
                 counter_names: List[str] | None = None):
        self.name = name
        self.has_trigger = has_trigger
        self.is_evening = is_evening
        self.is_perm = is_perm
        self.counter_names = counter_names

    def trigger(self, active_states: List[str]) -> Self | None:
        if intersection(self.counter_names, active_states):
            return None
        else:
            return Self
