# graph/sop_graph.py
from agents.outline_agent import OutlineAgent
from agents.policy_agent import PolicyAgent
from agents.procedure_agent import ProcedureAgent
from agents.review_agent import ReviewAgent

class SOPWorkflow:
    def __init__(self):
        self.outline = OutlineAgent()
        self.policy = PolicyAgent()
        self.procedure = ProcedureAgent()
        self.review = ReviewAgent()

    def run(self, topic):
        outline = self.outline.run(topic)
        policy = self.policy.run(outline)
        procedure = self.procedure.run(outline)
        review = self.review.run(outline, policy, procedure)
        return {
            "outline": outline,
            "policy": policy,
            "procedure": procedure,
            "review": review
        }
        