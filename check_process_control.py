#!/bin/python3

import os
import subprocess

for filename in os.listdir('/tmp'):
    if filename.startswith('side_effect_'):
        os.unlink(os.path.joint('/tmp', filename))
pidfile = os.environ.get('TMT_TEST_PIDFILE', '/var/tmp/tmt-test.pid')
print(f'pidfile={pidfile}')
with open(pidfile) as pidfile_fo:
    test_pid = pidfile_fo.read().split()[0]
print(f'test_pid={test_pid}')
print(f'my pid={os.getpid()}')
print(f'my parent pid={os.getppid()}')
print("Children of the test_pid:", flush=True)
subprocess.run(['pstree', '-p', str(test_pid)])
print("Calling simulated reboot", flush=True)
subprocess.run(['./simulate-tmt-reboot'])
for i in range(10):
    open(f'/tmp/side_effect_{i}', 'w').close()
