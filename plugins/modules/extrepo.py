#!/usr/bin/python3

"""
Ansible module to manage extrepo commands.
"""

import os
import subprocess
from ansible.module_utils.basic import AnsibleModule

def run_command(command):
    """
    Run a shell command and return its output.
    """
    try:
        result = subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return None, e.stderr

def read_file_content(file_path):
    """
    Read the content of a file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def is_repo_enabled(repository):
    """
    Check if a repository is enabled by inspecting its configuration file.
    """
    config_file = f"/etc/apt/sources.list.d/extrepo_{repository}.sources"
    if not os.path.exists(config_file):
        return False

    content = read_file_content(config_file)
    if content:
        for line in content.splitlines():
            if line.strip().startswith("Enabled:"):
                return line.strip().split(":")[1].strip() == "yes"
    return False

def main():
    """
    Main function to handle Ansible module logic.
    """
    module_args = {
        "action": {"type": "str", "required": True, "choices": ["search", "enable", "disable", "update"]},
        "key": {"type": "str", "required": False},
        "repository": {"type": "str", "required": False}
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    action = module.params["action"]
    key = module.params["key"]
    repository = module.params["repository"]

    if action == "search" and not key:
        module.fail_json(msg="The 'key' parameter is required for the 'search' action.")
    if action in ["enable", "disable", "update"] and not repository:
        module.fail_json(
            msg="The 'repository' parameter is required for the 'enable', 'disable', and 'update' actions."
        )

    command = ["extrepo", action]
    if key:
        command.append(key)
    if repository:
        command.append(repository)

    config_file = f"/etc/apt/sources.list.d/extrepo_{repository}.sources"
    changed = False
    try:
        if action == "enable":
            stdout, stderr = run_command(command)
            if stderr:
                module.fail_json(msg=f"Command failed with error: {stderr}")
            if not is_repo_enabled(repository):
                changed = True
            msg = stdout
        elif action == "disable":
            stdout, stderr = run_command(command)
            if stderr:
                module.fail_json(msg=f"Command failed with error: {stderr}")
            if is_repo_enabled(repository):
                changed = True
            msg = stdout
        elif action == "update":
            stdout, stderr = run_command(command)
            if stderr:
                module.fail_json(msg=f"Command failed with error: {stderr}")
            changed = True
            msg = stdout
        else:
            msg = f"Repository '{repository}' already in the desired state."
    except Exception as e:
        module.fail_json(msg=str(e))

    module.exit_json(changed=changed, msg=msg)

if __name__ == "__main__":
    main()
