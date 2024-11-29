from toml_template import load_toml_with_template
import os

print(load_toml_with_template(os.path.join(os.path.dirname(__file__), "config.toml")))