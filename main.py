from core.file_handler import load_file, save_file
from core.core import Core

def main():
    print("Welcome to the Text Processing Tool!")

    # Initialize the Core
    core = Core("plugins")

    # Load text file
    file_path = input("Enter the path to the text file: ").strip()
    original_text = load_file(file_path)
    if not original_text:
        print("Failed to load the file. Exiting.")
        return

    # List plugins
    print("\nAvailable Plugins:")
    core.list_plugins()

    # Allow multiple plugin selection
    print("\nSelect one or more plugins to apply by entering their numbers separated by commas (e.g., 1,3,5):")
    choices = input("Enter your choices: ").strip().split(',')

    # Validate choices
    try:
        choices = [int(choice) - 1 for choice in choices]
        plugin_names = [list(core.plugins.keys())[choice] for choice in choices if choice in range(len(core.plugins))]
    except (ValueError, IndexError):
        print("Invalid choices. Exiting.")
        return

    # Apply selected plugins to the original text
    results = []
    for plugin_name in plugin_names:
        print(f"\nApplying plugin: {plugin_name}")
        result = core.apply_plugin(plugin_name, original_text)  # Always use the original text
        results.append(f"Result after '{plugin_name}':\n{result}")
        print(results[-1])

    # Save all results
    output_path = input("\nEnter the path to save the plugin results: ").strip()
    try:
        save_file(output_path, '\n\n'.join(results))
        print(f"Processed results saved to {output_path}.")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
