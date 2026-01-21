# Templates for Customer Requirements Framework

This directory contains templates to help you get started with the framework.

## Customer Segment Template

```python
from framework import CustomerSegment
from framework.models import SegmentType

segment = CustomerSegment(
    id="seg_xxx",
    name="Your Segment Name",
    segment_type=SegmentType.INDUSTRY,  # or COMPANY_SIZE, GEOGRAPHIC, BEHAVIORAL, CUSTOM
    description="Detailed description of this customer segment",
    characteristics=[
        "Key characteristic 1",
        "Key characteristic 2",
        "Key characteristic 3"
    ],
    size_estimate="Estimated size of this segment",
    metadata={
        "key1": "value1",
        "key2": "value2"
    }
)
```

## Requirement Template

```python
from framework import Requirement
from framework.models import Priority, RequirementStatus

requirement = Requirement(
    id="req_xxx",
    title="Requirement Title",
    description="Detailed description of the requirement",
    customer_segment_ids=["seg_xxx", "seg_yyy"],  # Which segments need this
    priority=Priority.HIGH,  # CRITICAL, HIGH, MEDIUM, LOW
    status=RequirementStatus.IDENTIFIED,  # IDENTIFIED, VALIDATED, IN_PROGRESS, IMPLEMENTED, REJECTED
    tags=["tag1", "tag2", "tag3"],
    validation_criteria=[
        "Criterion 1 to validate this requirement",
        "Criterion 2 to validate this requirement"
    ],
    business_value="Description of business value this requirement provides"
)
```

## Cell Template

```python
from framework import Cell

cell = Cell(
    id="cell_xxx",
    name="Cell Name",
    description="Description of the cell",
    specifications={
        "spec1": "value1",
        "spec2": "value2",
        "capacity": "X Ah",
        "voltage": "X V"
    },
    requirement_ids=["req_xxx", "req_yyy"]  # Which requirements this cell addresses
)
```

## Product Line Template

```python
from framework import ProductLine

product_line = ProductLine(
    id="pl_xxx",
    name="Product Line Name (Baureihe)",
    description="Description of the product line",
    cell_ids=["cell_xxx", "cell_yyy"],  # Which cells are used
    target_segments=["seg_xxx", "seg_yyy"],  # Which segments this targets
    requirement_ids=["req_xxx", "req_yyy"]  # Which requirements this addresses
)
```

## Product Template

```python
from framework import Product

product = Product(
    id="prod_xxx",
    name="Product Name",
    description="Description of the product",
    product_line_id="pl_xxx",  # Optional: which product line this belongs to
    target_segments=["seg_xxx", "seg_yyy"],
    requirement_ids=["req_xxx", "req_yyy"],
    features=[
        "Feature 1",
        "Feature 2",
        "Feature 3"
    ]
)
```

## Business Model Template

```python
from framework import BusinessModel

business_model = BusinessModel(
    id="bm_xxx",
    name="Business Model Name",
    description="Description of the business model",
    target_segments=["seg_xxx", "seg_yyy"],
    value_proposition="Clear value proposition for customers",
    revenue_streams=[
        "Revenue stream 1",
        "Revenue stream 2"
    ],
    key_activities=[
        "Key activity 1",
        "Key activity 2"
    ],
    key_resources=[
        "Key resource 1",
        "Key resource 2"
    ],
    requirement_ids=["req_xxx", "req_yyy"]  # Requirements that led to this model
)
```

## Complete Workflow Example

```python
from framework import RequirementsFramework

# 1. Create framework instance
framework = RequirementsFramework(name="My Project 2026")

# 2. Add customer segments
framework.add_customer_segment(segment)

# 3. Add requirements
framework.add_requirement(requirement)

# 4. Add cells, product lines, products
framework.add_cell(cell)
framework.add_product_line(product_line)
framework.add_product(product)

# 5. Add business models
framework.add_business_model(business_model)

# 6. Analyze
summary = framework.get_summary()
requirements_for_segment = framework.get_segment_requirements("seg_xxx")
gaps = framework.find_gaps("seg_xxx")
suggestions = framework.suggest_business_models("seg_xxx")

# 7. Check coverage
coverage = framework.get_requirement_coverage("req_xxx")
```
