
class DeveloperToolsPrompts:
    """Collection of prompts for analyzing AI models, tools and technologies"""

    # Tool extraction prompts
    TOOL_EXTRACTION_SYSTEM = """You are an AI tech researcher. Extract specific ai tool, library, platform, or service names from articles.
                            Focus on actual AI products/tools that developers can use, not general concepts or features."""

    @staticmethod
    def tool_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
                Article Content: {content}

                Extract a list of specific ai tool/models names mentioned in this content that are relevant to "{query}".

                Rules:
                - Only include actual product names, not generic terms
                - Focus on ai models and tools developers can directly use/implement
                - Include both open source and commercial options
                - Limit to the 5 most relevant models or tools
                - Return just the tool names, one per line, no descriptions

                Example format:
                GPT 4o
                LlAMA 4
                Gemini Flux
                Copilot
                Claude"""

    # Company/Tool analysis prompts
    TOOL_ANALYSIS_SYSTEM = """You are analyzing ai models, tools. 
                            Focus on extracting information relevant to AI researchers and software developers. 
                            Pay special attention to programming languages, model versions, APIs, SDKs, and ai model workflows."""

    # @staticmethod
    # def tool_analysis_user(company_name: str, content: str) -> str:
    #     return f"""Company/Tool: {company_name}
    #             Website Content: {content[:2500]}

    #             Analyze this content from a ai developer's and ai researcher's perspective and provide:
    #             - pricing_model: One of "Free", "Freemium", "Paid", "Enterprise", or "Unknown"
    #             - is_open_source: true if open source, false if proprietary, null if unclear
    #             - tech_stack: List of programming languages, frameworks, databases, APIs, or technologies supported/used
    #             - description: Brief 1-sentence description focusing on what this tool does for developers
    #             - api_available: true if REST API, GraphQL, SDK, or programmatic access is mentioned
    #             - language_support: List of programming languages explicitly supported (e.g., Python, JavaScript, Go, etc.)
    #             - integration_capabilities: List of tools/platforms it integrates with (e.g., GitHub, VS Code, Docker, AWS, etc.)

    #             Focus on developer-relevant features like APIs, SDKs, language support, integrations, and development workflows."""

    @staticmethod
    def tool_analysis_user(company_name: str, content: str) -> str:
        return f"""AI Model: {company_name}
            Content (truncated to 2500 chars):
            {content[:2500]}

            Analyze this content from an AI researcher's and ML engineer's perspective and extract structured information about this AI model. Provide these fields:

            - pricing_model: One of "Free", "Freemium", "Paid", "Enterprise", or "Unknown"
            - license: "Open-source", "Commercial", "Research-only", or null if unclear
            - api_available: true if API access is mentioned, false if not, null if unclear
            - description: A brief 1-2 sentence summary of what the model does
            - modality: List of modalities supported (e.g., "Text", "Vision", "Audio", "Multi-modal")
            - tasks: List of tasks the model is designed for (e.g., "Text generation", "Translation", "Image segmentation")
            - parameters: Number of parameters or model size as text, or null if unspecified
            - training_data: Brief description of training data sources or size if available
            - performance_metrics: List of benchmarks or metrics mentioned (e.g., BLEU, accuracy, FID)
            - language_support: List of human languages supported (e.g., English, Spanish)
            - integration_capabilities: Tools, SDKs, or platforms it integrates with (e.g., Hugging Face, LangChain, AWS)
            - release_date: Date or year the model was released, if mentioned
            - version: Version number or name, if specified

            Focus on details useful to ML engineers and AI researchers, such as model architecture, training data, licensing, modalities, tasks supported, and practical deployment info. Be as complete as the content allows."""


    # Recommendation prompts
    RECOMMENDATIONS_SYSTEM = """You are a senior AI engineer providing quick, concise ai models recommendations. 
                            Keep responses brief and actionable - maximum 3-4 sentences total."""

    @staticmethod
    def recommendations_user(query: str, company_data: str) -> str:
        return f"""AI Developer Query: {query}
                Tools/Technologies Analyzed: {company_data}

                Provide a brief recommendation (3-4 sentences max) covering:
                - Which ai model is best and why
                - Key cost/pricing consideration
                - Main technical advantage

                Be concise and direct - no long explanations needed."""
