import json
import re

def verify_iam_role_policy(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return False
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return False
    
    # Check if the JSON data contains the required fields
    if 'PolicyName' not in data or 'PolicyDocument' not in data:
        print("JSON does not contain required fields 'PolicyName' and/or 'PolicyDocument'.")
        return False
    
    # Check PolicyName field
    policy_name = data.get('PolicyName')
    if not isinstance(policy_name, str) or not re.match(r'[\w+=,.@-]+', policy_name):
        print("Invalid 'PolicyName' field format.")
        return False
    if len(policy_name) < 1 or len(policy_name) > 128:
        print("Invalid 'PolicyName' length. It should be between 1 and 128 characters.")
        return False
    
    # Check PolicyDocument field
    policy_document = data.get('PolicyDocument')
    if not isinstance(policy_document, dict):
        print("Invalid 'PolicyDocument' field format.")
        return False
    
    # Check if the PolicyDocument contains 'Version' and 'Statement'
    if 'Version' not in policy_document or 'Statement' not in policy_document:
        print("PolicyDocument does not contain required fields 'Version' and/or 'Statement'.")
        return False
    
    # Check each statement in PolicyDocument
    for statement in policy_document['Statement']:
        # Check if statement is a dictionary
        if not isinstance(statement, dict):
            print("Invalid statement format in PolicyDocument.")
            return False
        
        # Check if Resource field contains a single asterisk
        if statement.get('Resource') == '*':
            print("The 'Resource' field contains a single asterisk in PolicyDocument.")
            return False
    
    # If no statement contains a single asterisk, return True
    return True

# Example usage:
json_file_path = 'jsonfile.json'  # Replace with the path to your JSON file
result = verify_iam_role_policy(json_file_path)
print("Verification result:", result)
