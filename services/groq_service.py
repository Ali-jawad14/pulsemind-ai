"""
PulseMind AI - Analytical Core Service.
Handles structural data parsing, risk calculations, and enterprise LLM orchestrations via Groq LPU.
"""

import os
import streamlit as st
from typing import Dict, Any
from pydantic import BaseModel, Field, field_validator
from groq import Groq

class HealthMetricsModel(BaseModel):
    """Strict execution model for checking incoming telemetry data integrity."""
    sleep_hours: float = Field(..., ge=0.0, le=24.0)
    work_hours: float = Field(..., ge=0.0, le=24.0)
    stress_level: int = Field(..., ge=1, le=10)
    active_minutes: int = Field(..., ge=0, le=1440)

    @field_validator('stress_level')
    @classmethod
    def validate_stress(cls, value: int) -> int:
        if not 1 <= value <= 10:
            raise ValueError("Stress metric bounds anomaly identified.")
        return value

class PulseMindEngine:
    """Enterprise-tier analytics wrapper for structural health calculations."""
    
    def __init__(self) -> None:
        # Native Streamlit secrets fetch with OS environment fallback
        api_key = None
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        else:
            api_key = os.getenv("GROQ_API_KEY")
            
        if not api_key:
            raise ValueError("Configuration Error: GROQ_API_KEY missing from context environment.")
        
        self.client = Groq(api_key=api_key)
        
        # FUTURE-PROOFING: Pulls model from config, defaults to current stable Llama 3.1
        self.model = "llama-3.1-8b-instant"
        if "GROQ_MODEL" in st.secrets:
            self.model = st.secrets["GROQ_MODEL"]

    def calculate_risk_index(self, metrics: HealthMetricsModel) -> Dict[str, Any]:
        """Calculates structural risk ratios mathematically using telemetry inputs."""
        sleep_deficit = max(0.0, 8.0 - metrics.sleep_hours) * 15
        work_load_penalty = max(0.0, metrics.work_hours - 8.0) * 10
        stress_penalty = metrics.stress_level * 4
        activity_bonus = min(20.0, (metrics.active_minutes / 30.0) * 5)
        
        raw_score = 15 + sleep_deficit + work_load_penalty + stress_penalty - activity_bonus
        final_score = max(5, min(98, int(raw_score)))
        
        status = "Optimal"
        if final_score > 75:
            status = "Critical Burnout Threat"
        elif final_score > 45:
            status = "Elevated Fatigue Risk"
            
        return {"score": final_score, "status": status}

    def generate_ai_protocol(self, metrics: HealthMetricsModel, calculation: Dict[str, Any]) -> str:
        """Triggers structured contextual completion via Groq API targeting UN SDG 3."""
        system_prompt = "You are an enterprise preventative clinical health engine specialized in UN SDG 3. Provide concise, highly actionable mitigation roadmaps."
        
        user_prompt = f"""
        Telemetry Analysis Target:
        - Sleep: {metrics.sleep_hours} hours
        - Daily Workload: {metrics.work_hours} hours
        - Baseline Stress: {metrics.stress_level}/10
        - Physical Output: {metrics.active_minutes} minutes
        - Algorithmic Burnout Core Index: {calculation['score']}% ({calculation['status']})
        
        Formatting Constraints:
        Return your analysis organized under these exact operational headings:
        ### 1. CLINICAL TRAFFIC CONTROL OVERVIEW
        ### 2. IMMEDIATELY DEPLOYABLE MICRO-MITIGATIONS (Provide 3 points)
        ### 3. LONGER-TERM STRATEGIC PREVENTATIVE PATHWAYS
        ### 4. UNITED NATIONS SDG 3 FRAMEWORK ALIGNMENT
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model=self.model,
                temperature=0.3, 
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Strategic analytical bridge failure: {str(e)}"