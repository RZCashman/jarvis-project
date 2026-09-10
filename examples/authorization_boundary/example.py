"""
Simple authorization boundary example.

AI capability and system authority are separate concerns.
"""


class AuthorizationPolicy:
    """Defines which actions are permitted."""

    def __init__(self, allowed_actions):
        self.allowed_actions = allowed_actions

    def authorize(self, action):
        return action in self.allowed_actions


def execute_action(action, policy):
    """
    Execution only occurs after authorization.
    """

    if not policy.authorize(action):
        return f"Denied: {action}"

    return f"Executed: {action}"


if __name__ == "__main__":
    policy = AuthorizationPolicy(
        allowed_actions=[
            "read_status"
        ]
    )

    proposed_actions = [
        "read_status",
        "delete_files"
    ]

    for action in proposed_actions:
        print(execute_action(action, policy))