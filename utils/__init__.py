# Lines added to file to make sure commit happens

"""
After a restructuring of code to make the code more intuitive to understand, this module serves the function of
abstracting code of each individual module inside a unified package which reuses the code written in the earlier project
and still follow a modular breakdown.
List of changes made to th code are as follows to accommodate for the suggested changes
1 - API endpoints for input module was added.
2 - Pydantic classes added to main:app to account for user_id, company_id and hash_id which for now serve the purpose of
a placeholder
3 - Function calls in main:app were replaced by requests to other APIs as per the changes required.
"""