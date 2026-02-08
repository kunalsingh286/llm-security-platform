# LLM Security Platform

## Overview

LLM Security Platform is an open-source, production-grade security and governance layer for Large Language Models. It provides centralized protection against prompt injection, data leakage, and policy violations while enabling auditability and red-team evaluation.

The platform acts as a secure gateway between client applications and LLM backends.

---

## Core Capabilities

- Centralized LLM API Gateway
- Prompt Injection Detection
- Output Policy Enforcement
- Data Leakage Prevention
- Red-Team Testing Framework
- Audit Logging and Monitoring
- Policy-as-Code Engine
- Multi-Model Routing (Ollama)

---

## Architecture

Client → Security Platform → LLM Backend → Security Platform → Client

---

## Tech Stack

- Backend: FastAPI, Python
- Models: Ollama (LLaMA3, DeepSeek, Mistral)
- ML: HuggingFace, spaCy, PyTorch
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

Phase 0: Foundation Setup (In Progress)

---

## Author

Kunal Singh
