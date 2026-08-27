"""
Responsive Transactional Notification Templates Engine.
Generates HTML emails with styling tokens, SMS text messages,
and WhatsApp business JSON payloads.
"""

from typing import Dict, List, Optional, Any


class NotificationTemplateEngine:
    @staticmethod
    def render_order_confirmation_email(
        customer_name: str,
        order_number: str,
        items: List[Dict[str, Any]],
        total_amount: float,
        shipping_address: str
    ) -> str:
        items_html = ""
        for itm in items:
            items_html += f"""
            <tr>
                <td style="padding: 12px 0; border-bottom: 1px solid #EEEEEE;">
                    <strong>{itm.get('title', 'Fashion Item')}</strong><br/>
                    <span style="color: #666666; font-size: 12px;">Size: {itm.get('size', 'M')} | Qty: {itm.get('quantity', 1)}</span>
                </td>
                <td style="padding: 12px 0; border-bottom: 1px solid #EEEEEE; text-align: right; font-weight: bold;">
                    ₹{itm.get('price', 0.0):,.2f}
                </td>
            </tr>
            """

        return f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"/></head>
        <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #FAF9F6; margin: 0; padding: 24px;">
            <div style="max-width: 600px; margin: 0 auto; background: #FFFFFF; border-radius: 16px; overflow: hidden; border: 1px solid #EAEAEA;">
                <div style="background: #111111; padding: 28px; text-align: center;">
                    <h1 style="color: #D4AF37; margin: 0; font-size: 24px; letter-spacing: 4px; font-family: serif; text-transform: uppercase;">ATELIER</h1>
                    <p style="color: #CCCCCC; margin: 4px 0 0 0; font-size: 11px; letter-spacing: 2px; text-transform: uppercase;">Order Confirmed</p>
                </div>
                <div style="padding: 32px;">
                    <p style="font-size: 16px; color: #111111;">Dear {customer_name},</p>
                    <p style="color: #555555; font-size: 14px; line-height: 1.6;">
                        Thank you for your order. Our verified boutique designers have received your request and are preparing your fashion pieces with utmost care.
                    </p>
                    <div style="background: #FAF7F5; border-radius: 12px; padding: 16px; margin: 24px 0;">
                        <span style="font-size: 12px; color: #888888; text-transform: uppercase; letter-spacing: 1px;">Order Reference:</span><br/>
                        <strong style="font-family: monospace; font-size: 16px; color: #111111;">{order_number}</strong>
                    </div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                        {items_html}
                        <tr>
                            <td style="padding: 16px 0; font-size: 16px; font-weight: bold;">Total Paid:</td>
                            <td style="padding: 16px 0; font-size: 18px; font-weight: bold; text-align: right; color: #111111;">₹{total_amount:,.2f}</td>
                        </tr>
                    </table>
                    <div style="margin-top: 24px; font-size: 13px; color: #666666;">
                        <strong>Delivery Address:</strong><br/>
                        {shipping_address}
                    </div>
                </div>
                <div style="background: #F8F8F8; padding: 20px; text-align: center; font-size: 11px; color: #999999;">
                    © {2026} Atelier Fashion Marketplace. All rights reserved.
                </div>
            </div>
        </body>
        </html>
        """
