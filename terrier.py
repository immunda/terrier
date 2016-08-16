import json
import click
import subprocess

CONFIG_FILENAME = "terrier.json"

@click.group()
def cli():
    pass

def _load_config(filename=CONFIG_FILENAME, env=None):
    try:
        with open(filename) as terrier_file:
            conf = json.load(terrier_file)
    except IOError:
        click.echo("Error. Could not find '%s'." % filename)
        exit(1)

    if env is not None:
        env_conf = conf.get(env, None)
        if env_conf is None:
            click.echo("Environment '%s' not found." % env)
            exit(1)
        else:
            return env_conf

    return conf

@cli.command()
@click.argument("name")
def remote(name):
    conf = _load_config(env=name)
    remote_conf = conf.get("remote", None)
    if remote_conf is None:
        click.echo("No remote found for '%s'." % name)

    backend = remote_conf.get("backend", None)
    if backend is None:
        click.echo("No remote backend provided for '%s'." % name)
        exit(1)
    else:
        terraform_cmd = "terraform remote config "
        terraform_cmd += "-backend=%s " % backend
        for key, val in remote_conf.get("config", {}).items():
            terraform_cmd += "-backend-config=\"%s=%s\" " % (key, val)
        terraform_cmd = terraform_cmd.strip()
        subprocess.call(terraform_cmd, shell=True)

# @cli.command()
# def plan(*args, **kwargs):
#     click.echo(args)
#     click.echo(kwargs)


if __name__ == '__main__':
    cli()
