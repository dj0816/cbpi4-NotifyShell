
# -*- coding: utf-8 -*-
import os
import subprocess # for shell execution
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
import cbpi
from cbpi.api import *
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase
import requests
from voluptuous.schema_builder import message
from cbpi.api.dataclasses import NotificationType
from cbpi.controller.notification_controller import NotificationController
from cbpi.http_endpoints.http_notification import NotificationHttpEndpoints

logger = logging.getLogger(__name__)

pushover_token = None
pushover_user = None
pushover = None

class NotifyShell(CBPiExtension):

    def __init__(self,cbpi):
        self.cbpi = cbpi
        self._task = asyncio.create_task(self.run())


    async def run(self):
        logger.info('Starting Shell Notifications background task')
        await self.shellUser()
        await self.shellCommand()
        if shell_command is None or shell_command == "" or not shell_command:
            logger.warning('Check Shell Commane is set')
        elif shell_user is None or shell_user == "" or not shell_user:
            logger.warning('Check Shell User is set') 
        else:
            self.listener_ID = self.cbpi.notification.add_listener(self.messageEvent)
            logger.info("Shell Listener ID: {}".format(self.listener_ID))
        pass

    async def shellCommand(self):
        global shell_command
        shell_command = self.cbpi.config.get("shell_command", None)
        if pushover_token is None:
            logger.info("INIT Shell Notification Command")
            try:
                await self.cbpi.config.add("shell_command", "", ConfigType.STRING, "Shell Notification Command")
            except:
                logger.warning('Unable to update config')
                
    async def shellUser(self):
        global shell_user
        shell_user = self.cbpi.config.get("shell_user", None)
        if pushover_user is None:
            logger.info("INIT Shell Notification user")
            try:
                await self.cbpi.config.add("shell_user", "", ConfigType.STRING, "Shell Notification User")
            except:
                logger.warning('Unable to update config')

    async def messageEvent(self, cbpi, title, message, type, action):
            #pushoverData = {}
            #pushoverData["token"] = shell_command
            #pushoverData["user"] = shell_user
            #pushoverData["message"] = message 
            #pushoverData["title"] = title
            #requests.post("https://api.pushover.net/1/messages.json", data=pushoverData)
            logger.warning('DAVID: Trying to send a notification')
            p = subprocess.run("/bin/bash", shell_command, title, messageEvent)

def setup(cbpi):
    cbpi.plugin.register("NotifyShell", NotifyShell)
    pass
