import os

def get_env_value(env_variable):
    try:
      	return os.environ[env_variable]
    except KeyError:
        print('Set the {} environment variable'.format(env_variable))
        return None
