from app.lib.authenticator import AuthenticatorConfig


def authenticator_config():
    return AuthenticatorConfig({
        "hongymagic": "password",
        "vincent.zhang": "hello",
    })