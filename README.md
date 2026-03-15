# Agentic AI for Mutual Fund Financial Reporting

Prototype demonstrating how Agentic AI can automate the review of a **Schedule of Investments (SOI)** from mutual fund financial statements.

The system reads a mutual fund report PDF, extracts the Schedule of Investments section, and performs automated validation using regulatory guidance, historical errors, and financial reporting checklists.

---

## Problem

Fund administrators and financial reporting teams manually review the **Schedule of Investments (SOI)** before publishing financial statements.

Typical review checks include:

- security classification accuracy
- correct footnote references
- pricing anomalies
- duplicate securities
- presentation consistency
- comparison with prior reporting cycle

These reviews are often **manual and checklist-based**.

This project demonstrates how **Agentic AI + RAG** can assist in automating these validation workflows.

---

## Architecture

Mutual Fund Report (PDF)

↓

PDF Extraction Agent

↓

SOI Detection Agent

↓

Structured Data Builder

↓

Validation Agents  
(Classification / Pricing / Footnotes / Sorting)

↓

Prior Cycle Comparison Agent

↓

RAG Knowledge Retrieval  
(Regulations + Review Checklists + Past Errors)

↓

LLM Financial Review Agent

↓

Preventive Control Agent

↓

Financial Reporting Review Summary

---

## Key Capabilities

**Document AI**

Extract Schedule of Investments data directly from financial report PDFs.

**Agentic Workflow**

Multiple agents perform validation tasks such as classification checks and footnote verification.

**RAG Knowledge Base**

Financial reporting rules and historical errors are stored in a vector database for retrieval.

**Financial Reporting Validation**

Automated checks based on common fund administration review procedures.

**Preventive Controls**

The system identifies patterns from past reporting errors and suggests controls to avoid recurrence.

---

## Knowledge Sources (RAG)

The system retrieves contextual knowledge from:

- US GAAP investment company guidance (ASC 946)
- Financial reporting review checklists
- Historical reporting errors from past cycles
- Reviewer feedback

This allows the AI to provide **more accurate financial reporting analysis**.

---

## Repository Structure

---

## Technologies Used

Python

PDF document extraction

Vector database retrieval (RAG)

Large Language Models

Financial reporting validation logic

---

## Use Case

This prototype illustrates how **AI can support financial reporting teams and fund administrators** by automating review workflows and surfacing potential reporting issues earlier in the reporting cycle.

---

## Disclaimer

This project is a **prototype for educational and demonstration purposes** and should not be used for production financial reporting without appropriate validation and controls.
