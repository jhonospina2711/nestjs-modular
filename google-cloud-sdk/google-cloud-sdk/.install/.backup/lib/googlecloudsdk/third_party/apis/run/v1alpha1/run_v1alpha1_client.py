"""Generated client library for run version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.run.v1alpha1 import run_v1alpha1_messages as messages


class RunV1alpha1(base_api.BaseApiClient):
  """Generated client library for service run version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://run.googleapis.com/'
  MTLS_BASE_URL = 'https://run.mtls.googleapis.com/'

  _PACKAGE = 'run'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'RunV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new run handle."""
    url = url or self.BASE_URL
    super(RunV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.namespaces_domainmappings = self.NamespacesDomainmappingsService(self)
    self.namespaces_jobs = self.NamespacesJobsService(self)
    self.namespaces = self.NamespacesService(self)
    self.projects_locations_domainmappings = self.ProjectsLocationsDomainmappingsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class NamespacesDomainmappingsService(base_api.BaseApiService):
    """Service class for the namespaces_domainmappings resource."""

    _NAME = 'namespaces_domainmappings'

    def __init__(self, client):
      super(RunV1alpha1.NamespacesDomainmappingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new domain mapping.

      Args:
        request: (RunNamespacesDomainmappingsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/domains.cloudrun.com/v1alpha1/namespaces/{namespacesId}/domainmappings',
        http_method='POST',
        method_id='run.namespaces.domainmappings.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='apis/domains.cloudrun.com/v1alpha1/{+parent}/domainmappings',
        request_field='domainMapping',
        request_type_name='RunNamespacesDomainmappingsCreateRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a domain mapping.

      Args:
        request: (RunNamespacesDomainmappingsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/domains.cloudrun.com/v1alpha1/namespaces/{namespacesId}/domainmappings/{domainmappingsId}',
        http_method='DELETE',
        method_id='run.namespaces.domainmappings.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['apiVersion', 'kind', 'orphanDependents', 'propagationPolicy'],
        relative_path='apis/domains.cloudrun.com/v1alpha1/{+name}',
        request_field='',
        request_type_name='RunNamespacesDomainmappingsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a domain mapping.

      Args:
        request: (RunNamespacesDomainmappingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/domains.cloudrun.com/v1alpha1/namespaces/{namespacesId}/domainmappings/{domainmappingsId}',
        http_method='GET',
        method_id='run.namespaces.domainmappings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/domains.cloudrun.com/v1alpha1/{+name}',
        request_field='',
        request_type_name='RunNamespacesDomainmappingsGetRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list domain mappings.

      Args:
        request: (RunNamespacesDomainmappingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDomainMappingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/domains.cloudrun.com/v1alpha1/namespaces/{namespacesId}/domainmappings',
        http_method='GET',
        method_id='run.namespaces.domainmappings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='apis/domains.cloudrun.com/v1alpha1/{+parent}/domainmappings',
        request_field='',
        request_type_name='RunNamespacesDomainmappingsListRequest',
        response_type_name='ListDomainMappingsResponse',
        supports_download=False,
    )

    def ReplaceDomainMapping(self, request, global_params=None):
      r"""Rpc to replace a domain mapping. Only the spec and metadata labels and annotations are modifiable. After the Update request, Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

      Args:
        request: (RunNamespacesDomainmappingsReplaceDomainMappingRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('ReplaceDomainMapping')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceDomainMapping.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/domains.cloudrun.com/v1alpha1/namespaces/{namespacesId}/domainmappings/{domainmappingsId}',
        http_method='PUT',
        method_id='run.namespaces.domainmappings.replaceDomainMapping',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/domains.cloudrun.com/v1alpha1/{+name}',
        request_field='domainMapping',
        request_type_name='RunNamespacesDomainmappingsReplaceDomainMappingRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

  class NamespacesJobsService(base_api.BaseApiService):
    """Service class for the namespaces_jobs resource."""

    _NAME = 'namespaces_jobs'

    def __init__(self, client):
      super(RunV1alpha1.NamespacesJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a job.

      Args:
        request: (RunNamespacesJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/run.googleapis.com/v1alpha1/namespaces/{namespacesId}/jobs',
        http_method='POST',
        method_id='run.namespaces.jobs.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='apis/run.googleapis.com/v1alpha1/{+parent}/jobs',
        request_field='job',
        request_type_name='RunNamespacesJobsCreateRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a job.

      Args:
        request: (RunNamespacesJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/run.googleapis.com/v1alpha1/namespaces/{namespacesId}/jobs/{jobsId}',
        http_method='DELETE',
        method_id='run.namespaces.jobs.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['apiVersion', 'kind', 'propagationPolicy'],
        relative_path='apis/run.googleapis.com/v1alpha1/{+name}',
        request_field='',
        request_type_name='RunNamespacesJobsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get information about a job.

      Args:
        request: (RunNamespacesJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/run.googleapis.com/v1alpha1/namespaces/{namespacesId}/jobs/{jobsId}',
        http_method='GET',
        method_id='run.namespaces.jobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/run.googleapis.com/v1alpha1/{+name}',
        request_field='',
        request_type_name='RunNamespacesJobsGetRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List jobs.

      Args:
        request: (RunNamespacesJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/run.googleapis.com/v1alpha1/namespaces/{namespacesId}/jobs',
        http_method='GET',
        method_id='run.namespaces.jobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='apis/run.googleapis.com/v1alpha1/{+parent}/jobs',
        request_field='',
        request_type_name='RunNamespacesJobsListRequest',
        response_type_name='ListJobsResponse',
        supports_download=False,
    )

  class NamespacesService(base_api.BaseApiService):
    """Service class for the namespaces resource."""

    _NAME = 'namespaces'

    def __init__(self, client):
      super(RunV1alpha1.NamespacesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsDomainmappingsService(base_api.BaseApiService):
    """Service class for the projects_locations_domainmappings resource."""

    _NAME = 'projects_locations_domainmappings'

    def __init__(self, client):
      super(RunV1alpha1.ProjectsLocationsDomainmappingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new domain mapping.

      Args:
        request: (RunProjectsLocationsDomainmappingsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/domainmappings',
        http_method='POST',
        method_id='run.projects.locations.domainmappings.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/domainmappings',
        request_field='domainMapping',
        request_type_name='RunProjectsLocationsDomainmappingsCreateRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a domain mapping.

      Args:
        request: (RunProjectsLocationsDomainmappingsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/domainmappings/{domainmappingsId}',
        http_method='DELETE',
        method_id='run.projects.locations.domainmappings.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['apiVersion', 'kind', 'orphanDependents', 'propagationPolicy'],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='RunProjectsLocationsDomainmappingsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a domain mapping.

      Args:
        request: (RunProjectsLocationsDomainmappingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/domainmappings/{domainmappingsId}',
        http_method='GET',
        method_id='run.projects.locations.domainmappings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='RunProjectsLocationsDomainmappingsGetRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list domain mappings.

      Args:
        request: (RunProjectsLocationsDomainmappingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDomainMappingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/domainmappings',
        http_method='GET',
        method_id='run.projects.locations.domainmappings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='v1alpha1/{+parent}/domainmappings',
        request_field='',
        request_type_name='RunProjectsLocationsDomainmappingsListRequest',
        response_type_name='ListDomainMappingsResponse',
        supports_download=False,
    )

    def ReplaceDomainMapping(self, request, global_params=None):
      r"""Rpc to replace a domain mapping. Only the spec and metadata labels and annotations are modifiable. After the Update request, Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

      Args:
        request: (RunProjectsLocationsDomainmappingsReplaceDomainMappingRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('ReplaceDomainMapping')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceDomainMapping.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/domainmappings/{domainmappingsId}',
        http_method='PUT',
        method_id='run.projects.locations.domainmappings.replaceDomainMapping',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='domainMapping',
        request_type_name='RunProjectsLocationsDomainmappingsReplaceDomainMappingRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(RunV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(RunV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
