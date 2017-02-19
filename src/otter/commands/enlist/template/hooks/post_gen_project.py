"""Clean out __pycache__ directories."""
import logging
import pathlib

LOG = logging.getLogger(__name__)


def main():
    """Main."""
    project_dir = pathlib.Path().absolute()
    LOG.debug('Absolute generated project path: %s', project_dir)

    for path in project_dir.rglob('*.j2'):
        LOG.debug('Strip .j2 suffix: %s', path)
        path.rename(path.with_suffix(''))


if __name__ == '__main__':
    logging.basicConfig()

    main()
