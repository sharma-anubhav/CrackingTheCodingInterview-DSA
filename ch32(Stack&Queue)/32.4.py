actions = [["go", "google.com"],
                    ["go", "wikipedia.com"],
                    ["go", "amazon.com"],
                    ["back", 4],
                    ["go", "youtube.com"],
                    ["go", "netflix.com"],
                    ["back", 1]]
# Output: "youtube.com"

def cur_website(actions):
    stack = []
    for action, wild in actions:
        if action == "go":
            stack.append(wild)
        if action == "back":
            for i in range(wild):
                if len(stack) > 1:
                    stack.pop()
    if stack:
        return stack[-1]
    return []
