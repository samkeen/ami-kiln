import time
from uuid import uuid1
import datetime
import click
from kiln.util import log

execution_start_time = time.time()
execution_uuid = uuid1()

executionMetrics = {
    'execution_uuid': execution_uuid,
    'start_timestamp': execution_start_time,
    'start_datetime': datetime.datetime.fromtimestamp(execution_start_time).isoformat(),
    'ami_build_queue_url': '',
    'job_message': None,
    'job_build_template': '',
    'job_build_template_sha': '',
    'created_ami_id': '',
    'created_ami_region': '',
    'ended_in_error': False,
    'end_timestamp': '',
    'end_datetime': '',
    'processing_duration': ''
}


@click.command()
@click.option('--configPath', default=None,
              help='optional override path to the config file')
@click.option('--verbose', is_flag=True,
              help='Verbose mode flag')
def main(configpath, verbose):
    """The kiln script"""
    if verbose:
        click.echo('verbose mode')
    if configpath:
        click.echo('Config Path: ' + configpath)

    logger = log.setup_custom_logger('root', filename='kiln.log')
    logger.debug('Kiln run started')

    logger.info('Kiln run finished')

if __name__ == '__main__':
    main()
