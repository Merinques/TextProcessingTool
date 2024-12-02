from core.file_handler import load_file, save_file
from core.plugin_loader import load_plugins

class Core:
    def __init__(self, plugin_dir: str):
        self.plugins = load_plugins(plugin_dir)

    def list_plugins(self):
        """
        List all available plugins.
        """
        if not self.plugins:
            print("No plugins available.")
            return
        print("\nAvailable Plugins:")
        for i, plugin_name in enumerate(self.plugins.keys(), start=1):
            print(f"{i}. {plugin_name}")

    def apply_plugin(self, plugin_name: str, text: str) -> str:
        """
        Apply a selected plugin to the given text.
        :param plugin_name: Name of the plugin to apply.
        :param text: Input text to process.
        :return: Processed text.
        """
        if plugin_name in self.plugins:
            return self.plugins[plugin_name](text)
        else:
            print(f"Plugin '{plugin_name}' not found.")
            return text

