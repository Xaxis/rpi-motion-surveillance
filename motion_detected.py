import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

COMMASPACE = ', '

def main():
	sender = 'source@gmail.com'
	gmail_password = 'yourpassword!'
	recipients = ['target@gmail.com']
	attachments = []

	# Create the enclosing (outer) message
	outer = MIMEMultipart()
	outer['Subject'] = 'MOTION DETECTED'
	outer['To'] = COMMASPACE.join(recipients)
	outer['From'] = sender
	outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

	# Get most recent captured surveillance
	list_of_images = glob.glob('/home/pi/surveillance/records/*.jpg')
	sorted_list_of_images = sorted(list_of_images, key=os.path.getctime)

	# Add up to 6 attachments when present
	image_list_len = len(list_of_images)
	latest_images = []
	if image_list_len >= 6:
		latest_images = sorted_list_of_images[-6:]
	elif image_list_len >= 5:
		latest_images = sorted_list_of_images[-5:]
	elif image_list_len >= 4:
		latest_images = sorted_list_of_images[-4:]
	elif image_list_len >= 3:
                latest_images = sorted_list_of_images[-3:]
	elif image_list_len >= 2:
                latest_images = sorted_list_of_images[-2:]
	elif image_list_len >= 1:
                latest_images = sorted_list_of_images[-1:]

	# Add captured surveillance to attachments
	attachments.extend(latest_images)

	# Iterate over attachments for the message
	for file in attachments:
		try:
			with open(file, 'rb') as fp:
				msg = MIMEBase('application', "octet-stream")
				msg.set_payload(fp.read())
			encoders.encode_base64(msg)
			msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
			outer.attach(msg)
		except:
			print("Unable to open one of the attachments.")
			raise

	# Stringify the composed message
	composed = outer.as_string()

	# Send motion detected email
	try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
                print("SURVEILLANCE MOTION DETECTED. EMAIL ALERT SENT.")
	except:
		print("SURVEILLANCE MOTION DETECTED. EMAIL ALERT FAILED TO SEND.")
		raise

if __name__ == '__main__' :
	main()