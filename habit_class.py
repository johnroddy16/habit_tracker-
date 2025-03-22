#!/usr/bin/env python3 

# habit tracker class:

import requests 

class HabitTracker:
    # constructor:
    def __init__(self, token, username, graph_id):
        self.token = token 
        self.username = username 
        self.graph_id = graph_id 
        self.pixela_endpoint = 'https://pixe.la/v1/users'
        self.headers = {'X-USER-TOKEN': token}
    
    # create the user:    
    def create_user(self):
        params = {
            'token': self.token,
            'username': self.username,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes', 
        }
        
        response = requests.post(url=self.pixela_endpoint, json=params) 
        print(response.text) 
     
    # create the graph:   
    def create_graph(self, name, unit, type, color, timezone):
        params = {
            'id': self.graph_id,
            'name': name, 
            'unit': unit,  
            'type': type, 
            'color': color,
            'timezone': timezone 
        }
        
        graph_endpoint = f'{self.pixela_endpoint}/{self.username}/graphs'
        
        response = requests.post(url=graph_endpoint, json=params, headers=self.headers)
        print(response.text)
        
    # post a pixel:
    def post_pixel(self, date, quantity):
        params = {
            'date': date, 
            'quantity': quantity 
        }
        
        pixel_post_endpoint = f'{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}'
        
        response = requests.post(url=pixel_post_endpoint, json=params, headers=self.headers)
        print(response.text) 
        
    # update a pixel:
    def update_pixel(self, date, quantity):
        params = {
            'quantity': quantity 
        } 
        
        pixel_update_endpoint = f'{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/{date}'
        
        response = requests.put(url=pixel_update_endpoint, json=params, headers=self.headers)
        print(response.text) 
        
    # delete a pixel:
    def delete_pixel(self, date):
        pixel_delete_endpoint = f'{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/{date}'
        
        response = requests.delete(url=pixel_delete_endpoint, headers=self.headers)
        print(response.text)    
        
        
        
    