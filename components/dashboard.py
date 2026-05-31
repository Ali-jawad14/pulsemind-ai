"""
PulseMind AI - Presentation Graphics Component.
Generates structural metric gauges and visual data readouts.
"""

import streamlit as st
import plotly.graph_objects as go
from typing import Dict, Any

def render_metrics_dashboard(calc_results: Dict[str, Any]) -> None:
    """Generates an enterprise-tier structural metric readout container using Plotly."""
    score = calc_results["score"]
    status = calc_results["status"]
    
    # Select dynamic UI indicators
    if score > 75:
        indicator_color = "#FF4B4B"
    elif score > 45:
        indicator_color = "#FFA500"
    else:
        indicator_color = "#00D2C4"

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"System Status: {status}", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [0, 1] if score <= 1 else [0, 100], 'tickwidth': 1},
            'bar': {'color': indicator_color},
            'bgcolor': "#1E2335",
            'borderwidth': 2,
            'bordercolor': "#3E4560",
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "#FFFFFF"},
        height=280,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)