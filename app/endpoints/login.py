from fastapi import APIRouter, Depends
from app.lib.authenticator import Authenticator
from app.models.user import UserInRequest

# TODO: What is dependency_overrides_provider argument to APIRouter?
router = APIRouter()


@router.post("/login", response_model=bool, tags=["login"])
async def login(user_request: UserInRequest, authenticator: Authenticator = Depends(Authenticator)):
    """
    Try this payload:

    ```json
    {
        "username": "hongymagic",
        "password": "password"
    }
    ```
    """
    return authenticator.authenticate(user_request.username, user_request.password)