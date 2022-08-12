from factory import create_app, register_routers

app = create_app()
register_routers(app, "views")
