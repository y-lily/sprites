from os import PathLike
from typing import IO, Sequence, TypeAlias, Union

import pygame as pg
from pygame import Color, Rect, Surface

RGBAOutput: TypeAlias = tuple[int, int, int, int]
ColorValue = Union[Color, int, str,
                   tuple[int, int, int],
                   RGBAOutput,
                   Sequence[int]]
AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
FileArg = Union[AnyPath, IO[str], IO[bytes]]


class SpriteSheet:
    """
    A big image containing multiple smaller images which can be extracted
    via `extract_image` or `split` methods.
    """

    def __init__(self,
                 file_path: FileArg,
                 alpha: bool = False,
                 ) -> None:

        sheet = pg.image.load(file_path)
        self._sheet = sheet.convert_alpha() if alpha else sheet.convert()
        self.alpha = alpha

    @property
    def size(self) -> tuple[int, int]:
        return self._sheet.get_size()

    def extract_image(self,
                      rect: tuple[int, int, int, int] | Rect,
                      alpha: bool | None = None,
                      colorkey: ColorValue | None = None,
                      ) -> Surface:
        """
        Extract part of the spritesheet located on the given rect.
        If alpha is not provided, initial alpha value will be used.
        Both alpha and colorkey cannot be true.
        """

        if alpha is None:
            alpha = self.alpha
        if alpha and colorkey:
            raise ValueError("Cannot accept both alpha and colorkey.")

        size = rect[2:4]
        if alpha:
            image = Surface(size, pg.SRCALPHA).convert_alpha()
        else:
            image = Surface(size).convert()
        if colorkey:
            image.set_colorkey(colorkey, pg.RLEACCEL)

        image.blit(self._sheet, (0, 0), rect)
        return image

    def extract_whole(self,
                      alpha: bool | None = None,
                      colorkey: ColorValue | None = None,
                      ) -> Surface:
        """
        Extract the entire spritesheet as a single image.
        If alpha is not provided, initial alpha value will be used.
        Both alpha and colorkey cannot be true.
        """

        rect = self._sheet.get_rect()
        return self.extract_image(rect=rect, alpha=alpha, colorkey=colorkey)

    def split(self,
              size: tuple[int, int],
              alpha: bool | None = None,
              colorkey: ColorValue | None = None,
              ) -> list[Surface]:
        """
        Split the spritesheet into equal chunks (sprites) of the given size.
        Any extra area will be cropped out.
        If alpha is not provided, initial alpha value will be used.
        Both alpha and colorkey cannot be true.
        """

        width, height = size
        rects = [(x, y, width, height)
                 for y in range(0, self._sheet.get_height(), height)
                 for x in range(0, self._sheet.get_width(), width)]
        return [self.extract_image(r, alpha, colorkey) for r in rects]
