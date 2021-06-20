import sublime
import sublime_plugin


class CloseOtherTabs(sublime_plugin.WindowCommand):
    def run(self):
        group, index = self.window.get_sheet_index(self.window.active_sheet())
        self.window.run_command('close_others_by_index', {
            "group": group,
            "index": index
            })
