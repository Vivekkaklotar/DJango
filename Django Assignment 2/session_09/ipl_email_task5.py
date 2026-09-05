# views.py
from django.core.mail import EmailMultiAlternatives

def send_ipl_welcome_email(user_email, username):
    subject = "🏏 Get Ready for the Ultimate Showdown! Welcome to IPL Fantasy League 2026 🔥"
    text_content = f"Hey {username}, welcome to IPL Fantasy League! Pick your XI and win grand prizes."
    
    html_content = f"""
    <html>
        <body style="background-color: #0b132b; color: white; padding: 30px; font-family: sans-serif;">
            <div style="max-width: 500px; margin: auto; border: 2px solid #5bc0be; padding: 20px; border-radius: 12px; text-align: center;">
                <h1 style="color: #6fffe9;">🏏 Welcome to IPL Fantasy!</h1>
                <p>Hey <strong>{username}</strong>,</p>
                <p>The stadium is roaring and your dream team awaits! Build your playing XI now and climb the global leaderboard.</p>
                <a href="http://127.0.0.1:8000/fantasy/create-team/" style="background: #5bc0be; color: #0b132b; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px; display: inline-block; margin-top: 15px;">Create Your XI Now</a>
            </div>
        </body>
    </html>
    """
    
    msg = EmailMultiAlternatives(subject, text_content, 'fantasy@ipl.com', [user_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()