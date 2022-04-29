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
"""Create Bitbucket Server config command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from googlecloudsdk.api_lib.cloudbuild import cloudbuild_util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.cloudbuild import bitbucketserver_flags
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class CreateAlpha(base.CreateCommand):
  """Create a Bitbucket Server config for use by Google Cloud Build."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
        to capture some information, but behaves like an ArgumentParser.
    """
    parser = bitbucketserver_flags.AddBitbucketServerConfigCreateArgs(parser)
    parser.display_info.AddFormat("""
          table(
            name,
            createTime.date('%Y-%m-%dT%H:%M:%S%Oz', undefined='-'),
            host_uri
          )
        """)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """

    client = cloudbuild_util.GetClientInstance()
    messages = cloudbuild_util.GetMessagesModule()
    bbs = cloudbuild_util.BitbucketServerConfigFromArgs(args, False)

    parent = properties.VALUES.core.project.Get(required=True)
    # Use default region global until Proctor is fully regionalized.
    bbs_region = cloudbuild_util.DEFAULT_REGION
    # Get the parent project ref
    parent_resource = resources.REGISTRY.Create(
        collection='cloudbuild.projects.locations',
        projectsId=parent,
        locationsId=bbs_region)
    # Send the Create request
    created_config = client.projects_locations_bitbucketServerConfigs.Create(
        messages.CloudbuildProjectsLocationsBitbucketServerConfigsCreateRequest(
            parent=parent_resource.RelativeName(), bitbucketServerConfig=bbs))
    bbs_resource = resources.REGISTRY.Parse(
        None,
        collection='cloudbuild.projects.locations.bitbucketServerConfigs',
        api_version='v1',
        params={
            'projectsId': parent,
            'locationsId': bbs_region,
            'bitbucketServerConfigsId': created_config.name,
        })

    log.CreatedResource(bbs_resource)

    return created_config
