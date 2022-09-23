class AppStore:
    APPLICATION = dict()

    def add_application(self, app):
        obj = {app.name: app}
        self.APPLICATION.update(obj)

    def remove_application(self, app):
        self.APPLICATION.pop(app.name)

    def block_application(self, app):
        obj = self.APPLICATION.get(app.name)
        setattr(obj, 'blocked', True)

    def total_apps(self):
        return len(self.APPLICATION)


class Application:
    def __init__(self, name: str, blocked: bool = False):
        self.name = name
        self.blocked = blocked


