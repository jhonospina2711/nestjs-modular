# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to list Transfer operations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json

from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.transfer import name_util
from googlecloudsdk.core import properties
from googlecloudsdk.core.resource import resource_printer


class List(base.ListCommand):
  """Lists Transfer Service transfer operations."""

  detailed_help = {
      'DESCRIPTION':
          """\
      List Transfer Service transfer operations to view their progress details
      at a glance.
      """,
      'EXAMPLES':
          """\
      To list all transfer operations in your current project, run:

        $ {command}

      To list all failed operations in your project, run:

        $ {command} --job-operation-statuses=failed

      To list operations 'foo' and 'bar', run:

        $ {command} --operation-names=foo,bar

      To list all operations in your current project as JSON, which provides
      all fields and formatting available in the API, run:

        $ {command} --format=json
      """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--job-names',
        type=arg_parsers.ArgList(),
        metavar='JOB_NAMES',
        help='The names of the jobs whose operations you want to list. Separate'
        ' multiple job names with commas (e.g., --job-names=foo,bar). If not'
        ' specified, operations for all jobs are listed.')
    parser.add_argument(
        '--operation-names',
        type=arg_parsers.ArgList(),
        metavar='OPERATION_NAMES',
        help='The names of operations you want to list. Separate multiple'
        ' operation names with commas (e.g., --operation-names-name=foo,bar).'
        ' If not specified, all operations are listed.')
    parser.add_argument(
        '--operation-statuses',
        type=arg_parsers.ArgList(),
        metavar='OPERATION_STATUSES',
        help='List only transfer operations with the statuses you'
        " specify. Options include 'in-progress', 'paused', 'success',"
        "'failed', 'aborted'. Separate multiple statuses with commas (e.g.,"
        ' --operation-statuses=failed,aborted).')
    parser.add_argument(
        '--expand-table',
        action='store_true',
        help='Include additional table columns (operation name, start time,'
        ' status, data copied, status, has errors, job name) in command'
        ' output. Tip: increase the size of your terminal before running the'
        ' command.')

  def Display(self, args, resources):
    """API response display logic."""
    if args.expand_table:
      # Removes unwanted "transferJobs/" and "transferOperations/" prefixes.
      # Extract start date from start time string.
      # Remove "s" from repeatInterval seconds and make ISO duration string.
      format_string = """table(
          operations.name.map().slice(19:).map().join(sep='').join(sep='\n'),
          operations.metadata.startTime.map().date().join(
              sep='\n'):label='START TIME',
          operations.metadata.counters.bytesCopiedToSink.map().size().join(
              sep='\n'):label='DATA COPIED',
          operations.metadata.status.join(sep='\n'),
          operations.metadata.errorBreakdowns.map().yesno(yes='Yes').join(
            sep='\n'):label='HAS ERRORS',
          operations.metadata.transferJobName.map().slice(13:).map().join(
            sep='').join(sep='\n'):label='TRANSFER JOB NAME')
      """
    else:
      format_string = """table(
          operations.name.map().slice(19:).map().join(sep='').join(sep='\n'),
          operations.metadata.startTime.map().date('%Y-%m-%d').join(
              sep='\n'):label='START DATE',
          operations.metadata.status.join(sep='\n'))
      """
    resource_printer.Print(resources, format_string)

  def Run(self, args):
    """Command execution logic."""
    client = apis.GetClientInstance('storagetransfer', 'v1')
    messages = apis.GetMessagesModule('storagetransfer', 'v1')

    if args.job_names:
      formatted_job_names = name_util.add_job_prefix(args.job_names)
    else:
      formatted_job_names = None
    if args.operation_names:
      formatted_operation_names = name_util.add_operation_prefix(
          args.operation_names)
    else:
      formatted_operation_names = None
    operation_statuses = args.operation_statuses or None

    filter_dictionary = {
        'jobNames': formatted_job_names,
        'operationNames': formatted_operation_names,
        'transferStatuses': operation_statuses,
        'projectId': properties.VALUES.core.project.Get(),
    }
    filter_string = json.dumps(filter_dictionary)

    return client.transferOperations.List(
        # name is unused but required.
        messages.StoragetransferTransferOperationsListRequest(
            name='transferOperations', filter=filter_string))
