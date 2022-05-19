# Craftbeerpi4 NotifyShell Notifications Plugin

## Plugin to forward Craftbeerpi4 Notifications to a shell command

- Installation:

	- Plugin requires cbpi >= 4.0.0.33
	- sudo pip3 install cbpi4-PushOver
	- or installation from github


- Usage:

	- First Installation will add parameters to settings.
	- Configure settings by adding token and user.
	- Restart cbpi

- Parameters:

	- shell_command: your command handling the notification, it gets parameter1=title, parameter2=text
	- shell_user: your user for this service

### Changelog:

- 19.05.22: (0.0.1) Initial Release.
