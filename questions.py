questions = [
    # Section 1: Company and Operations Overview
    {
        'id': 1,
        'question': 'What types of transportation services does your company provide?',
        'options': [
            'Long-distance deliveries (between cities or countries)',
            'Local deliveries (within a city or region)',
            'Multi-stop routes (milk runs)',
            'Specialized transport (e.g., refrigerated, hazardous materials, oversized items)',
            'Parcel and small package delivery',
            'Intermodal transport (combining road with rail, sea, or air)'
        ],
        'type': 'multiple',
        'next': 2
    },
    {
        'id': 2,
        'question': 'Do you operate cross-border (international) transportation services?',
        'type': 'yesno',
        'next': 3
    },
    {
        'id': 3,
        'question': 'Do you handle first-mile, mid-mile, or last-mile deliveries?',
        'options': [
            'First Mile (from supplier to manufacturer)',
            'Mid Mile (between facilities)',
            'Last Mile (to the end customer)',
            'All of the above'
        ],
        'type': 'multiple',
        'next': 4
    },
    {
        'id': 4,
        'question': 'What types of goods do you transport?',
        'options': [
            'Containerized goods',
            'Bulk cargo (e.g., grains, minerals)',
            'Perishable goods (requiring temperature control)',
            'Hazardous materials',
            'Oversized or heavy equipment',
            'General goods'
        ],
        'type': 'multiple',
        'next': 5
    },
    {
        'id': 5,
        'question': 'Do you primarily serve businesses (B2B), consumers (B2C), or both?',
        'options': [
            'B2B',
            'B2C',
            'Both'
        ],
        'type': 'single',
        'next': 6
    },
    {
        'id': 6,
        'question': 'What is the typical load type for your shipments?',
        'options': [
            'Full Truckload (FTL) / Full Container Load (FCL)',
            'Less Than Truckload (LTL) / Loose Cargo'
        ],
        'type': 'single',
        'next': 7
    },
    # Section 2: Fleet and Asset Management
    {
        'id': 7,
        'question': 'Do you own your transportation assets (vehicles, equipment), or do you outsource transportation services?',
        'options': [
            'Own Fleet',
            'Outsource to third-party carriers',
            'Both'
        ],
        'type': 'single',
        'next': 8
    },
    {
        'id': 8,
        'question': 'If you own vehicles, what types do you have?',
        'options': [
            'Trailers',
            'Tankers',
            'Flatbeds',
            'Vans/Pickups',
            'Refrigerated trucks (reefers)',
            'Specialized vehicles (e.g., lowboys, auto carriers)'
        ],
        'type': 'multiple',
        'next': 9
    },
    {
        'id': 9,
        'question': 'How many vehicles are in your owned fleet?',
        'type': 'text',
        'next': 10
    },
    {
        'id': 10,
        'question': 'Do you need to track vehicle maintenance schedules and asset utilization?',
        'type': 'yesno',
        'next': 11
    },
    {
        'id': 11,
        'question': 'Do you use GPS or tracking devices on your vehicles?',
        'type': 'yesno',
        'next': 12
    },
    {
        'id': 12,
        'question': 'Are your drivers company employees or third-party contractors?',
        'options': [
            'Company-employed drivers',
            'Third-party drivers',
            'Both'
        ],
        'type': 'single',
        'next': 13
    },
    # Section 3: Operational Processes
    {
        'id': 13,
        'question': 'Do you currently plan your trips and routes manually?',
        'type': 'yesno',
        'next': 14
    },
    {
        'id': 14,
        'question': 'Is optimizing delivery routes and schedules a priority for your business?',
        'type': 'yesno',
        'next': 15
    },
    {
        'id': 15,
        'question': 'Do you handle multi-stop deliveries or pickups in a single trip (milk runs)?',
        'type': 'yesno',
        'next': 16
    },
    {
        'id': 16,
        'question': 'Do your vehicles have specific compartmentalization or partitioning needs (e.g., for different temperature zones)?',
        'type': 'yesno',
        'next': 17
    },
    {
        'id': 17,
        'question': 'Do you need to manage special handling requirements for goods (e.g., hazardous materials, temperature control)?',
        'type': 'yesno',
        'next': 18
    },
    {
        'id': 18,
        'question': 'Do you have specific delivery windows or time slots that must be met?',
        'type': 'yesno',
        'next': 19
    },
    {
        'id': 19,
        'question': 'Is real-time communication with drivers and customers important to your operations?',
        'type': 'yesno',
        'next': 20
    },
    {
        'id': 20,
        'question': 'Do you use any hardware or devices for operational purposes (e.g., GPS devices, mobile apps)?',
        'type': 'yesno',
        'next': 21
    },
    # Section 4: Order and Inventory Management
    {
        'id': 21,
        'question': 'How are orders placed and managed in your system?',
        'options': [
            'Sales team entries',
            'Customer portal',
            'Digital integrations (EDI/API)',
            'Phone calls',
            'Manual entry (e.g., spreadsheets)'
        ],
        'type': 'multiple',
        'next': 22
    },
    {
        'id': 22,
        'question': 'Do you need to integrate with existing ERP or SaaS systems for operations management?',
        'type': 'yesno',
        'next': 23
    },
    {
        'id': 23,
        'question': 'Do you manage inventory or stock movements between warehouses or branches?',
        'type': 'yesno',
        'next': 24
    },
    {
        'id': 24,
        'question': 'Do you require document management for shipping documents (e.g., bills of lading, delivery notes)?',
        'type': 'yesno',
        'next': 25
    },
    # Section 5: Vendor and Customer Relations
    {
        'id': 25,
        'question': 'Do you work with multiple transporters or vendors?',
        'type': 'yesno',
        'next': 26
    },
    {
        'id': 26,
        'question': 'Is managing contracts with vendors or service providers important for your business?',
        'type': 'yesno',
        'next': 27
    },
    {
        'id': 27,
        'question': 'Do you have a preferred list of vendors or transporters?',
        'type': 'yesno',
        'next': 28
    },
    {
        'id': 28,
        'question': 'How many customers do you serve regularly?',
        'type': 'text',
        'next': 29
    },
    {
        'id': 29,
        'question': 'Do your customers require real-time updates on shipment status?',
        'type': 'yesno',
        'next': 30
    },
    {
        'id': 30,
        'question': 'Do you handle billing and invoicing manually or require an automated system?',
        'options': [
            'Manual',
            'Automated system needed'
        ],
        'type': 'single',
        'next': 31
    },
    # Section 6: Pricing and Quotation
    {
        'id': 31,
        'question': 'Do you need to generate quotes for your customers?',
        'type': 'yesno',
        'next': 32
    },
    {
        'id': 32,
        'question': 'Are your pricing structures complex, involving various parameters like routes, vehicle types, and service levels?',
        'type': 'yesno',
        'next': 33
    },
    {
        'id': 33,
        'question': 'Do you negotiate rates with customers and vendors regularly?',
        'type': 'yesno',
        'next': 34
    },
    # Section 7: Compliance and Regulatory Requirements
    {
        'id': 34,
        'question': 'Do you need to manage permits, zone validations, or comply with specific regulations?',
        'type': 'yesno',
        'next': 35
    },
    {
        'id': 35,
        'question': 'Do you transport goods that require compliance with safety standards (e.g., hazardous materials)?',
        'type': 'yesno',
        'next': 36
    },
    # Section 8: Business Challenges and Goals
    {
        'id': 36,
        'question': 'What are the main challenges you face in your operations?',
        'options': [
            'High operational costs',
            'Inefficient route planning',
            'Lack of real-time visibility',
            'Manual and time-consuming processes',
            'Difficulty managing vendors or fleet',
            'Inaccurate billing or revenue leakage',
            'Compliance issues'
        ],
        'type': 'multiple',
        'next': 37
    },
    {
        'id': 37,
        'question': 'What are your primary goals for automation and software implementation?',
        'options': [
            'Reduce operational costs',
            'Improve efficiency and productivity',
            'Enhance customer satisfaction',
            'Gain better visibility and control',
            'Automate billing and invoicing',
            'Optimize fleet utilization',
            'Ensure compliance'
        ],
        'type': 'multiple',
        'next': 38
    },
    # Section 9: Additional Requirements
    {
        'id': 38,
        'question': 'Do you require multi-language support for your operations?',
        'type': 'yesno',
        'next': 39
    },
    {
        'id': 39,
        'question': 'Do you use or require communication platforms like WhatsApp integration for business communication?',
        'type': 'yesno',
        'next': 40
    },
    {
        'id': 40,
        'question': 'Are you interested in advanced reporting and analytics to support decision-making?',
        'type': 'yesno',
        'next': None
    }
]
