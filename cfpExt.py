import sublime, sublime_plugin, os

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(os.path.basename(self.view.file_name()))

class PathToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(os.path.dirname(self.view.file_name()))