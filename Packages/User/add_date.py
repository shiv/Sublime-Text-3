import datetime, getpass
import sublime, sublime_plugin
import os

class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  "/**\n *    author:  Shivam Gupta\n *    created: " + datetime.date.today().strftime("%d.%m.%Y") + " " + datetime.datetime.now().strftime("%H:%M:%S") + "\n**/\n\n"} )