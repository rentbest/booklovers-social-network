from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from app.core.config import settings


cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.PRIVATE_KEY,
        lifetime_seconds=3600,
        algorithm="RS256",
        public_key=settings.PUBLIC_KEY,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
