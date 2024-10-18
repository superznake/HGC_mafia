from role import Role
from state import State


class Player:
    states = []
    active_states = []

    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.passive = role.passive

    def set_state(self, state: State):
        self.states.append(state)
        self.active_states.append(state.name)

    def update_state_morning(self):
        for state in self.states:
            if not state.is_evening:
                if state.has_trigger:
                    state.trigger(self.active_states)
                if not state.is_perm:
                    self.states.remove(state)
                    self.active_states.remove(state)

    def update_state_evening(self):
        for state in self.states:
            if state.is_evening:
                if state.has_trigger:
                    state.trigger()
                if not state.is_perm:
                    self.states.remove(state)
