import os
import importlib.util

def load_plugins(plugin_dir: str):
    """
    Load plugins from the specified directory.
    :plugin_dir: Path to the plugins directory.
    :return: A dictionary of plugin names and their respective process functions.
    """
    plugins = {}
    try:
        for file in os.listdir(plugin_dir):
            if file.endswith(".py"):
                plugin_name = file[:-3]  # Remove .py extension
                plugin_path = os.path.join(plugin_dir, file)
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Ensure the plugin has a 'process' function
                if hasattr(module, 'process') and callable(module.process):
                    plugins[plugin_name] = module.process
                else:
                    print(f"Warning: {plugin_name} does not have a callable 'process' function.")
    except Exception as e:
        print(f"Error loading plugins: {e}")
    return plugins
