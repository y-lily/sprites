from typing import Generic, Protocol, TypeVar

from pygame import Surface
from typing_extensions import override

StateType = TypeVar("StateType", bound=object)


class ImageHolder(Generic[StateType], Protocol):

    """
    Interface for classes storing an image or multiple images
    and providing them via the `get_image` method.
    A static implementation would have an empty `update` method.
    """

    state: StateType

    def get_image(self) -> Surface:
        ...

    def update(self, dt: float) -> None:
        ...


class StaticImageHolder(ImageHolder[None]):

    """
    Static implementation of the ImageHolder interface which
    returns the same image every single time and does nothing
    on update.
    """

    state = None

    def __init__(self, image: Surface) -> None:
        self._image = image

    @override
    def get_image(self) -> Surface:
        return self._image

    @override
    def update(self, dt: float) -> None:
        pass
