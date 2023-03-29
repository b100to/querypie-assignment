from fastapi import APIRouter
from models import EnvVar
from services import env_var_service

router = APIRouter()

@router.post("/env-vars/")
def create_or_update_env_var(env_var: EnvVar):
    env_var_service.create_or_update_env_var(env_var.key, env_var.value)
    return {"message": "Environment variable created or updated"}

@router.get("/env-vars/{key}")
def get_env_var(key: str):
    value = env_var_service.get_env_var(key)
    if value:
        return {"key": key, "value": value}
    else:
        return {"message": "Environment variable not found"}

@router.delete("/env-vars/{key}")
def delete_env_var(key: str):
    env_var_service.delete_env_var(key)
    return {"message": "Environment variable deleted"}
