#!/usr/bin/python3

import datetime as dt
import getpass

_rootdir = './tickets/'

def get_msg():
    return input('What\'s wrong?: ')

if __name__ == '__main__':
    msg = get_msg()

    now = dt.datetime.now()
    fn = '{}-{}-{}-{}-{}-{}'.format(now.year,
                                    now.month,
                                    now.day,
                                    now.hour,
                                    now.minute,
                                    getpass.getuser())

    with open(_rootdir + fn, 'w') as f:
        f.write('{}\n'.format(msg))

    print('Thanks; Buzzing Alan...')
