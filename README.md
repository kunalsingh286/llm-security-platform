# LLM Security Platform

## Overview

LLM Security Platform is an open-source, production-grade security and governance layer for Large Language Models. It provides centralized protection against prompt injection, data leakage, and policy violations while enabling auditability and red-team evaluation.

The platform acts as a secure gateway between client applications and LLM backends.

---

## Core Capabilities

- Centralized LLM API Gateway
- Rule-Based Prompt Filtering
- Output Safety Enforcement
- Violation Logging
- Policy-Ready Architecture
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

Phase 2: Rule-Based Security Layer (Completed)

---

## Author

Kunal Singh
