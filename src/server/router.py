from src.server.routers import user, excavation, artifact, place, culture

routers = (
    user.router,
    excavation.router,
    artifact.router,
    user.router,
    place.router,
    culture.router,
    )
