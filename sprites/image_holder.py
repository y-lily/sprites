from typing import Protocol

from pygame import Surface
from typing_extensions import override


class ImageHolder(Protocol):

    """
    Interface for classes storing an image or multiple images
    and providing them via the `get_image` method.
    A static implementation would have an empty `update` method.
    """

    def get_image(self) -> Surface:
        ...

    def update(self, dt: float) -> None:
        ...


class StaticImageHolder(ImageHolder):

    """
    Static implementation of the ImageHolder interface which
    returns the same image every single time and does nothing
    on update.
    """

    def __init__(self, image: Surface) -> None:
        self._image = image

    @override
    def get_image(self) -> Surface:
        return self._image

    @override
    def update(self, dt: float) -> None:
        pass
