"""Illustrative unit-economics calculator.

Use your ACTUAL shipping, fee, refund and CAC inputs before making decisions.
"""
from dataclasses import dataclass

@dataclass
class Economics:
    retail: float
    product: float
    shipping_subsidy: float
    payment_fee_pct: float = 0.029
    payment_fee_fixed: float = 0.30
    ai_render: float = 0.20
    support_reprint_reserve_pct: float = 0.04
    discount_pct: float = 0.0

    def calculate(self):
        net_revenue = self.retail * (1 - self.discount_pct)
        fees = net_revenue * self.payment_fee_pct + self.payment_fee_fixed
        reserve = net_revenue * self.support_reprint_reserve_pct
        contribution = (
            net_revenue
            - self.product
            - self.shipping_subsidy
            - fees
            - self.ai_render
            - reserve
        )
        return {
            "net_revenue": round(net_revenue, 2),
            "fees": round(fees, 2),
            "reserve": round(reserve, 2),
            "contribution_before_cac": round(contribution, 2),
            "contribution_margin_pct": round(100 * contribution / net_revenue, 1)
                if net_revenue else 0,
            "break_even_cac": round(max(contribution, 0), 2),
        }

if __name__ == "__main__":
    examples = {
        "card": Economics(retail=2.99, product=1.10, shipping_subsidy=0.0),
        "puzzle": Economics(retail=29.00, product=10.00, shipping_subsidy=3.00),
        "book": Economics(retail=39.00, product=6.50, shipping_subsidy=4.00),
    }
    for name, e in examples.items():
        print(name, e.calculate())
