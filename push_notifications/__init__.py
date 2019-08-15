import pkg_resources


__version__ = "1.6.0" # pkg_resources.require("django-push-notifications")[0].version


class NotificationError(Exception):
	pass
