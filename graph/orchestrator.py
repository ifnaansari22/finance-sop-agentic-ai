# Orchestrates agent flow

# graph/orchestrator.py
from agents.outline_agent import OutlineAgent
from agents.policy_agent import PolicyAgent
from agents.procedure_agent import ProcedureAgent
from agents.review_agent import ReviewAgent

def run_pipeline(document_text):
    outline = OutlineAgent().generate_outline(document_text)
    policy = PolicyAgent().analyze_policy(document_text)
    procedure = ProcedureAgent().generate_procedure(document_text)
    review = ReviewAgent().review_sop(outline, policy, procedure)
    return outline, policy, procedure, review
