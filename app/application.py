import os.path
from croydon.baseapp import BaseApp
from app.middleware import TimingMiddleware, SessionMiddleware


class Application(BaseApp):

    def __init__(self):
        app_dir = os.path.abspath(os.path.dirname(__file__))
        project_dir = os.path.abspath(os.path.join(app_dir, ".."))
        super().__init__(project_dir=project_dir)

    def setup_routes(self) -> None:
        from .controllers.api.v1.account import account_ctrl
        from .controllers.api.v1.flights import flights_ctrl
        self.include_router(account_ctrl)
        self.include_router(flights_ctrl)

    def setup_middleware(self) -> None:
        self.add_middleware(TimingMiddleware)
        super().setup_middleware()
        self.add_middleware(SessionMiddleware)
