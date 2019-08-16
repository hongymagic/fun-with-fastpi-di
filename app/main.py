from fastapi import FastAPI

from .lib.authenticator import AuthenticatorConfig
from .config import authenticator_config
from .endpoints import router


app = FastAPI(title="Autha")
app.dependency_overrides[AuthenticatorConfig] = authenticator_config
app.include_router(router)