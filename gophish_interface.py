from gophish import Gophish
from gophish.models import *
from pip._vendor.distlib.compat import raw_input

api_key = raw_input("Enter your API Key:\n")

host = raw_input("Enter your Host (I.E. https://server.net:3333):\n")
api = Gophish(api_key, host=host, verify=False) # Ignore SSL Errors

group_name = raw_input("Enter your Target Group:\n")
groups = [Group(name=group_name)]

page_name = raw_input("Enter the Name of your Landing Page:\n")
page = Page(name=page_name)

template_name = raw_input("Enter the name of your Template:\n")
template = Template(name=template_name)

smtp_name = raw_input("Enter the name of your Sending Profile:\n")
smtp = SMTP(name=smtp_name)

campaign_name = raw_input("Name your campaign!\n")
campaign = Campaign(name=campaign_name, groups=groups, page=page, template=template, smtp=smtp)

campaign = api.campaigns.post(campaign)

print("Your Campaign ID is: " + campaign.id + "\n")

