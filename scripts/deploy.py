from ape import project
from ape.cli import get_user_selected_account
import click
from ape.cli import network_option, NetworkBoundCommand, ape_cli_context
from ape.api.networks import LOCAL_NETWORK_NAME

def main():
    account = get_user_selected_account()
    account.deploy(project.CommitReveal)

@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@network_option()
def cli(cli_ctx, network):
    network = cli_ctx.provider.network.name
    if network == LOCAL_NETWORK_NAME or network.endswith("-fork"):
        account = cli_ctx.account_manager.test_accounts[0]
    else:
        account = get_user_selected_account()

    account.deploy(project.CommitReveal)
