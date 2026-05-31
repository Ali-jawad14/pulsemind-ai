"""
PulseMind AI - Input Interface Components.
Handles telemetry entry mechanics cleanly.
"""

import streamlit as st
from typing import Dict, Any

def render_telemetry_sidebar() -> Dict[str, Any]:
    """Builds the primary metric configuration panels inside the workspace sidebar."""
    with st.sidebar:
        st.header("⚡ Telemetry Controls")
        st.markdown("Adjust lifestyle and operational parameters to evaluate systemic fatigue.")
        
        sleep = st.slider("Sleep Duration (Hours)", 3.0, 12.0, 7.0, 0.5)
        work = st.slider("Daily Active Workload (Hours)", 2.0, 16.0, 8.0, 0.5)
        stress = st.slider("Subjective Stress Vector", 1, 10, 5)
        active = st.slider("Physical Activity (Minutes)", 0, 120, 30, 5)
        
        st.markdown("---")
        submit_triggered = st.button("EXECUTE ANALYTICS RUN", use_container_width=True)
        
        return {
            "sleep_hours": sleep,
            "work_hours": work,
            "stress_level": stress,
            "active_minutes": active,
            "submit": submit_triggered
        }