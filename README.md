# Group 3 - General Merchandise System - Bulk or Retail

A customer wants to buy items either in bulk or as retail at AE general merchandise store. The system calculates the total cost based on the purchase type and applies a bulk purchase discount for items bought in large quantities.

Key Features:
Purchase Type Selection: The customer can choose between buying products in bulk or retail:

Retail Purchase: The customer buys individual items at the full price.
Bulk Purchase: The customer buys in large quantities (e.g., more than 20 items) and gets a discount on the total price.
Cost Calculation:

If the customer buys in retail, the total cost is simply the price per unit multiplied by the quantity.
For bulk purchases, if the customer buys more than 20 units, a 15% discount is applied.
Discount for Bulk Purchases: The system checks the quantity of items purchased. If it exceeds 20, the system applies a 15% discount on the total price.

Input Validation:

The system ensures that the unit price and quantity are valid numeric values.
It verifies that the purchase type is either "bulk" or "retail".
It ensures that the user provides a valid number of items for purchase.
Display Output:

The system displays the total price after the discount (if applicable) for both retail and bulk purchases.
Example:
A customer buys 30 units of a product priced at $10 each.

If the customer selects bulk, the system applies a 15% discount. The total cost is calculated as:
Total cost = 30 × $10 = $300
Discounted price = $300 × 0.85 = $255
If the customer buys retail, there is no discount, so the total cost is simply:
30 × $10 = $300

# Tech Used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)