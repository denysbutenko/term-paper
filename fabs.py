import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..'))
from fabfile import *


def my_deploy():
    env.domain = 'mq.denysbutenko.com'
    env.repository = 'git@github.com:denysbutenko/term-paper.git'

    deploy()

if __name__ == '__main__':
    # hack for pycharm run configuration.
    import subprocess
    import sys
    subprocess.call(['fab', '-f', __file__] + sys.argv[1:])
