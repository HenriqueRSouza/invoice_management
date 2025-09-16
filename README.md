# Purchase Orders and Invoice Management System

A comprehensive system for managing Purchase Orders (POs) and Invoices, built with Python and Streamlit. Perfect for companies that need strict control over budgets, suppliers, and approval workflows.

## Key Features

### Purchase Orders (POs) Management
- Complete PO registration with budget control
- Real-time monitoring of available vs used balance
- Automatic supplier linking
- Complete transaction history

### Invoice Control
- Invoice entry linked to POs
- Status tracking (Pending/Paid/Cancelled)
- Automatic budget limit validation
- Auto-generation of payment request texts

### Supplier Management
- Complete registration with CNPJ, Legal Name and Trade Name
- Commercial relationship history
- Expense analysis by supplier

### Analytics and Reports
- Real-time financial metrics dashboard
- Payment status charts
- Monthly expense analysis by supplier
- Budget vs actual comparison
- Dynamic expense table by period
- Excel export with applied filters

### Special Features
- **Smart Copy & Paste**: Automatically generates formatted texts for payment requests
- **SAP Integration**: Direct button to access SAP portal with copied PO
- **Advanced Filters**: By supplier, status, period, amount, etc.
- **Automatic Export**: Excel reports with timestamp

## Technologies Used

- **Python 3.8+**
- **Streamlit** - Interactive web interface
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Visualizations and charts
- **OpenPyXL** - Excel file manipulation
- **Pyperclip** - Clipboard integration

## Quick Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/po-invoice-management.git
cd po-invoice-management
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access in browser**
```
http://localhost:8501
```

## Requirements.txt
```
streamlit>=1.28.0
pandas>=2.0.0
matplotlib>=3.7.0
openpyxl>=3.1.0
pyperclip>=1.8.0
```

## Project Structure

```
po-invoice-management/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # This file
├── fornecedores.xlsx     # Suppliers database (auto-generated)
├── pos.csv              # POs database (auto-generated)
├── notas.csv            # Invoices database (auto-generated)
└── exports/             # Folder for exported files (auto-created)
```

## How to Use

### 1. First Access
- Run the application
- Register your suppliers in the sidebar
- Create your first POs linking to suppliers

### 2. Invoice Entry
- Select an existing PO
- Fill in the invoice data
- System automatically validates available balance
- Register the invoice and track budget consumption

### 3. Management and Control
- Use filters to find specific invoices
- Monitor due dates and payment status
- Generate monthly reports
- Analyze expenses by supplier and period

### 4. Payment Requests
- Select an invoice
- Click "Copy Invoice Data"
- Paste in email/approval system (text already formatted)

### Smart Copy & Paste
The system automatically generates formatted texts for payment requests:

```
Good afternoon,
How are you?.
Could you make this payment? Please find below request and approval.
Invoice attached.

Payment Request – [Description] - [Date]
PO/FB60: [PO Code]
Supplier Code: [Code]
Invoice Number/ND: [Invoice Number]
[...]
```

### SAP Integration
- Automatically copies PO code
- Opens SAP MySAP portal directly
- Accelerates approval process

## Improvement Roadmap

- [ ] **V2.0**: Migration to SQLite database
- [ ] **V2.1**: Authentication and permissions system
- [ ] **V2.2**: REST API for integrations
- [ ] **V2.3**: Automatic due date notifications
- [ ] **V2.4**: OCR for automatic invoice reading
- [ ] **V2.5**: Advanced executive dashboard

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Credits

Developed with care by Henrique Ribeiro

---

**If this project helped you, consider giving it a star in the repository!**