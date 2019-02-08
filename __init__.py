# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class LightSwitchPlugin(octoprint.plugin.EventHandlerPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.SettingsPlugin,
                        octoprint.plugin.AssetPlugin):
	def __init__(self):
		self.IOpin = 19

    def on_event(self, event, payload):
        if event == "PrintStarted":
            self.light_on()
        if event == "PrintFailed":
            self.light_off()
        if event == "PrintDone":
            self.light_off()

    def get_settings_defaults(self):
        return dict(IOpin="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_vars(self):
        return dict(IOpin=self._settings.get(["IOpin"]))

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
         return dict(
             js=["js/helloworld.js"],
             css=["css/helloworld.css"],
             less=["less/helloworld.less"]
         )

	def getVars(self):
		self.IOpin = float(self._settings.get(["IOpin"]))

    def light_on(self):
        self._logger.info("switching light ON")

    def light_off(self):
        self._logger.info("switching light OFF")

__plugin_implementation__ = LightSwitchPlugin()
