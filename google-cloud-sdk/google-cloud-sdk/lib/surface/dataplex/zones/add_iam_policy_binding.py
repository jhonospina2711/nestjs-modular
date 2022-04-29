# -*- coding: utf-8 -*- #
# Copyright 2021 Google Inc. All Rights Reserved.
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
"""`gcloud dataplex zone add-iam-policy-binding` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataplex import zone
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataplex import resource_args
from googlecloudsdk.command_lib.iam import iam_util


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class AddIamPolicyBinding(base.Command):
  """Adds IAM policy binding to a zone."""

  detailed_help = {
      'EXAMPLES':
          """\
          To add an IAM policy binding to a Zone, run:

            $ {command} add-iam-policy-binding projects/{project_id}/locations/{location}/lakes/{lake_id}/zones/{zone_id} --role=roles/dataplex.viewer --member=user:foo@gmail.com
          """,
  }

  @staticmethod
  def Args(parser):
    resource_args.AddZoneResourceArg(parser, 'to add IAM policy binding to.')

    iam_util.AddArgsForAddIamPolicyBinding(parser)

  def Run(self, args):
    zone_ref = args.CONCEPTS.zone.Parse()

    result = zone.AddIamPolicyBinding(zone_ref, args.member, args.role)
    return result
