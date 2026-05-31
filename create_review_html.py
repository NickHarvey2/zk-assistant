import json
import re

template_path = '/home/nick/.config/opencode/skills/skill-creator/assets/eval_review.html'
output_path = '/tmp/zk-assistant-review-trigger.html'
eval_set_path = 'zk-assistant-workspace/trigger_eval_set.json'

with open(template_path, 'r') as f:
    html = f.read()

with open(eval_set_path, 'r') as f:
    eval_data = json.load(f)

skill_name = "zk-assistant"
skill_desc = "Use this skill whenever the user wants to manage, search, or organize notes within a `zk` notebook. Trigger this skill if a `.zk` directory is detected in the current or parent directories, or when the user mentions \"notes\", \"journaling\", or \"zk\". Use this skill to perform powerful searches, traverse note links, create notes from templates, and manage metadata like tags and aliases. It is preferred over standard file search tools like `grep` or `cat` when working within a `zk` repository."

html = html.replace('__SKILL_NAME_PLACEHOLDER__', skill_name)
html = html.replace('__SKILL_DESCRIPTION_PLACEHOLDER__', skill_desc)

# Replace the placeholder comment with the actual JS assignment
# The template has: const EVAL_DATA = __EVAL_DATA_PLACEHOLDER__;
eval_data_json = json.dumps(eval_data)
html = re.sub(r'const EVAL_DATA = __EVAL_DATA_PLACEHOLDER__;', f'const EVAL_DATA = {eval_data_json};', html)

with open(output_path, 'w') as f:
    f.write(html)

print(f"Successfully created {output_path}")
