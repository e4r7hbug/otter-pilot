"""Otter Pilot, ready for duty."""
import importlib
import logging
import pkgutil

import click

LOG = logging.getLogger(__name__)


def main():
    """Entry point."""
    logging.basicConfig()

    link_commands(root)

    root()


@click.group()
def root():
    """Ready for takeoff."""
    click.secho('Aye aye, otter away!', fg='green')


def link_commands(pilot_root_group):
    """Search for Pilot commands and link in."""
    commands_module_path = '.'.join([__package__, 'commands'])
    LOG.debug('Commands module path: %s', commands_module_path)
    commands_module = importlib.util.find_spec(commands_module_path)

    for module_info in pkgutil.iter_modules(commands_module.submodule_search_locations):
        command_module_path = '.'.join([commands_module_path, module_info.name])
        LOG.debug('Command module path: %s', command_module_path)

        module = importlib.import_module(command_module_path)
        LOG.debug('Module: %s', module)

        *_, command_name = module.__name__.split('.')
        try:
            command = click.command()(module.main)
            LOG.debug('Regular entry point function wrapped.')
        except TypeError:
            LOG.debug('Command is already a Click Command.')
            command = module.main
        LOG.debug('New command to attach: %s', command)

        pilot_root_group.add_command(command, name=command_name)


if __name__ == '__main__':
    main()
