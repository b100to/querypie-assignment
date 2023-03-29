from typing import Dict


class EnvVarService:
    def __init__(self):
        self.env_vars: Dict[str, str] = {}

    def create_or_update_env_var(self, key: str, value: str):
        self.env_vars[key] = value

    def get_env_var(self, key: str):
        return self.env_vars.get(key)

    def delete_env_var(self, key: str):
        if key in self.env_vars:
            del self.env_vars[key]


env_var_service = EnvVarService()
