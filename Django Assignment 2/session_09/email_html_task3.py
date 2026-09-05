# views.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_order_confirmation(user_email, order_data):
    subject = "Swiggy - Order Confirmation"
    text_content = f"Thank you for your order #{order_data['order_id']}!"
    
    # Render HTML template to string
    html_content = render_to_string('emails/order_confirmation.html', {'order': order_data})
    
    msg = EmailMultiAlternatives(subject, text_content, 'orders@swiggy.com', [user_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()