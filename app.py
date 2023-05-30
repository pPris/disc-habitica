from flask import Flask, request
from discord_manager import fwdToDiscordParty
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world', 200

@app.route('/quest', methods=['POST'])
def quest_webhook():
    res = request.json
    print(res)
    # todo
    return 'Received quest webhook event', 200

# URI for receiving inbound webhook request
@app.route('/', methods=['POST'])
def webhook():
    # Request contains data as shown at https://habitica.com/apidoc/#api-Webhook
     # .json converts request to Python dictionary
    print(request.json)  # type: dict
    res = request.json

    # <YOUR CODE FOR HANDLING EVENT HERE>
    formattedText = res['chat']['text']
    unformattedText = res['chat']['unformattedText']
    
    isSystem = res['chat']['uuid'] == 'system'
    if (isSystem): 
        sender = ("system")
    else: 
        sender = res['chat']['user']

    fwdToDiscordParty(formattedText, unformattedText, sender)
    # print(res['chat']['info']['user'])
 
    return '', 200 # Return 200 code to the sending webserver
    

if __name__ == "__main__":
    app.run(debug=False)
    # app.run(host='0.0.0.0', port='<your_port>')