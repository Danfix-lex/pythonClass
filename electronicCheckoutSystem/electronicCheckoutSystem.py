from datetime import datetime

def generate_invoice(customer_name, product_names, quantities, prices, discount_percent, cashier_name):
    subtotal = 0
    totals = []
    for quantity, price in zip(quantities, prices):
        item_total = quantity * price
        totals.append(item_total)
        subtotal += item_total

    discount = (discount_percent / 100) * subtotal
    vat = 0.075 * (subtotal - discount)
    total = subtotal - discount + vat

    current_date = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
    invoice = []

    invoice.append("\nSEMICOLON STORES")
    invoice.append("MAIN BRANCH")
    invoice.append("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    invoice.append("TEL: 0329382343")
    invoice.append(f"Date: {current_date}")
    invoice.append(f"Cashier: {cashier_name}")
    invoice.append(f"Customer Name: {customer_name}")
    invoice.append("=" * 47)
    invoice.append(f"{'ITEM':<15} {'QTY':<5} {'PRICE':<10} {'TOTAL(NGN)':<10}")
    invoice.append("=" * 47)

    for name, qty, price, total in zip(product_names, quantities, prices, totals):
        invoice.append(f"{name:<15} {qty:<5} {price:<10.2f} {total:<10.2f}")

    invoice.append("=" * 47)
    invoice.append(f"Sub Total: {'':>24}{subtotal:.2f}")
    invoice.append(f"Discount: {'':>24}{discount:.2f}")
    invoice.append(f"VAT @ 7.5%: {'':>22}{vat:.2f}")
    invoice.append("=" * 47)
    invoice.append(f"Bill Total: {'':>23}{total:.2f}")
    invoice.append("=" * 47)
    invoice.append(f"THIS IS NOT A RECEIPT. KINDLY PAY {total:.2f}")

    return "\n".join(invoice)

