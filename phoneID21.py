# Loading Developer Libraries
import click, json
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

server_url = 'http://localhost:7001/'

# Request the 402 end-points from the server and assign price and address to variables.
info = requests.get_402_info(url=server_url+'caller-id')
endpoint_info = dict(info)
price = int(endpoint_info['price'])
address = str(endpoint_info['bitcoin-address'])

@click.command()
@click.argument('number')
def cli(number):
    """Access caller id via click command. Outputs json file."""
    sel_url = server_url+'caller-id?number={0}'
    response = requests.get(url=sel_url.format(number))
    name = response.json()
    data = {
        'Name': name['name'],
        'Number': name['number'],
        'URI': name['uri'],
        'Price in satoshis': price
    }
    click.echo(json.dumps(data, indent=2))
