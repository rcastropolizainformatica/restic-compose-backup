import logging
from typing import List
from subprocess import Popen, PIPE

logger = logging.getLogger(__name__)


def test():
    return run_command(['ls', '/backup'])


def ping_mysql(host, port, username, password) -> int:
    """Check if the mysql is up and can be reached"""
    return run([
        'mysqladmin',
        'ping',
        '--host',
        host,
        '--port',
        port,
        '--user',
        username,
        f'--password={password}',
    ])


def ping_mariadb(host, port, username, password) -> int:
    """Check if the mariadb is up and can be reached"""
    return run([
        'mysqladmin',
        'ping',
        '--host',
        host,
        '--port',
        port,
        '--user',
        username,
        f'--password={password}',
    ])


def ping_postgres(host, port, username, password) -> int:
    """Check if postgres can be reached"""
    return run([
        "pg_isready",
        f"--host={host}",
        f"--port={port}",
        f"--username={username}", 
    ])


def run(cmd: List[str]) -> int:
    """Run a command with parameters"""
    logger.info('cmd: %s', ' '.join(cmd))
    child = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdoutdata, stderrdata = child.communicate()

    if stdoutdata:
        logger.info(stdoutdata.decode().strip())
        logger.info('-' * 28)

    if stderrdata:
        logger.info('%s STDERR %s', '-' * 10, '-' * 10)
        logger.info(stderrdata.decode().strip())
        logger.info('-' * 28)

    logger.info("returncode %s", child.returncode)
    return child.returncode