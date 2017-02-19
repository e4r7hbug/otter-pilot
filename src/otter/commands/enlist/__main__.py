"""Enlist new Otter Pilot commands."""
import logging
import pathlib

from cookiecutter.main import cookiecutter

LOG = logging.getLogger(__name__)


def main():
    """Stamp out new Copilot command."""
    command_dir = pathlib.Path(__file__).parent
    LOG.debug('Module directory: %s', command_dir)

    template_dir = command_dir / 'template'
    LOG.debug('Template directory: %s', template_dir)

    cookiecutter(str(template_dir))


if __name__ == '__main__':
    main()
