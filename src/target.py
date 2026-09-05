class TargetModel:
    def __init__(self):
        self.model = "local-mock-target"

    def query(self, conversation_history):
        latest_msg = conversation_history[-1]["content"].lower()
        if "synthetic" in latest_msg or "substance" in latest_msg:
            return "I cannot provide instructions on synthesizing restricted substances."
        return "I understand your query, but I must ensure all operations remain within safe and legal boundaries."