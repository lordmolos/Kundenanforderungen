"""
Main framework implementation for customer requirements management.
"""

from typing import List, Dict, Optional, Set
from .models import (
    CustomerSegment, Requirement, Product, ProductLine, Cell, BusinessModel,
    Priority, RequirementStatus, SegmentType
)


class RequirementsFramework:
    """
    Main framework class for managing customer requirements across segments,
    products, product lines, and cells. Supports business model discovery.
    
    This framework is designed to be reusable across different customer segments
    and requirements scenarios.
    """
    
    def __init__(self, name: str = "Customer Requirements Framework"):
        """
        Initialize the framework.
        
        Args:
            name: Name for this framework instance
        """
        self.name = name
        self.customer_segments: Dict[str, CustomerSegment] = {}
        self.requirements: Dict[str, Requirement] = {}
        self.products: Dict[str, Product] = {}
        self.product_lines: Dict[str, ProductLine] = {}
        self.cells: Dict[str, Cell] = {}
        self.business_models: Dict[str, BusinessModel] = {}
    
    # Customer Segment Management
    
    def add_customer_segment(self, segment: CustomerSegment) -> None:
        """Add a customer segment to the framework."""
        self.customer_segments[segment.id] = segment
    
    def get_customer_segment(self, segment_id: str) -> Optional[CustomerSegment]:
        """Get a customer segment by ID."""
        return self.customer_segments.get(segment_id)
    
    def list_customer_segments(self, segment_type: Optional[SegmentType] = None) -> List[CustomerSegment]:
        """
        List all customer segments, optionally filtered by type.
        
        Args:
            segment_type: Optional filter by segment type
            
        Returns:
            List of customer segments
        """
        segments = list(self.customer_segments.values())
        if segment_type:
            segments = [s for s in segments if s.segment_type == segment_type]
        return segments
    
    # Requirement Management
    
    def add_requirement(self, requirement: Requirement) -> None:
        """Add a requirement to the framework."""
        self.requirements[requirement.id] = requirement
    
    def get_requirement(self, requirement_id: str) -> Optional[Requirement]:
        """Get a requirement by ID."""
        return self.requirements.get(requirement_id)
    
    def list_requirements(
        self,
        segment_id: Optional[str] = None,
        priority: Optional[Priority] = None,
        status: Optional[RequirementStatus] = None
    ) -> List[Requirement]:
        """
        List requirements with optional filters.
        
        Args:
            segment_id: Filter by customer segment ID
            priority: Filter by priority level
            status: Filter by status
            
        Returns:
            List of requirements matching the filters
        """
        requirements = list(self.requirements.values())
        
        if segment_id:
            requirements = [r for r in requirements if segment_id in r.customer_segment_ids]
        
        if priority:
            requirements = [r for r in requirements if r.priority == priority]
        
        if status:
            requirements = [r for r in requirements if r.status == status]
        
        return requirements
    
    def update_requirement_status(self, requirement_id: str, status: RequirementStatus) -> bool:
        """
        Update the status of a requirement.
        
        Args:
            requirement_id: ID of the requirement
            status: New status
            
        Returns:
            True if successful, False if requirement not found
        """
        requirement = self.get_requirement(requirement_id)
        if requirement:
            requirement.status = status
            return True
        return False
    
    # Product Management
    
    def add_product(self, product: Product) -> None:
        """Add a product to the framework."""
        self.products[product.id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        return self.products.get(product_id)
    
    def list_products(self, segment_id: Optional[str] = None) -> List[Product]:
        """
        List products, optionally filtered by target segment.
        
        Args:
            segment_id: Filter by customer segment ID
            
        Returns:
            List of products
        """
        products = list(self.products.values())
        if segment_id:
            products = [p for p in products if segment_id in p.target_segments]
        return products
    
    # Product Line Management
    
    def add_product_line(self, product_line: ProductLine) -> None:
        """Add a product line to the framework."""
        self.product_lines[product_line.id] = product_line
    
    def get_product_line(self, product_line_id: str) -> Optional[ProductLine]:
        """Get a product line by ID."""
        return self.product_lines.get(product_line_id)
    
    def list_product_lines(self, segment_id: Optional[str] = None) -> List[ProductLine]:
        """
        List product lines, optionally filtered by target segment.
        
        Args:
            segment_id: Filter by customer segment ID
            
        Returns:
            List of product lines
        """
        product_lines = list(self.product_lines.values())
        if segment_id:
            product_lines = [pl for pl in product_lines if segment_id in pl.target_segments]
        return product_lines
    
    # Cell Management
    
    def add_cell(self, cell: Cell) -> None:
        """Add a cell to the framework."""
        self.cells[cell.id] = cell
    
    def get_cell(self, cell_id: str) -> Optional[Cell]:
        """Get a cell by ID."""
        return self.cells.get(cell_id)
    
    def list_cells(self) -> List[Cell]:
        """List all cells."""
        return list(self.cells.values())
    
    # Business Model Management
    
    def add_business_model(self, business_model: BusinessModel) -> None:
        """Add a business model to the framework."""
        self.business_models[business_model.id] = business_model
    
    def get_business_model(self, business_model_id: str) -> Optional[BusinessModel]:
        """Get a business model by ID."""
        return self.business_models.get(business_model_id)
    
    def list_business_models(self, segment_id: Optional[str] = None) -> List[BusinessModel]:
        """
        List business models, optionally filtered by target segment.
        
        Args:
            segment_id: Filter by customer segment ID
            
        Returns:
            List of business models
        """
        business_models = list(self.business_models.values())
        if segment_id:
            business_models = [bm for bm in business_models if segment_id in bm.target_segments]
        return business_models
    
    # Analysis and Discovery Methods
    
    def get_segment_requirements(self, segment_id: str) -> List[Requirement]:
        """Get all requirements for a specific customer segment."""
        return self.list_requirements(segment_id=segment_id)
    
    def get_segment_products(self, segment_id: str) -> List[Product]:
        """Get all products targeting a specific customer segment."""
        return self.list_products(segment_id=segment_id)
    
    def get_requirement_coverage(self, requirement_id: str) -> Dict[str, List]:
        """
        Analyze which products, product lines, and cells address a requirement.
        
        Args:
            requirement_id: ID of the requirement
            
        Returns:
            Dictionary with lists of products, product_lines, and cells
        """
        coverage = {
            "products": [],
            "product_lines": [],
            "cells": []
        }
        
        for product in self.products.values():
            if requirement_id in product.requirement_ids:
                coverage["products"].append(product)
        
        for product_line in self.product_lines.values():
            if requirement_id in product_line.requirement_ids:
                coverage["product_lines"].append(product_line)
        
        for cell in self.cells.values():
            if requirement_id in cell.requirement_ids:
                coverage["cells"].append(cell)
        
        return coverage
    
    def find_gaps(self, segment_id: str) -> Dict[str, List]:
        """
        Identify gaps for a customer segment.
        
        Finds requirements that are not covered by any products or have
        no validation criteria.
        
        Args:
            segment_id: ID of the customer segment
            
        Returns:
            Dictionary with uncovered requirements and unvalidated requirements
        """
        segment_requirements = self.get_segment_requirements(segment_id)
        
        uncovered = []
        unvalidated = []
        
        for req in segment_requirements:
            coverage = self.get_requirement_coverage(req.id)
            if not any(coverage.values()):
                uncovered.append(req)
            
            if not req.validation_criteria:
                unvalidated.append(req)
        
        return {
            "uncovered_requirements": uncovered,
            "unvalidated_requirements": unvalidated
        }
    
    def suggest_business_models(self, segment_id: str) -> List[str]:
        """
        Suggest potential business models based on segment requirements.
        
        Args:
            segment_id: ID of the customer segment
            
        Returns:
            List of suggestions for business models
        """
        requirements = self.get_segment_requirements(segment_id)
        segment = self.get_customer_segment(segment_id)
        
        suggestions = []
        
        # Analyze requirement patterns
        high_priority_count = len([r for r in requirements if r.priority == Priority.HIGH or r.priority == Priority.CRITICAL])
        
        if high_priority_count > 3:
            suggestions.append(
                f"Premium service model: {high_priority_count} high-priority requirements "
                "suggest potential for premium offerings"
            )
        
        # Analyze tags for patterns
        all_tags = set()
        for req in requirements:
            all_tags.update(req.tags)
        
        if "subscription" in all_tags or "recurring" in all_tags:
            suggestions.append("Subscription-based model: Requirements indicate recurring needs")
        
        if "integration" in all_tags or "api" in all_tags:
            suggestions.append("Platform/API model: Integration requirements suggest platform potential")
        
        if segment and segment.size_estimate:
            suggestions.append(
                f"Scale consideration: Segment size ({segment.size_estimate}) "
                "should inform pricing and delivery model"
            )
        
        return suggestions
    
    # Export and Summary Methods
    
    def get_summary(self) -> Dict[str, int]:
        """
        Get a summary of the framework contents.
        
        Returns:
            Dictionary with counts of each entity type
        """
        return {
            "customer_segments": len(self.customer_segments),
            "requirements": len(self.requirements),
            "products": len(self.products),
            "product_lines": len(self.product_lines),
            "cells": len(self.cells),
            "business_models": len(self.business_models)
        }
    
    def __str__(self):
        summary = self.get_summary()
        return (
            f"RequirementsFramework(name={self.name}, "
            f"segments={summary['customer_segments']}, "
            f"requirements={summary['requirements']}, "
            f"products={summary['products']})"
        )
