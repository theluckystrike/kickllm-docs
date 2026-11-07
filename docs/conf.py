"""Sphinx configuration for the KickLLM cost documentation."""
project = "KickLLM cost reference"
author = "Michal Lip"
copyright = "2026, Michal Lip"
release = "1.0"
extensions = []
templates_path = []
exclude_patterns = ["_build"]
html_theme = "alabaster"
html_static_path = []
html_title = "KickLLM cost reference"
html_theme_options = {
    "description": "What an LLM API bill is actually made of.",
    "github_user": "theluckystrike",
    "github_repo": "kickllm-docs",
    "github_button": False,
    "fixed_sidebar": True,
}
