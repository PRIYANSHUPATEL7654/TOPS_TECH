SYSTEM_PROMPT = """You are a professional and helpful food delivery support agent. Responses must not exceed 80 words. Verify order facts before making a decision. Return: Decision, Reason, Next step."""
ALLOWED = {'late delivery', 'missing item', 'wrong item'}

def build_prompt(customer_name, order_id, issue_type):
    if issue_type not in ALLOWED:
        raise ValueError("issue_type must be 'late delivery', 'missing item', or 'wrong item'.")
    user = f"Customer name: {customer_name}\nOrder ID: {order_id}\nIssue type: {issue_type}\nPlease provide support."
    return SYSTEM_PROMPT, user

def main():
    tests = [('Priyanshu', 'FD-1001', 'late delivery'), ('Aarav', 'FD-1002', 'missing item'), ('Meera', 'FD-1003', 'invalid issue')]
    for case in tests:
        try:
            system, user = build_prompt(*case); print('SYSTEM:\n'+system+'\nUSER:\n'+user+'\n')
        except ValueError as e: print('Please correct the request:', e)
if __name__ == '__main__': main()
