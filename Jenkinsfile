library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/openstack_undercloud.git'
  molecule_role_name = 'openstack_undercloud'
  molecule_scenarios = ['openstack']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
