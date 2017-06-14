#!/usr/bin/env python3

def create_email_body(customer_name, prosoc_rec):
	customer_name = customer_name
	prosoc_rec = prosoc_rec

	html_body = html = """\
<html>
  <head></head>
  <body>
    <p>""" + customer_name + """ Team,<br><br>
       Analyst, please assess the multiple unique "trojan-activity" events to assess if this is an indicator of compromise. List the signatures (name of Snort events) in the correlation and findings in the "*Additional Information" section.<br><br>
	</p>
	<p> INSERT EMAIL BODY HERE<br><br><br><br><br><br><br><br>
	""" + prosoc_rec + """
	</p>
	
  </body>
</html>
"""
	return html_body