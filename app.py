"""
PulseMind AI - System Orchestrator Core File.
Designed to align perfectly with UN SDG 3 evaluation protocols.
"""

import streamlit as st
from services.groq_service import PulseMindEngine, HealthMetricsModel
from components.inputs import render_telemetry_sidebar
from components.dashboard import render_metrics_dashboard

# Application initialization & presentation configuration
st.set_page_config(
    page_title="PulseMind AI | UN SDG 3 Analytics Workspace",
    page_icon="🧠",
    layout="wide"
)

def run_application_pipeline() -> None:
    """Orchestrates system inputs, business layers, and visual rendering modules."""
    st.title("🧠 PulseMind AI")
    st.caption("Advanced Preventative Well-being Engine & Systems Analytics Architecture (UN SDG 3.4)")
    st.markdown("<hr style='border: 1px solid #3E4560; margin-top: 0;'/>", unsafe_allow_html=True)

    # Instantiate Backend Interface Engine safely
    try:
        engine_instance = PulseMindEngine()
    except ValueError as error_message:
        st.error(str(error_message))
        st.info("System Initialization Halted: Please configure the GROQ_API_KEY inside your environment variables.")
        return

    # Draw input module
    input_state = render_telemetry_sidebar()

    # Layout structure split into control and presentation columns
    col_metric, col_insight = st.columns([1, 1], gap="large")

    if input_state["submit"]:
        try:
            # Structurally validate telemetry input via Pydantic model contracts
            validated_telemetry = HealthMetricsModel(
                sleep_hours=input_state["sleep_hours"],
                work_hours=input_state["work_hours"],
                stress_level=input_state["stress_level"],
                active_minutes=input_state["active_minutes"]
            )
            
            # Execute baseline statistical calculations
            calculated_index = engine_instance.calculate_risk_index(validated_telemetry)
            
            with col_metric:
                st.subheader("📊 Analytical Risk Mapping")
                render_metrics_dashboard(calculated_index)
                
            with col_insight:
                st.subheader("🔮 LPU-Accelerated Wellness Protocol")
                with st.spinner("Processing architectural data nodes..."):
                    ai_report = engine_instance.generate_ai_protocol(validated_telemetry, calculated_index)
                    st.markdown(ai_report)
                    
        except Exception as diagnostic_exception:
            st.error(f"Execution Context Exception Encountered: {str(diagnostic_exception)}")
    else:
        with col_metric:
            st.info("System Status: Standby. Define your telemetry configurations in the panel to begin evaluation pathways.")

if __name__ == "__main__":
    run_application_pipeline()