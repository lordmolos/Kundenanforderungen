# Kundenanforderungen Framework

Ein umfassendes Framework zur strukturierten Erfassung und Definition von Kundenanforderungen für verschiedene Marktsegmente, Produkte, Baureihen und Zellen. Das Framework unterstützt auch die Findung neuer Geschäftsmodelle.

## A comprehensive framework for finding and defining structured customer requirements across different market segments, products, product lines, and cells. Also supports business model discovery.

## 🎯 Zweck / Purpose

Dieses Framework ermöglicht es Ihnen:
- Strukturierte Kundenanforderungen für verschiedene Marktsegmente zu definieren
- Anforderungen über Produkte, Baureihen und Zellen nachzuverfolgbar zu machen
- Lücken in der Anforderungsabdeckung zu identifizieren
- Neue Geschäftsmodelle basierend auf Kundenanforderungen zu entdecken
- Das Framework für verschiedene Kundensegmente und Produkte wiederzuverwenden

This framework enables you to:
- Define structured customer requirements for different market segments
- Track requirements across products, product lines, and cells
- Identify gaps in requirement coverage
- Discover new business models based on customer requirements
- Reuse the framework for different customer segments and products

## 🏗️ Struktur / Structure

Das Framework besteht aus folgenden Kernkomponenten:

### Core Components

1. **CustomerSegment (Kundensegment)**: Repräsentiert verschiedene Marktsegmente
   - Industrie, Unternehmensgröße, geografisch, verhaltensbezogen
   - Eigenschaften und Metadaten

2. **Requirement (Anforderung)**: Strukturierte Kundenanforderungen
   - Priorität (CRITICAL, HIGH, MEDIUM, LOW)
   - Status (IDENTIFIED, VALIDATED, IN_PROGRESS, IMPLEMENTED, REJECTED)
   - Validierungskriterien
   - Business Value

3. **Cell (Zelle)**: Kleinste Einheit in der Produkthierarchie
   - Spezifikationen
   - Zugeordnete Anforderungen

4. **ProductLine (Baureihe)**: Produktlinie mit mehreren Zellen
   - Zielsegmente
   - Zugeordnete Anforderungen

5. **Product (Produkt)**: Einzelne Produkte
   - Features
   - Zielsegmente
   - Zugeordnete Anforderungen

6. **BusinessModel (Geschäftsmodell)**: Potenzielle Geschäftsmodelle
   - Value Proposition
   - Umsatzströme
   - Schlüsselaktivitäten

## 🚀 Installation

Das Framework benötigt Python 3.7 oder höher.

```bash
# Clone the repository
git clone https://github.com/lordmolos/Kundenanforderungen.git
cd Kundenanforderungen

# No additional dependencies required - uses Python standard library only
```

## 📖 Verwendung / Usage

### Schnellstart / Quick Start

```python
from framework import RequirementsFramework, CustomerSegment, Requirement
from framework.models import SegmentType, Priority

# Create framework instance
framework = RequirementsFramework(name="My Project 2026")

# Add a customer segment
segment = CustomerSegment(
    id="seg_001",
    name="Automotive OEMs",
    segment_type=SegmentType.INDUSTRY,
    description="Large automotive manufacturers",
    characteristics=["High volume", "Safety critical"]
)
framework.add_customer_segment(segment)

# Add a requirement
requirement = Requirement(
    id="req_001",
    title="Fast Charging",
    description="Battery must support fast charging",
    customer_segment_ids=["seg_001"],
    priority=Priority.HIGH
)
framework.add_requirement(requirement)

# Analyze
summary = framework.get_summary()
print(summary)
```

### Vollständiges Beispiel / Complete Example

Siehe `example_usage.py` für ein vollständiges Beispiel mit:
- Mehreren Kundensegmenten
- Anforderungen mit Prioritäten
- Zellen, Baureihen und Produkten
- Geschäftsmodellen
- Analyse und Gap-Identifikation

See `example_usage.py` for a complete example including:
- Multiple customer segments
- Requirements with priorities
- Cells, product lines, and products
- Business models
- Analysis and gap identification

```bash
python example_usage.py
```

## 📋 Templates

Im `templates/` Verzeichnis finden Sie Vorlagen für alle Komponenten:
- Customer Segment Template
- Requirement Template
- Cell Template
- Product Line Template
- Product Template
- Business Model Template

In the `templates/` directory you'll find templates for all components.

## 🔍 Hauptfunktionen / Key Features

### 1. Segment-spezifische Analyse
```python
# Get all requirements for a segment
requirements = framework.get_segment_requirements("seg_001")

# Get all products for a segment
products = framework.get_segment_products("seg_001")
```

### 2. Gap-Analyse / Gap Analysis
```python
# Find uncovered requirements and unvalidated requirements
gaps = framework.find_gaps("seg_001")
print(f"Uncovered: {len(gaps['uncovered_requirements'])}")
print(f"Unvalidated: {len(gaps['unvalidated_requirements'])}")
```

### 3. Anforderungsabdeckung / Requirement Coverage
```python
# Check which products/product lines/cells cover a requirement
coverage = framework.get_requirement_coverage("req_001")
print(f"Products: {len(coverage['products'])}")
print(f"Product Lines: {len(coverage['product_lines'])}")
print(f"Cells: {len(coverage['cells'])}")
```

### 4. Business Model Discovery
```python
# Get suggestions for business models based on requirements
suggestions = framework.suggest_business_models("seg_001")
for suggestion in suggestions:
    print(f"- {suggestion}")
```

### 5. Filtering und Suche / Filtering and Search
```python
# Filter requirements by priority
high_priority = framework.list_requirements(priority=Priority.HIGH)

# Filter by status
validated = framework.list_requirements(status=RequirementStatus.VALIDATED)

# Filter by segment
segment_reqs = framework.list_requirements(segment_id="seg_001")
```

## 🔄 Wiederverwendbarkeit / Reusability

Das Framework ist so konzipiert, dass es für verschiedene Szenarien wiederverwendet werden kann:

The framework is designed to be reusable for different scenarios:

1. **Verschiedene Marktsegmente**: Einfach neue CustomerSegment-Objekte erstellen
2. **Verschiedene Produkte**: Neue Product, ProductLine und Cell Objekte hinzufügen
3. **Verschiedene Projekte**: Mehrere Framework-Instanzen für verschiedene Projekte

1. **Different Market Segments**: Simply create new CustomerSegment objects
2. **Different Products**: Add new Product, ProductLine, and Cell objects
3. **Different Projects**: Multiple framework instances for different projects

## 📊 Datenmodell / Data Model

```
CustomerSegment
    ↓ (1:n)
Requirement
    ↓ (n:m)
Product / ProductLine / Cell
    ↓
BusinessModel
```

Alle Beziehungen werden über IDs verwaltet, was Flexibilität und einfache Serialisierung ermöglicht.

All relationships are managed via IDs, enabling flexibility and easy serialization.

## 🛠️ Erweiterte Nutzung / Advanced Usage

### Status-Tracking
```python
# Update requirement status as it progresses
framework.update_requirement_status("req_001", RequirementStatus.IN_PROGRESS)
framework.update_requirement_status("req_001", RequirementStatus.IMPLEMENTED)
```

### Metadaten nutzen / Using Metadata
```python
# Add custom metadata to any entity
segment.metadata["market_size_usd"] = "5B"
segment.metadata["growth_rate"] = "15%"
requirement.metadata["compliance"] = ["ISO 26262", "UL 2580"]
```

### Multiple Framework Instanzen / Multiple Framework Instances
```python
# Create separate frameworks for different scenarios
framework_2026 = RequirementsFramework(name="2026 Product Planning")
framework_2027 = RequirementsFramework(name="2027 Product Planning")
```

## 🎓 Best Practices

1. **Eindeutige IDs**: Verwenden Sie konsistente ID-Schemas (z.B. `seg_`, `req_`, `prod_`)
2. **Validierungskriterien**: Definieren Sie immer klare Validierungskriterien für Anforderungen
3. **Business Value**: Dokumentieren Sie den Geschäftswert jeder Anforderung
4. **Tags**: Nutzen Sie Tags für einfache Kategorisierung und Filterung
5. **Gap-Analyse**: Führen Sie regelmäßig Gap-Analysen durch
6. **Status Updates**: Halten Sie den Status der Anforderungen aktuell

1. **Unique IDs**: Use consistent ID schemes (e.g., `seg_`, `req_`, `prod_`)
2. **Validation Criteria**: Always define clear validation criteria for requirements
3. **Business Value**: Document the business value of each requirement
4. **Tags**: Use tags for easy categorization and filtering
5. **Gap Analysis**: Perform regular gap analyses
6. **Status Updates**: Keep requirement status up to date

## 📄 Lizenz / License

Dieses Projekt ist Open Source und frei verwendbar.

This project is open source and free to use.

## 🤝 Beitragen / Contributing

Beiträge sind willkommen! Bitte erstellen Sie ein Issue oder Pull Request.

Contributions are welcome! Please create an issue or pull request.

## 📞 Kontakt / Contact

Bei Fragen oder Anregungen öffnen Sie bitte ein Issue im Repository.

For questions or suggestions, please open an issue in the repository.