actions = [["go", "google.com"],
                    ["go", "wikipedia.com"],
                    ["back", 1],
                    ["forward", 1],
                    ["back", 3],
                    ["go", "netflix.com"],
                    ["forward", 3]]
# Output: "netflix.com"


def browser(actions):
    forward_stack = []
    backward_stack = []

    for action, value in actions:
        if action == "go":
            forward_stack.append(value)
            backward_stack = []
        if action == "back":
            for i in range(value):
                if len(forward_stack) > 1:
                    backward_stack.append(forward_stack.pop())
        if action == "forward":
            while backward_stack and value > 0:
                forward_stack.append(backward_stack.pop())
                value-=1
    return forward_stack[-1]
