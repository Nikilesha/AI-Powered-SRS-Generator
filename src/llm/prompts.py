def build_srs_prompt(project_scope):
    return f"""
    You are an Expert software analyst and is known to give
    the best software requirement specification document.

    Analyze the following project scope

    Return ONLY valid JSON.

    {{
    "project_name": "",
    "project_domain": "",
    "stakeholders": [],
    "user_roles": [],
    "functional_requirements": [],
    "non_functional_requirements": [],
    "assumptions": [],
    "constraints": []
    }}

    Project Scope:
    {project_scope}

"""