import logging
import time
from uuid import uuid1
import datetime

__author__ = 'samkeen'

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

print(executionMetrics)
