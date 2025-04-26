
import argparse 

def parse_args():
    parser = argparse.ArgumentParser(description='Interact with the pixela API')
    parser.add_argument('--token', required=True, help='Pixela token')
    parser.add_argument('--username', required=True, help='Pixela username')
    parser.add_argument('--graph_id', required=True, help='Pixela graph id')
    parser.add_argument('--create_user', action='store_true', help='Create pixela user')
    parser.add_argument('--create_graph', action='store_true', help='Create new graph')
    parser.add_argument('--graph_params', nargs='*', help='Graph parameters in key=value format')
    parser.add_argument('--post_pixel', nargs=2, help='Date and quantity of the pixel')
    parser.add_argument('--update_pixel', nargs=2, help='Date and quantity to update pixel')
    parser.add_argument('--delete_pixel', help='Date of pixel to be deleted')
    
    return parser.parse_args() 

 