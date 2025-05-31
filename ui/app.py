# ui/app.py
import streamlit as st
from graph.sop_graph import SOPWorkflow

st.title("Finance SOP Generator (Agentic AI)")
topic = st.text_input("Enter SOP Topic:")

if st.button("Generate SOP"):
    workflow = SOPWorkflow()
    results = workflow.run(topic)

    st.subheader("Outline:")
    st.write(results["outline"])

    st.subheader("Policy:")
    st.write(results["policy"])
    st.subheader("Procedure:")
    st.write(results["procedure"]) 