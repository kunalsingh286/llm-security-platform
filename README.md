# LLM Security Platform

## Overview

LLM Security Platform is an open-source, production-grade security and governance layer for Large Language Models. It provides centralized protection against prompt injection, data leakage, and policy violations while enabling auditability, monitoring, and red-team evaluation.

The platform acts as a secure gateway between client applications and LLM backends.

---

## Core Capabilities

- Centralized LLM API Gateway
- Policy-as-Code Engine
- ML-Based Injection Detection
- LLM-as-Judge Security
- Data Loss Prevention (DLP)
- Automatic PII & Secret Redaction
- Red-Team Attack Simulation
- Defense Scoring System
- Persistent Audit Logging
- Real-Time Admin Dashboard
- Security Analytics
- Multi-Model Routing (Ollama)

---

## Architecture

Client → Security → LLM → DLP → Audit DB → Client  
Dashboard → Audit API → Analytics

---

## Tech Stack

- Backend: FastAPI, Python
- Frontend: React, Tailwind, Recharts
- Models: Ollama (LLaMA3, DeepSeek, Mistral)
- ML: Transformers, PyTorch, HuggingFace
- Storage: SQLite (Audit), PostgreSQL (Optional), Redis
- Infra: Docker, Prometheus
- UI: React, Tailwind

---

## Project Structure

llm-security-platform/
├── backend/
├── ml/
├── policies/
├── redteam/
├── dashboard-ui/
├── infra/
├── docs/
└── README.md

---

## Status

Phase 8: Admin Dashboard (Completed)

---

## Author

Kunal Singh
