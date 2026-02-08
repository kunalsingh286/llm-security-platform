# LLM Security Platform

## Overview

LLM Security Platform is an open-source, production-grade security and governance layer for Large Language Models. It provides centralized protection against prompt injection, data leakage, and policy violations while enabling auditability and red-team evaluation.

The platform acts as a secure gateway between client applications and LLM backends.

---

## Core Capabilities

- Centralized LLM API Gateway
- Policy-as-Code Engine
- ML-Based Injection Detection
- LLM-as-Judge Security
- Data Loss Prevention (DLP)
- Automatic PII & Secret Redaction
- Ensemble Risk Analysis
- Violation Logging
- Multi-Model Routing (Ollama)

---

## Architecture

Client → Security → LLM → DLP → Client

---

## Tech Stack

- Backend: FastAPI, Python
- Models: Ollama (LLaMA3, DeepSeek, Mistral)
- ML: Transformers, PyTorch, HuggingFace
- Storage: PostgreSQL, Redis
- Infra: Docker, Prometheus
- UI: React, Tailwind

---

## Project Structure

llm-security-platform/
├── backend/
├── ml/
├── policies/
├── redteam/
├── dashboard/
├── infra/
├── docs/
└── README.md

---

## Status

Phase 5: Data Leakage Prevention (Completed)

---

## Author

Kunal Singh
