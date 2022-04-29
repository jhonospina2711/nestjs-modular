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
"""Approves a Cloud Deploy rollout."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.api_lib.clouddeploy import release
from googlecloudsdk.api_lib.clouddeploy import rollout
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.deploy import release_util
from googlecloudsdk.command_lib.deploy import resource_args
from googlecloudsdk.core import resources
from googlecloudsdk.core.console import console_io

_DETAILED_HELP = {
    'DESCRIPTION':
        '{description}',
    'EXAMPLES':
        """ \
To approve a rollout 'test-rollout' for delivery pipeline 'test-pipeline', release 'test-release' in region 'us-central1', run:

$ {command} test-rollout --delivery-pipeline=test-pipeline --release=test-release --region=us-central1

""",
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Approve(base.CreateCommand):
  """Approves a rollout having an Approval state of "Required"."""
  detailed_help = _DETAILED_HELP

  @staticmethod
  def Args(parser):
    resource_args.AddRolloutResourceArg(parser, positional=True)

  def Run(self, args):
    rollout_ref = args.CONCEPTS.rollout.Parse()
    try:
      rollout_obj = rollout.RolloutClient().Get(rollout_ref.RelativeName())
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(error)

    release_ref = resources.REGISTRY.ParseRelativeName(
        rollout_ref.Parent().RelativeName(),
        collection='clouddeploy.projects.locations.deliveryPipelines.releases')
    try:
      release_obj = release.ReleaseClient().Get(release_ref.RelativeName())
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(error)

    prompt = 'Approving rollout {} from {} to target {}.\n\n'.format(
        rollout_ref.Name(), release_ref.Name(), rollout_obj.targetId)
    release_util.PrintDiff(release_ref, release_obj, prompt=prompt)

    console_io.PromptContinue(cancel_on_no=True)

    return rollout.RolloutClient().Approve(rollout_ref.RelativeName(), True)
