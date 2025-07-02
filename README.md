# 🗺️ Atlas of All Models

> An **agentic AI-powered app** to crawl the web and build an organized atlas of AI models — their specs, capabilities, limitations, and notable details.  

---

## ✨ What is this?

**Atlas of All Models** is an intelligent research assistant that:
- Searches the web for AI model information
- Extracts structured details about the model
- Saves specs in a consistent, queryable schema

No more manual scraping, no more scattered info — just **clean, structured AI model data** at your fingertips.

---

## 🎯 Project Goal

> Build a reliable, automated system to **collect, analyze, and store information about AI models** available on the internet.

We want to answer questions like:
- "What tasks can this model do?"
- "Is there an API?"
- "How many parameters?"
- "What's the license?"
- "What modalities does it support?"

---

## 🛠️ Core Features

✅ Agentic architecture for autonomous research  
✅ Web search and scraping to find official info  
✅ Structured extraction of AI model details  
✅ Pydantic schemas to validate and store results  
✅ Focus on researcher and engineer needs

---

## 🧩 Data Schema

We extract and store fields like:

- `name`: Model name (e.g., GPT-4, LLaMA-3)
- `developer`: Who made it
- `description`: Short what-it-does summary
- `modality`: Text, Vision, Audio, Multi-modal
- `tasks`: Supported tasks
- `parameters`: Model size
- `license`: Open-source, Commercial, Research-only
- `pricing_model`: Free, Freemium, Paid, Enterprise
- `api_available`: Is there an API?
- `integration_capabilities`: Plugins, SDKs, platforms
- `performance_metrics`: Benchmarks or reported scores
- `release_date`: When it launched
- `version`: Specific version info

---

## ⚡ How It Works

1. **Input a query** (like "Gemini 1.5 official site")
2. **Search** the web (using Firecrawl or other search tools)
3. **Scrape** the content from top results
4. **Analyze** the text with an LLM
5. **Extract** structured model specs using our schema
6. **Store** it for easy querying or use in other apps

---

## 🤖 Agentic Design

We use an "agent" approach:
- Maintains state across steps
- Plans searches and analyses
- Calls LLM to generate structured outputs
- Handles errors and rate limits

This isn't just a one-shot LLM prompt — it's a full workflow.

---

## 🚀 Tech Stack

- Python
- Pydantic for data schemas
- LangChain / LangGraph for agentic workflows
- Firecrawl (or other search/scraping tools)
- Any LLM (OpenAI, Anthropic, Groq, etc.) for text analysis

---
