from typing import List, Optional, Dict, Any
from pydantic import BaseModel


# class CompanyAnalysis(BaseModel):
#     """Structured output for LLM company analysis focused on developer tools"""
#     pricing_model: str  # Free, Freemium, Paid, Enterprise, Unknown
#     is_open_source: Optional[bool] = None
#     tech_stack: List[str] = []
#     description: str = ""
#     api_available: Optional[bool] = None
#     language_support: List[str] = []
#     integration_capabilities: List[str] = []


class ModelAnalysis(BaseModel):
    """
    Structured output for analyzing AI models. Think of it as the TLDR for the LLM's summary.
    """
    pricing_model: Optional[str] = None  # Free, Freemium, Paid, Enterprise
    license: Optional[str] = None  # Open-source, Commercial, Research-only
    api_available: Optional[bool] = None
    description: str = ""
    modality: List[str] = []  # Text, Vision, Audio, Multi-modal
    tasks: List[str] = []  # Summarized supported tasks
    parameters: Optional[str] = None  # Number of parameters
    performance_metrics: List[str] = []
    language_support: List[str] = []
    integration_capabilities: List[str] = []


# class CompanyInfo(BaseModel):
#     name: str
#     description: str
#     website: str
#     pricing_model: Optional[str] = None
#     is_open_source: Optional[bool] = None
#     tech_stack: List[str] = []
#     competitors: List[str] = []
#     # Developer-specific fields
#     api_available: Optional[bool] = None
#     language_support: List[str] = []
#     integration_capabilities: List[str] = []
#     developer_experience_rating: Optional[str] = None  # Poor, Good, Excellent

class AIModelInfo(BaseModel):
    """
    Detailed info about an AI model. This is the database record / final structured fact
    """
    name: str
    description: str    
    website: Optional[str] = None
    pricing_model: Optional[str] = None
    license: Optional[str] = None
    api_available: Optional[bool] = None
    modality: List[str] = []
    tasks: List[str] = []
    parameters: Optional[str] = None
    training_data: Optional[str] = None
    performance_metrics: List[str] = []
    language_support: List[str] = []
    integration_capabilities: List[str] = []
    release_date: Optional[str] = None
    version: Optional[str] = None

class ResearchState(BaseModel):
    query: str
    extracted_tools: List[str] = []  # Tools extracted from articles
    companies: List[AIModelInfo] = []
    search_results: List[Dict[str, Any]] = []
    analysis: Optional[str] = None
