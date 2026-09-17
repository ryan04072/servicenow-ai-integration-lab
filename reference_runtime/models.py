from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import uuid

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"

@dataclass
class Artifact:
    id: str
    artifact_type: str
    name: str
    source: str
    environment: str
    summary: str = ""
    scope: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    evidence_locator: Optional[str] = None
    retrieved_at: Optional[str] = None
    sensitivity: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class Edge:
    from_id: str
    relationship: str
    to_id: str
    confidence: str
    evidence_locator: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class HumanAction:
    action_id: str
    correlation_id: str
    action_type: str
    status: str
    title: str
    requested_from: List[str]
    authoritative_system: str
    allowed_responses: List[str]
    summary: str = ""
    participant_mode: str = "single"
    authoritative_record: Optional[str] = None
    source_url: Optional[str] = None
    recommended_response: Optional[str] = None
    evidence: List[Dict[str, Any]] = field(default_factory=list)
    risk: Optional[str] = None
    created_at: str = field(default_factory=utc_now)
    due_at: Optional[str] = None
    resolved_at: Optional[str] = None
    resolved_by: Optional[str] = None
    decision: Optional[str] = None
    comment: Optional[str] = None
    resume_event: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
