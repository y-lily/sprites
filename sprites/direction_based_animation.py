from typing import Generic, TypeAlias

from pygame import Surface
from typing_extensions import override

from .animation import Animation
from .direction import Direction
from .image_holder import ImageHolder, StateType

DirectionName: TypeAlias = str


class DirectionBasedAnimation(ImageHolder[StateType]):

    state: StateType

    def __init__(self,
                 animations: dict[StateType, Animation[Direction]],
                 initial_state: StateType,
                 ) -> None:

        self._animations = animations
        self.state = initial_state

    @property
    def direction(self) -> Direction:
        return self._animations[self.state].state

    @direction.setter
    def direction(self, new: Direction | DirectionName) -> None:
        self._animations[self.state].state = Direction(new)

    @override
    def get_image(self) -> Surface:
        return self._animations[self.state].get_image()

    @override
    def update(self, dt: float) -> None:
        self._animations[self.state].update(dt)
