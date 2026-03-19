class Memory:
    def __init__(self, max_history=6):
        self.chat_history = []
        self.user_profile = {}
        self.max_history = max_history

    def add(self, role: str, message: str):
        self.chat_history.append((role, message))

        if len(self.chat_history) > self.max_history:
            self.chat_history.pop(0)

    def get_history(self) -> str:
        return "\n".join([f"{r}: {m}" for r, m in self.chat_history])

    def update_profile(self, key, value):
        self.user_profile[key] = value

    def get_profile_text(self):
        if not self.user_profile:
            return "No user data available"
        return "\n".join([f"{k}: {v}" for k, v in self.user_profile.items()])