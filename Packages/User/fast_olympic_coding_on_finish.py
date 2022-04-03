import sublime
import sublime_plugin

from Default.exec import ExecCommand

class FastOlympicCodingOnFinishCommand(ExecCommand):
    
    def run(self, **kwargs):
        print(kwargs)
        super().run(**kwargs)
        
    def on_finished(self, proc):
        super().on_finished(proc)
        
        if proc != self.proc:
            return
        
        if proc.killed:
            self.window.status_message("Build Cancelled")
        else:
            exit_code = proc.exit_code()
            if exit_code == 0 or exit_code is None:
                self.window.active_view().run_command("view_tester", {"action": "make_opd", "use_debugger": False})
            else:
                self.window.status_message("Build Failed")
