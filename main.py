#!/usr/bin/env python3 

from habit_args import parse_args
from habit_class import HabitTracker

def main():
    
    args = parse_args()
    
    instance = HabitTracker(args.token, args.username, args.graph_id) 

    if args.create_user:
        instance.create_user() 
    
    graph_kwargs = {}
    if args.graph_params:
        for item in args.graph_params:
            if '=' in item:
                key, value = item.split('=', 1)
                graph_kwargs[key] = value
        instance.create_graph(**graph_kwargs)
    
    if args.post_pixel:
        instance.post_pixel(args.post_pixel[0], args.post_pixel[1])
    
    if args.update_pixel:
        instance.update_pixel(args.update_pixel[0], args.update_pixel[1])
    
    if args.delete_pixel:
        instance.delete_pixel(args.delete_pixel)
        
if __name__ == '__main__':
    main() 
    
    