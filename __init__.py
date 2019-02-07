# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class LightSwitchPlugin(octoprint.plugin.EventHandlerPlugin,
                        octoprint.plugin.TemplatePlugin):

    def on_event(self, event, payload):
        if event == "PrintStarted":
            self.light_on()
        if event == "PrintFailed":
            self.light_off()
        if event == "PrintDone":
            self.light_off()

    def light_on(self):
        self._logger.info("switching light ON")

    def light_off(self):
        self._logger.info("switching light OFF")

__plugin_name__ = "Light Switch"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Light switch for OctoPrint"
__plugin_implementation__ = LightSwitchPlugin()
