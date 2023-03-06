import yaml
import os

class StackNotConfiguredException(Exception):
    pass

class TerraformConfig():
    def __init__(self, stack_id):
        with open("config.yml", "r") as file:
            config = yaml.safe_load(file)

        environment = config[os.environ['ENVIRONMENT']]
        
        backend = environment['backend']
        self._backend_bucket = backend['bucket']
        self._backend_prefix = backend['prefix']
        self._backend_dynamodb_table = backend['dynamodb_table']
        self._backend_region = backend['region']

        self._stack_config = None
        for stack in environment['stacks']:
            if stack['id'] == stack_id:
                self._stack_config = stack
                self._backend_key = self._backend_prefix + stack['state_key']
                break

        if self._stack_config == None:
            raise StackNotConfiguredException(f'No stack configuration for {id}')

        self._provider_access_key = os.environ['AWS_ACCESS_KEY_ID']
        self._provider_secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
        self._provider_session_token = os.environ['AWS_SESSION_TOKEN']

    @property
    def backend_bucket(self):
        return self._backend_bucket
    
    @property
    def backend_key(self):
        return self._backend_key
    
    @property
    def backend_dynamodb_table(self):
        return self._backend_dynamodb_table
    
    @property
    def backend_region(self):
        return self._backend_region
    
    @property
    def stack_config(self):
        return self._stack_config
    
    @property
    def provider_access_key(self):
        return self._provider_access_key
    
    @property
    def provider_secret_key(self):
        return self._provider_secret_key
    
    @property
    def provider_session_token(self):
        return self._provider_session_token
