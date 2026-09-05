"""Pydantic data models for the scan pipeline (pydantic v2)."""
from typing import Literal, Optional, Any
from pathlib import Path
from pydantic import BaseModel, Field

ClaimType = Literal["actionable", "informational"]
Status = Literal["covered", "partial", "superseded", "missing", "ambiguous"]
Method = Literal["id", "semantic", "none"]

class Claim(BaseModel):
    id: str
    text: str
    source_file: str
    line_number: int
    section: str
    type: ClaimType = "informational"

class Match(BaseModel):
    master_claim: Claim
    revision_claim: Optional[Claim] = None
    method: Method = "none"
    score: float = 0.0
    status: Status = "missing"      # authoritative (curated if present, else auto)
    auto_status: Optional[str] = None   # the detector's inferred status (for auditing)
    note: str = ""
    auto_note: str = ""
    pipeline: Literal["execute", "presence"] = "presence"  # verification pipeline (item 3)
    model_version: str = "original"  # provenance: original gross-depletion vs corrected (1‴)
    auto_tier: Literal["auto-covered", "candidate", "none"] = "candidate"
    # auto-covered = high-confidence (> auto_covered_threshold): no human check needed.
    # candidate = retrieved but below the auto bar: present to a human.

class NumericResult(BaseModel):
    claim_id: str
    computed: dict = Field(default_factory=dict)
    expected: dict = Field(default_factory=dict)
    errors: dict = Field(default_factory=dict)
    passed: Optional[bool] = None       # None => verdict-style (no pass/fail)
    description: str = ""
    error: str = ""

class ConsistencyIssue(BaseModel):
    line1: int
    sentence1: str
    line2: int
    sentence2: str
    relation: str = "contradict"
    score: float = 0.0
    note: str = ""

class RiskItem(BaseModel):
    claim_id: str
    risk_score: float
    status: Status
    criticality: Literal["high", "medium", "low"]
    reason: str
    type: ClaimType = "informational"

class ScanReport(BaseModel):
    master_path: str
    revision_path: str
    timestamp: str
    config: dict
    matches: list[Match] = Field(default_factory=list)
    numeric: list[NumericResult] = Field(default_factory=list)
    consistency: list[ConsistencyIssue] = Field(default_factory=list)
    risk: list[RiskItem] = Field(default_factory=list)
