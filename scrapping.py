import requests

access_token = 'EAAU88vZBDJjEBOZBUnC7UUfkuysIOVLQXaFCXKkK1qNNr5lU3vSG2hpcZCsyTOi5ShtFaaw3xYMvAzT1ZCnf10zWpxbbEs5SiQl8jD9oGIRPNagpewv1C6uw7EjEoCenLVLfwWzOFXZCcBZBkAFJkT0IDMkZC1f5h6ukZC5Ka6R4DlZCx3RREqBsurAk2w2TZBeJRZCdMk5tjhnn9llRSg7Gx3B1yP5ZASggDrtDADmtzw7xB5FEJZAGDKIH7kB0luBkRjDNnn1H1MgZDZD'
group_id = 'your_group_id_here'

url = f'https://graph.facebook.com/v12.0/{group_id}/photos?access_token={access_token}'

response = requests.get(url)

# Process the response...
