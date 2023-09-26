from contextlib import suppress
from typing import TypeVar

from pygame import Surface

AnimationState = TypeVar("AnimationState", bound=object)


class Animation:

    def __init__(self,
                 frames: dict[AnimationState, list[Surface]],
                 frame_rate: int,
                 initial_state: AnimationState,
                 initial_frame: int = 0,
                 ) -> None:

        self._frames = frames
        self._frame_rate = frame_rate
        self.state = initial_state
        self._current_frame: float = initial_frame
        self._default_image = self.get_image()

    def __getitem__(self, key: AnimationState) -> list[Surface]:
        return self._frames[key]

    @property
    def current_frame(self) -> int:
        return int(self._current_frame)

    @current_frame.setter
    def current_frame(self, new_value: int) -> None:
        self._current_frame = new_value

    def get_image(self) -> Surface:
        with suppress(KeyError):
            return self._frames[self.state][self.current_frame]
        return self._default_image