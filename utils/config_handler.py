# Further code to save and load configurations in JSON format


# import json
# import os

# CONFIG_DIR = "configs"
# os.makedirs(CONFIG_DIR, exist_ok=True)

# def save_config(config, name):
#     filename = os.path.join(CONFIG_DIR, f"config_{name}.json")
#     with open(filename, "w") as f:
#         json.dump(config, f, indent=4)

# def load_config(name):
#     filename = os.path.join(CONFIG_DIR, f"config_{name}.json")
#     if not os.path.isfile(filename):
#         return None
#     with open(filename, "r") as f:
#         return json.load(f)

# def list_configs():
#     files = os.listdir(CONFIG_DIR)
#     configs = [f[7:-5] for f in files if f.startswith("config_") and f.endswith(".json")]
#     return configs

