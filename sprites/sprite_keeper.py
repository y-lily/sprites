from pathlib import Path

from .sprite_sheet import SpriteSheet


class SpriteKeeper:

    """
    Tool used to store spritesheets from the given directory
    for quicker access.
    Spritesheets are added into SpriteKeeper's dictionary on demand.
    Spritesheets can be accessed via `get_spritesheet` method.
    """

    def __init__(self, resource_dir: str | Path) -> None:
        self._spritesheets: dict[Path, SpriteSheet] = {}
        self._resource_dir = Path(resource_dir)

    def get_spritesheet(self,
                        name: str | Path,
                        ) -> SpriteSheet:
        """
        Get a spritesheet with the given name from the resource directory.
        """

        path = self._resource_dir / name

        try:
            # Don't create a new spritesheet if it's already present.
            spritesheet = self._spritesheets[path]
        except KeyError:
            # Make default alpha true in order to have access to both transparent and non-transparent versions.
            spritesheet = self._spritesheets.setdefault(
                path, SpriteSheet(path, alpha=True))

        return spritesheet
