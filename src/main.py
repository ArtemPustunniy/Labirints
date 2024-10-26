import logging
import platform
import multiprocessing

from src.labirint.maze_facade import MazeCascade

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    maze = MazeCascade()
    maze.initialize_labirint()


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    main()
