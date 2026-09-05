# Setting session timeout explicitly
request.session['otp'] = otp
request.session.set_expiry(300) # 300 seconds = 5 minutes