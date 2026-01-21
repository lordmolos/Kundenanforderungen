"""
Example usage of the Customer Requirements Framework.

This example demonstrates how to use the framework for a fictional
automotive battery manufacturer serving different market segments.
"""

from framework import (
    RequirementsFramework,
    CustomerSegment,
    Requirement,
    Product,
    ProductLine,
    Cell,
    BusinessModel
)
from framework.models import Priority, RequirementStatus, SegmentType


def main():
    # Create a new framework instance
    framework = RequirementsFramework(name="Battery Market Requirements 2026")
    
    # Define customer segments
    segment_automotive = CustomerSegment(
        id="seg_auto_oem",
        name="Automotive OEMs",
        segment_type=SegmentType.INDUSTRY,
        description="Large automotive manufacturers requiring battery systems for electric vehicles",
        characteristics=[
            "High volume requirements",
            "Strict safety standards",
            "Long-term contracts",
            "Integration with vehicle systems"
        ],
        size_estimate="50+ major OEMs globally",
        metadata={"region": "global", "market_maturity": "established"}
    )
    
    segment_energy_storage = CustomerSegment(
        id="seg_energy_storage",
        name="Energy Storage Systems",
        segment_type=SegmentType.INDUSTRY,
        description="Companies building grid-scale and commercial energy storage solutions",
        characteristics=[
            "Stationary applications",
            "Long cycle life requirements",
            "High capacity focus",
            "Grid integration needs"
        ],
        size_estimate="Growing market, 200+ providers",
        metadata={"growth_rate": "high", "regulation_sensitive": True}
    )
    
    segment_small_business = CustomerSegment(
        id="seg_sme",
        name="Small to Medium Enterprises",
        segment_type=SegmentType.COMPANY_SIZE,
        description="SMEs looking for customized battery solutions",
        characteristics=[
            "Custom requirements",
            "Lower volumes",
            "Flexibility focus",
            "Cost-sensitive"
        ],
        size_estimate="1000+ potential customers",
        metadata={"segment_diversity": "high"}
    )
    
    framework.add_customer_segment(segment_automotive)
    framework.add_customer_segment(segment_energy_storage)
    framework.add_customer_segment(segment_small_business)
    
    # Define requirements for automotive segment
    req_fast_charging = Requirement(
        id="req_auto_001",
        title="Fast Charging Capability",
        description="Battery cells must support fast charging up to 3C without degradation",
        customer_segment_ids=["seg_auto_oem"],
        priority=Priority.CRITICAL,
        status=RequirementStatus.VALIDATED,
        tags=["performance", "charging", "automotive"],
        validation_criteria=[
            "Charge rate: 0-80% in 20 minutes",
            "Less than 10% capacity loss after 1000 cycles",
            "Temperature management during fast charge"
        ],
        business_value="Enables competitive EV products with consumer-friendly charging times"
    )
    
    req_safety = Requirement(
        id="req_auto_002",
        title="Safety Certification",
        description="Must meet automotive safety standards including crash test requirements",
        customer_segment_ids=["seg_auto_oem"],
        priority=Priority.CRITICAL,
        status=RequirementStatus.IN_PROGRESS,
        tags=["safety", "certification", "automotive"],
        validation_criteria=[
            "ISO 26262 compliance",
            "UL 2580 certification",
            "Crash test validation"
        ],
        business_value="Required for market entry and customer acceptance"
    )
    
    req_long_cycle = Requirement(
        id="req_energy_001",
        title="Extended Cycle Life",
        description="Minimum 5000 cycles at 80% depth of discharge",
        customer_segment_ids=["seg_energy_storage"],
        priority=Priority.HIGH,
        status=RequirementStatus.IDENTIFIED,
        tags=["longevity", "performance", "energy-storage"],
        validation_criteria=[
            "5000+ cycles demonstrated",
            "80% capacity retention after rated cycles",
            "Predictable degradation pattern"
        ],
        business_value="Reduces total cost of ownership for energy storage applications"
    )
    
    req_modular = Requirement(
        id="req_sme_001",
        title="Modular Design",
        description="Battery system should be easily configurable for different capacities",
        customer_segment_ids=["seg_sme", "seg_energy_storage"],
        priority=Priority.MEDIUM,
        status=RequirementStatus.IDENTIFIED,
        tags=["flexibility", "design", "customization"],
        validation_criteria=[
            "Scalable from 10kWh to 100kWh",
            "Standardized interfaces",
            "Tool-free assembly options"
        ],
        business_value="Enables serving diverse customer needs with fewer SKUs"
    )
    
    framework.add_requirement(req_fast_charging)
    framework.add_requirement(req_safety)
    framework.add_requirement(req_long_cycle)
    framework.add_requirement(req_modular)
    
    # Define cells
    cell_high_power = Cell(
        id="cell_hp_001",
        name="HP-2170 High Power Cell",
        description="21700 format high power density cell optimized for fast charging",
        specifications={
            "format": "21700",
            "capacity": "4.8 Ah",
            "max_charge_rate": "3C",
            "max_discharge_rate": "5C",
            "cycle_life": "1500 cycles @ 1C"
        },
        requirement_ids=["req_auto_001"]
    )
    
    cell_long_life = Cell(
        id="cell_ll_001",
        name="LL-2170 Long Life Cell",
        description="21700 format cell optimized for long cycle life",
        specifications={
            "format": "21700",
            "capacity": "5.0 Ah",
            "max_charge_rate": "1C",
            "max_discharge_rate": "2C",
            "cycle_life": "5000+ cycles @ 0.5C"
        },
        requirement_ids=["req_energy_001"]
    )
    
    framework.add_cell(cell_high_power)
    framework.add_cell(cell_long_life)
    
    # Define product lines
    product_line_automotive = ProductLine(
        id="pl_auto_001",
        name="PowerDrive Automotive Series",
        description="High-performance battery systems for electric vehicles",
        cell_ids=["cell_hp_001"],
        target_segments=["seg_auto_oem"],
        requirement_ids=["req_auto_001", "req_auto_002"]
    )
    
    product_line_stationary = ProductLine(
        id="pl_stat_001",
        name="EnergyStore Stationary Series",
        description="Long-life battery systems for energy storage applications",
        cell_ids=["cell_ll_001"],
        target_segments=["seg_energy_storage"],
        requirement_ids=["req_energy_001", "req_modular"]
    )
    
    framework.add_product_line(product_line_automotive)
    framework.add_product_line(product_line_stationary)
    
    # Define products
    product_ev_pack = Product(
        id="prod_ev_001",
        name="PowerDrive EV 80kWh Pack",
        description="80kWh battery pack for mid-size electric vehicles",
        product_line_id="pl_auto_001",
        target_segments=["seg_auto_oem"],
        requirement_ids=["req_auto_001", "req_auto_002"],
        features=[
            "Fast charging capability (0-80% in 20 min)",
            "Integrated thermal management",
            "Automotive safety certified",
            "10-year warranty"
        ]
    )
    
    product_grid_storage = Product(
        id="prod_grid_001",
        name="EnergyStore 100kWh Module",
        description="Modular 100kWh energy storage unit for grid applications",
        product_line_id="pl_stat_001",
        target_segments=["seg_energy_storage"],
        requirement_ids=["req_energy_001", "req_modular"],
        features=[
            "5000+ cycle life",
            "Scalable configuration",
            "Remote monitoring",
            "15-year warranty"
        ]
    )
    
    framework.add_product(product_ev_pack)
    framework.add_product(product_grid_storage)
    
    # Define a business model
    bm_subscription = BusinessModel(
        id="bm_001",
        name="Battery-as-a-Service",
        description="Subscription-based model where customers pay per kWh delivered",
        target_segments=["seg_sme"],
        value_proposition="Eliminate upfront capital costs and ensure optimal battery performance",
        revenue_streams=[
            "Monthly subscription fees",
            "Usage-based charges (per kWh)",
            "Maintenance and support contracts"
        ],
        key_activities=[
            "Battery health monitoring",
            "Predictive maintenance",
            "Performance optimization",
            "End-of-life recycling"
        ],
        key_resources=[
            "IoT monitoring infrastructure",
            "Service technician network",
            "Recycling partnerships"
        ],
        requirement_ids=["req_modular"]
    )
    
    framework.add_business_model(bm_subscription)
    
    # Demonstrate framework usage
    print("=" * 80)
    print(f"Framework: {framework.name}")
    print("=" * 80)
    print()
    
    # Show summary
    summary = framework.get_summary()
    print("Framework Summary:")
    print(f"  Customer Segments: {summary['customer_segments']}")
    print(f"  Requirements: {summary['requirements']}")
    print(f"  Products: {summary['products']}")
    print(f"  Product Lines: {summary['product_lines']}")
    print(f"  Cells: {summary['cells']}")
    print(f"  Business Models: {summary['business_models']}")
    print()
    
    # Analyze automotive segment
    print("=" * 80)
    print("Analysis: Automotive OEM Segment")
    print("=" * 80)
    
    auto_requirements = framework.get_segment_requirements("seg_auto_oem")
    print(f"\nRequirements for Automotive OEMs: {len(auto_requirements)}")
    for req in auto_requirements:
        print(f"  - [{req.priority.value}] {req.title}")
        print(f"    Status: {req.status.value}")
    
    auto_products = framework.get_segment_products("seg_auto_oem")
    print(f"\nProducts for Automotive OEMs: {len(auto_products)}")
    for prod in auto_products:
        print(f"  - {prod.name}")
        print(f"    Features: {len(prod.features)} features")
    
    # Check for gaps
    gaps = framework.find_gaps("seg_auto_oem")
    print(f"\nGap Analysis:")
    print(f"  Uncovered Requirements: {len(gaps['uncovered_requirements'])}")
    print(f"  Unvalidated Requirements: {len(gaps['unvalidated_requirements'])}")
    
    # Business model suggestions
    print("\n" + "=" * 80)
    print("Business Model Discovery: SME Segment")
    print("=" * 80)
    suggestions = framework.suggest_business_models("seg_sme")
    print("\nSuggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"  {i}. {suggestion}")
    
    # Show requirement coverage
    print("\n" + "=" * 80)
    print("Requirement Coverage Analysis")
    print("=" * 80)
    
    coverage = framework.get_requirement_coverage("req_auto_001")
    print(f"\nCoverage for '{req_fast_charging.title}':")
    print(f"  Products: {len(coverage['products'])}")
    for prod in coverage['products']:
        print(f"    - {prod.name}")
    print(f"  Product Lines: {len(coverage['product_lines'])}")
    for pl in coverage['product_lines']:
        print(f"    - {pl.name}")
    print(f"  Cells: {len(coverage['cells'])}")
    for cell in coverage['cells']:
        print(f"    - {cell.name}")
    
    print("\n" + "=" * 80)
    print("Framework demonstration completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
