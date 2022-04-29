# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""Command to list hyperparameter tuning jobs in Vertex AI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.ai.hp_tuning_jobs import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ai import constants
from googlecloudsdk.command_lib.ai import endpoint_util
from googlecloudsdk.command_lib.ai import flags


@base.ReleaseTracks(base.ReleaseTrack.GA, base.ReleaseTrack.BETA,
                    base.ReleaseTrack.ALPHA)
class List(base.ListCommand):
  """List existing hyperparameter tuning jobs.

  ## EXAMPLES

  To list the jobs of project ``example'' in region
  ``us-central1'', run:

    $ {command} --project=example --region=us-central1
  """

  @staticmethod
  def Args(parser):
    flags.AddRegionResourceArg(parser, 'to list hyperparameter tuning jobs')

  def Run(self, args):
    region_ref = args.CONCEPTS.region.Parse()
    region = region_ref.AsDict()['locationsId']
    version = constants.GA_VERSION if self.ReleaseTrack(
    ) == base.ReleaseTrack.GA else constants.BETA_VERSION
    with endpoint_util.AiplatformEndpointOverrides(
        version=version, region=region):
      return client.HpTuningJobsClient(version=version).List(
          region=region_ref.RelativeName())
