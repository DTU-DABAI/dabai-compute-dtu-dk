"""Upload site."""

from os.path import expanduser

from six.moves import configparser

from subprocess import Popen


def main():
    """Handle command-line."""
    config_filename = expanduser('~/python.cfg')
    config = configparser.ConfigParser()
    config.read(config_filename)

    host = config.get('dabai-compute-dtu-dk', 'host')
    target_directory = config.get('dabai-compute-dtu-dk', 'directory')
    user = config.get('dabai-compute-dtu-dk', 'user')

    destination = user + '@' + host + ':' + target_directory
    subprocess = Popen(['scp', '-r', 'site/index.html', destination])
    subprocess = Popen(['scp', '-r', 'site/css/', destination])
    subprocess = Popen(['scp', '-r', 'site/fonts/', destination])
    subprocess = Popen(['scp', '-r', 'site/images/', destination])
    subprocess = Popen(['scp', '-r', 'site/js/', destination])


if __name__ == '__main__':
    main()
