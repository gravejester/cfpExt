import sublime, sublime_plugin, os

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard(os.path.basename(self.view.file_name()))
		sublime.status_message("Copied filename")

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0

class PathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard(os.path.dirname(self.view.file_name()))
		sublime.status_message("Copied path")

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0