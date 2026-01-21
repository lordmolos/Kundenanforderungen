"""
Core data models for the customer requirements framework.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any
from datetime import datetime


class Priority(Enum):
    """Priority levels for requirements."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RequirementStatus(Enum):
    """Status of a requirement."""
    IDENTIFIED = "identified"
    VALIDATED = "validated"
    IN_PROGRESS = "in_progress"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"


class SegmentType(Enum):
    """Types of customer segments."""
    INDUSTRY = "industry"
    COMPANY_SIZE = "company_size"
    GEOGRAPHIC = "geographic"
    BEHAVIORAL = "behavioral"
    CUSTOM = "custom"


@dataclass
class CustomerSegment:
    """
    Represents a customer segment in the market.
    
    Attributes:
        id: Unique identifier for the segment
        name: Name of the customer segment
        segment_type: Type of segmentation
        description: Detailed description of the segment
        characteristics: Key characteristics of this segment
        size_estimate: Estimated market size or customer count
        metadata: Additional metadata as key-value pairs
    """
    id: str
    name: str
    segment_type: SegmentType
    description: str
    characteristics: List[str] = field(default_factory=list)
    size_estimate: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"CustomerSegment(id={self.id}, name={self.name}, type={self.segment_type.value})"


@dataclass
class Requirement:
    """
    Represents a customer requirement.
    
    Attributes:
        id: Unique identifier for the requirement
        title: Short title of the requirement
        description: Detailed description
        customer_segment_ids: List of customer segment IDs this requirement applies to
        priority: Priority level
        status: Current status
        tags: Tags for categorization
        validation_criteria: Criteria to validate if requirement is met
        business_value: Description of business value
        created_at: Timestamp when requirement was created
        metadata: Additional metadata as key-value pairs
    """
    id: str
    title: str
    description: str
    customer_segment_ids: List[str]
    priority: Priority = Priority.MEDIUM
    status: RequirementStatus = RequirementStatus.IDENTIFIED
    tags: List[str] = field(default_factory=list)
    validation_criteria: List[str] = field(default_factory=list)
    business_value: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"Requirement(id={self.id}, title={self.title}, priority={self.priority.value})"


@dataclass
class Cell:
    """
    Represents a cell (smallest unit) in product hierarchy.
    
    Attributes:
        id: Unique identifier for the cell
        name: Name of the cell
        description: Description of the cell
        specifications: Technical specifications
        requirement_ids: Requirements addressed by this cell
        metadata: Additional metadata
    """
    id: str
    name: str
    description: str
    specifications: Dict[str, Any] = field(default_factory=dict)
    requirement_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"Cell(id={self.id}, name={self.name})"


@dataclass
class ProductLine:
    """
    Represents a product line (Baureihe).
    
    Attributes:
        id: Unique identifier for the product line
        name: Name of the product line
        description: Description of the product line
        cell_ids: IDs of cells in this product line
        target_segments: Target customer segments
        requirement_ids: Requirements addressed by this product line
        metadata: Additional metadata
    """
    id: str
    name: str
    description: str
    cell_ids: List[str] = field(default_factory=list)
    target_segments: List[str] = field(default_factory=list)
    requirement_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"ProductLine(id={self.id}, name={self.name})"


@dataclass
class Product:
    """
    Represents a product.
    
    Attributes:
        id: Unique identifier for the product
        name: Name of the product
        description: Description of the product
        product_line_id: ID of the product line this belongs to
        target_segments: Target customer segments
        requirement_ids: Requirements addressed by this product
        features: List of product features
        metadata: Additional metadata
    """
    id: str
    name: str
    description: str
    product_line_id: Optional[str] = None
    target_segments: List[str] = field(default_factory=list)
    requirement_ids: List[str] = field(default_factory=list)
    features: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"Product(id={self.id}, name={self.name})"


@dataclass
class BusinessModel:
    """
    Represents a potential business model.
    
    Attributes:
        id: Unique identifier for the business model
        name: Name of the business model
        description: Description of the business model
        target_segments: Target customer segments
        value_proposition: Value proposition for customers
        revenue_streams: Potential revenue streams
        key_activities: Key activities required
        key_resources: Key resources required
        requirement_ids: Requirements that led to this business model
        metadata: Additional metadata
    """
    id: str
    name: str
    description: str
    target_segments: List[str] = field(default_factory=list)
    value_proposition: str = ""
    revenue_streams: List[str] = field(default_factory=list)
    key_activities: List[str] = field(default_factory=list)
    key_resources: List[str] = field(default_factory=list)
    requirement_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"BusinessModel(id={self.id}, name={self.name})"
