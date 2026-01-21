# Kundenanforderungen Framework - Quick Start Guide

## Was ist das Framework? / What is the Framework?

Das Kundenanforderungen Framework ist ein strukturiertes System zur Erfassung, Verwaltung und Analyse von Kundenanforderungen über verschiedene Marktsegmente, Produkte und Geschäftsmodelle hinweg.

The Customer Requirements Framework is a structured system for capturing, managing, and analyzing customer requirements across different market segments, products, and business models.

## In 5 Minuten starten / Get Started in 5 Minutes

### 1. Framework erstellen / Create Framework

```python
from framework import RequirementsFramework

framework = RequirementsFramework(name="My Project 2026")
```

### 2. Kundensegment hinzufügen / Add Customer Segment

```python
from framework import CustomerSegment
from framework.models import SegmentType

segment = CustomerSegment(
    id="seg_001",
    name="Enterprise Customers",
    segment_type=SegmentType.COMPANY_SIZE,
    description="Large enterprise customers with complex needs",
    characteristics=["High budget", "Complex integration"]
)

framework.add_customer_segment(segment)
```

### 3. Anforderung definieren / Define Requirement

```python
from framework import Requirement
from framework.models import Priority

requirement = Requirement(
    id="req_001",
    title="API Integration",
    description="Must provide REST API for system integration",
    customer_segment_ids=["seg_001"],
    priority=Priority.HIGH,
    validation_criteria=["RESTful API", "API documentation", "OAuth support"]
)

framework.add_requirement(requirement)
```

### 4. Analyse durchführen / Perform Analysis

```python
# Get summary
summary = framework.get_summary()
print(f"Total requirements: {summary['requirements']}")

# Find gaps
gaps = framework.find_gaps("seg_001")
print(f"Uncovered requirements: {len(gaps['uncovered_requirements'])}")

# Get business model suggestions
suggestions = framework.suggest_business_models("seg_001")
for suggestion in suggestions:
    print(f"- {suggestion}")
```

## Hauptkonzepte / Key Concepts

### Hierarchie / Hierarchy

```
CustomerSegment (Marktsegment)
    ↓
Requirement (Anforderung)
    ↓
Cell (Zelle) → ProductLine (Baureihe) → Product (Produkt)
    ↓
BusinessModel (Geschäftsmodell)
```

### Status-Workflow

```
IDENTIFIED → VALIDATED → IN_PROGRESS → IMPLEMENTED
                ↓
            REJECTED
```

### Prioritäten / Priorities

- **CRITICAL**: Must-have, blocking
- **HIGH**: Very important
- **MEDIUM**: Important
- **LOW**: Nice to have

## Typische Anwendungsfälle / Common Use Cases

### 1. Marktanalyse / Market Analysis
Definieren Sie verschiedene Marktsegmente und ihre spezifischen Anforderungen.
Define different market segments and their specific requirements.

### 2. Produktplanung / Product Planning
Ordnen Sie Anforderungen Produkten, Baureihen und Zellen zu.
Map requirements to products, product lines, and cells.

### 3. Gap-Analyse / Gap Analysis
Identifizieren Sie nicht abgedeckte Anforderungen.
Identify uncovered requirements.

### 4. Business Model Discovery
Entdecken Sie neue Geschäftsmodelle basierend auf Kundenanforderungen.
Discover new business models based on customer requirements.

## Best Practices

1. **Starten Sie mit Segmenten**: Definieren Sie zuerst Ihre Kundensegmente
   **Start with Segments**: Define your customer segments first

2. **Klare Validierungskriterien**: Jede Anforderung sollte messbare Kriterien haben
   **Clear Validation Criteria**: Each requirement should have measurable criteria

3. **Business Value dokumentieren**: Notieren Sie den Geschäftswert jeder Anforderung
   **Document Business Value**: Note the business value of each requirement

4. **Status aktuell halten**: Aktualisieren Sie den Status regelmäßig
   **Keep Status Updated**: Update status regularly

5. **Tags nutzen**: Verwenden Sie Tags für einfaches Filtern und Suchen
   **Use Tags**: Use tags for easy filtering and searching

## Nächste Schritte / Next Steps

1. Siehe `example_usage.py` für ein vollständiges Beispiel
   See `example_usage.py` for a complete example

2. Nutzen Sie die Templates in `templates/TEMPLATES.md`
   Use the templates in `templates/TEMPLATES.md`

3. Lesen Sie die vollständige Dokumentation in `README.md`
   Read the full documentation in `README.md`

## Hilfe / Help

Bei Fragen oder Problemen:
- Lesen Sie die vollständige README
- Schauen Sie sich `example_usage.py` an
- Öffnen Sie ein Issue im Repository

For questions or issues:
- Read the full README
- Check out `example_usage.py`
- Open an issue in the repository
