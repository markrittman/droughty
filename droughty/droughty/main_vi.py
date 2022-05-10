from droughty.lookml_cli import base 
#from droughty import dbt_test_cli
#from droughty import dbml_cli
#from droughty import cube_cli
from droughty.config_cli import profile_parser#,argument_profile

##app.add_typer(dbt_test_cli.app, name="dbt")
##app.add_typer(dbml_cli.app, name="dbml")
##app.add_typer(cube_cli.app, name="cube")

##app.add_typer(config_cli.app)

#####

import argparse

def some_function(profile_dir):
    """Some example funcion"""
    msg = profile_dir
    print(msg)



def start():
    # All the logic of argparse goes in this function

    parser = argparse.ArgumentParser(description='Say hi.')
    #parser.add_argument('--profile-dir', type=str, help='the directory of the profile')
    #parser.add_argument('--profile-dir-test', type=str, help='the directory of the profile')

    parser.add_argument('--end', dest='end', default="!",
                    help='sum the integers (default: find the max)')

    args = profile_parser.parse_args()

    some_function(args.profile_dir)

    #base(args.profile_dir)

    #argument_profile(args.profile_dir)
    base()

    foo = (args.profile_dir)

    sub_parsers = parser.add_subparsers(help='sub-command help')

    # create the parser for the "ahoy" sub-command
    parser_ahoy = sub_parsers.add_parser('lookml', help='lookml is cool sub-command')
    parser_ahoy.add_argument('--bar', type=int, help='bar is useful option')


if __name__ == '__main__':
    start()