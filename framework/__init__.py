"""
Kundenanforderungen Framework - Customer Requirements Framework

A comprehensive framework for finding and defining structured customer requirements
across different market segments, products, product lines, and cells.
Also supports business model discovery.
"""

from .models import CustomerSegment, Requirement, Product, ProductLine, Cell, BusinessModel
from .framework import RequirementsFramework

__version__ = "1.0.0"
__all__ = [
    "CustomerSegment",
    "Requirement",
    "Product",
    "ProductLine",
    "Cell",
    "BusinessModel",
    "RequirementsFramework",
]
