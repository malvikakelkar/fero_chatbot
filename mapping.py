# mapping.py

def recommend_modules(responses):
    recommended_modules = set()

    # Question 1: Types of transportation services
    q1_responses = responses.get(1, [])
    if 'Long-distance deliveries (between cities or countries)' in q1_responses:
        recommended_modules.update(['Trip Planning', 'Asset Management'])
    if 'Local deliveries (within a city or region)' in q1_responses:
        recommended_modules.update(['Dispatch Coordination', 'Fleet Management'])
    if 'Multi-stop routes (milk runs)' in q1_responses:
        recommended_modules.update(['Trip Planning', 'Capacity Engine'])
    if 'Specialized transport (e.g., refrigerated, hazardous materials, oversized items)' in q1_responses:
        recommended_modules.update(['Compliance Management', 'Exception Management'])
    if 'Parcel and small package delivery' in q1_responses:
        recommended_modules.update(['Weight Dispute Management', 'Dispatch Coordination'])
    if 'Intermodal transport (combining road with rail, sea, or air)' in q1_responses:
        recommended_modules.update(['Intermodal Management'])

    # Question 2: Cross-border operations
    if responses.get(2) == 'Yes':
        recommended_modules.update(['Compliance Management', 'Milestone Management'])

    # Question 3: First-mile, mid-mile, or last-mile deliveries
    q3_responses = responses.get(3, [])
    if 'First Mile' in q3_responses or 'Mid Mile' in q3_responses:
        recommended_modules.update(['Trip Planning', 'Asset Management'])
    if 'Last Mile' in q3_responses:
        recommended_modules.update(['Dispatch Coordination', 'Fleet Management'])

    # Question 4: Types of goods transported
    q4_responses = responses.get(4, [])
    if 'Perishable goods (requiring temperature control)' in q4_responses:
        recommended_modules.update(['Compliance Management', 'Exception Management', 'Asset Management'])
    if 'Hazardous materials' in q4_responses:
        recommended_modules.update(['Compliance Management', 'Exception Management'])
    if 'Oversized or heavy equipment' in q4_responses:
        recommended_modules.update(['Trip Planning', 'Asset Management'])

    # Question 5: Customer type (B2B/B2C)
    q5_response = responses.get(5)
    if q5_response == 'B2C':
        recommended_modules.add('Customer Management')
    elif q5_response == 'B2B':
        recommended_modules.add('Vendor Management')
    elif q5_response == 'Both':
        recommended_modules.update(['Customer Management', 'Vendor Management'])

    # Question 6: Typical load type
    q6_responses = responses.get(6, [])
    if 'Less Than Truckload (LTL) / Loose Cargo' in q6_responses:
        recommended_modules.add('Consolidation Management')

    # Question 7: Fleet ownership
    q7_response = responses.get(7)
    if q7_response in ['Own Fleet', 'Both']:
        recommended_modules.update(['Asset Management', 'Fleet Management'])
    if q7_response in ['Outsource to third-party carriers', 'Both']:
        recommended_modules.update(['Vendor Management', 'Procurement Engine'])

    # Question 10: Track maintenance schedules and asset utilization
    if responses.get(10) == 'Yes':
        recommended_modules.add('Asset Management')

    # Question 13: Manual trip planning
    if responses.get(13) == 'Yes':
        recommended_modules.add('Trip Planning')

    # Question 14: Route optimization priority
    if responses.get(14) == 'Yes':
        recommended_modules.add('Trip Planning')

    # Question 15: Multi-stop deliveries (milk runs)
    if responses.get(15) == 'Yes':
        recommended_modules.add('Capacity Engine')

    # Question 17: Special handling requirements
    if responses.get(17) == 'Yes':
        recommended_modules.update(['Compliance Management', 'Exception Management'])

    # Question 18: Specific delivery windows or time slots
    if responses.get(18) == 'Yes':
        recommended_modules.add('Dispatch Coordination')

    # Question 19: Real-time communication importance
    if responses.get(19) == 'Yes':
        recommended_modules.update(['Dispatch Coordination', 'Milestone Management'])

    # Question 22: ERP/SaaS integration
    if responses.get(22) == 'Yes':
        recommended_modules.add('Document Management')

    # Question 24: Require document management
    if responses.get(24) == 'Yes':
        recommended_modules.add('Document Management')

    # Question 25: Work with multiple transporters or vendors
    if responses.get(25) == 'Yes':
        recommended_modules.update(['Vendor Management', 'Procurement Engine'])

    # Question 26: Managing contracts with vendors/service providers
    if responses.get(26) == 'Yes':
        recommended_modules.add('Contract Management')

    # Question 29: Customers require real-time updates
    if responses.get(29) == 'Yes':
        recommended_modules.add('Milestone Management')

    # Question 30: Automated billing and invoicing
    if responses.get(30) == 'Automated system needed':
        recommended_modules.add('Invoicing Module')

    # Question 31: Need to generate customer quotes
    if responses.get(31) == 'Yes':
        recommended_modules.add('Quotation Engine')

    # Question 32: Complex pricing structures
    if responses.get(32) == 'Yes':
        recommended_modules.add('Pricing Engine')

    # Question 34: Manage permits, zone validations, or comply with regulations
    if responses.get(34) == 'Yes':
        recommended_modules.add('Compliance Management')

    # Question 35: Transport goods requiring safety compliance
    if responses.get(35) == 'Yes':
        recommended_modules.add('Compliance Management')

    # Question 36: Main operational challenges
    q36_responses = responses.get(36, [])
    if 'High operational costs' in q36_responses:
        recommended_modules.add('Trip Planning')
    if 'Inefficient route planning' in q36_responses:
        recommended_modules.add('Trip Planning')
    if 'Lack of real-time visibility' in q36_responses:
        recommended_modules.update(['Milestone Management', 'Dispatch Coordination'])
    if 'Manual and time-consuming processes' in q36_responses:
        recommended_modules.update(['Automation Tools', 'Invoicing Module'])
    if 'Difficulty managing vendors or fleet' in q36_responses:
        recommended_modules.update(['Vendor Management', 'Fleet Management'])
    if 'Inaccurate billing or revenue leakage' in q36_responses:
        recommended_modules.update(['Invoicing Module', 'Charge Code Engine', 'Weight Dispute Management'])
    if 'Compliance issues' in q36_responses:
        recommended_modules.add('Compliance Management')

    # Question 37: Primary goals for automation
    q37_responses = responses.get(37, [])
    if 'Reduce operational costs' in q37_responses:
        recommended_modules.add('Trip Planning')
    if 'Improve efficiency and productivity' in q37_responses:
        recommended_modules.add('Operations Scheduling')
    if 'Enhance customer satisfaction' in q37_responses:
        recommended_modules.add('Customer Management')
    if 'Gain better visibility and control' in q37_responses:
        recommended_modules.update(['Milestone Management', 'Reporting & Analytics'])
    if 'Automate billing and invoicing' in q37_responses:
        recommended_modules.add('Invoicing Module')
    if 'Optimize fleet utilization' in q37_responses:
        recommended_modules.update(['Fleet Management', 'Capacity Engine'])
    if 'Ensure compliance' in q37_responses:
        recommended_modules.add('Compliance Management')

    # Question 40: Interested in advanced reporting and analytics
    if responses.get(40) == 'Yes':
        recommended_modules.add('Reporting & Analytics')

    return recommended_modules

# Module Descriptions
module_descriptions = {
    'Trip Planning': 'Optimizes routes, delivery sequences, and vehicle capacity.',
    'Asset Management': 'Tracks and maintains assets, ensuring efficient utilization.',
    'Dispatch Coordination': 'Facilitates real-time communication between dispatchers, drivers, and customers.',
    'Fleet Management': 'Manages vehicles, drivers, maintenance schedules, and assignments.',
    'Capacity Engine': 'Helps plan ideal fleet capacity and utilization.',
    'Compliance Management': 'Manages permits, validations, and regulatory compliance.',
    'Exception Management': 'Detects and manages operational anomalies.',
    'Milestone Management': 'Provides real-time updates on shipment status to stakeholders.',
    'Vendor Management': 'Manages relationships with multiple transporters or vendors.',
    'Procurement Engine': 'Efficiently procures transportation services and manages suppliers.',
    'Contract Management': 'Handles contracts with vendors and customers, ensuring compliance.',
    'Invoicing Module': 'Automates billing and invoicing processes.',
    'Quotation Engine': 'Generates quick and accurate customer quotes.',
    'Pricing Engine': 'Manages complex pricing structures and negotiations.',
    'Document Management': 'Automates and manages shipping documents.',
    'Consolidation Management': 'Consolidates shipments to optimize loads and reduce costs.',
    'Weight Dispute Management': 'Handles disputes over shipment weights.',
    'Reporting & Analytics': 'Provides data-driven insights and decision-making support.',
    'Customer Management': 'Manages customer relationships, orders, and communications.',
    'Automation Tools': 'Automates manual and time-consuming processes.',
    'Operations Scheduling': 'Efficiently schedules shipments and resources.',
    'Intermodal Management': 'Manages transportation involving multiple modes (road, rail, sea, air).',
    'Charge Code Engine': 'Manages additional charges and ensures accurate invoicing.',
    # Add any other module descriptions as needed
}
