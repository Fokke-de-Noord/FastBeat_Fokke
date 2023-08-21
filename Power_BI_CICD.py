import requests



project_name = "Project_FastBeat"
headers = {"Authorization" : """Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTY0OTU1NDctNTM3ZS00ZGQwLTgxMzItZjJkYzYwZTFhODI1LyIsImlhdCI6MTY5MTM5NTM2MywibmJmIjoxNjkxMzk1MzYzLCJleHAiOjE2OTEzOTk4MjQsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVFFBeS84VUFBQUFZaWdBYkhiQUxseVpzY2xld21ZNFdxZUxOcmlEZ0ZuQndOcm1aREMrM2xjTDRIemJXcllrN1hWNE5WRm05UklIIiwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkRFIE5PT1JEIiwiZ2l2ZW5fbmFtZSI6IkZva2tlIiwiaXBhZGRyIjoiMmEwMjphNDQzOmNmMDoxOjVkMmI6YzVlODo5Y2U1OmVjZmYiLCJuYW1lIjoiRm9ra2UgREUgTk9PUkQiLCJvaWQiOiI3YjA1NWIyYy1mYjc3LTRhYzYtODYzMS1jNjM5NGQ5MTcyZTgiLCJwdWlkIjoiMTAwMzIwMDI0MjRGQTQ5NSIsInJoIjoiMC5BVHdBUjFWSkZuNVQwRTJCTXZMY1lPR29KUWtBQUFBQUFBQUF3QUFBQUFBQUFBQThBSHcuIiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgUGlwZWxpbmUuRGVwbG95IFBpcGVsaW5lLlJlYWQuQWxsIFBpcGVsaW5lLlJlYWRXcml0ZS5BbGwgUmVwb3J0LlJlYWQuQWxsIFJlcG9ydC5SZWFkV3JpdGUuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWQuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWRXcml0ZS5BbGwgVGVuYW50LlJlYWQuQWxsIFRlbmFudC5SZWFkV3JpdGUuQWxsIFVzZXJTdGF0ZS5SZWFkV3JpdGUuQWxsIFdvcmtzcGFjZS5SZWFkLkFsbCBXb3Jrc3BhY2UuUmVhZFdyaXRlLkFsbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6Ikw3OW5Md09uMTVuMWR3cWd5MmR3MVJYT001QVM3ZVBQSk52emRpOXoyNHciLCJ0aWQiOiIxNjQ5NTU0Ny01MzdlLTRkZDAtODEzMi1mMmRjNjBlMWE4MjUiLCJ1bmlxdWVfbmFtZSI6ImZva2tlLmRlLm5vb3JkQGRldm90ZWFtLmNvbSIsInVwbiI6ImZva2tlLmRlLm5vb3JkQGRldm90ZWFtLmNvbSIsInV0aSI6IlA2RkM1cElyTUVPQVlPSWs1dTR6QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.feDx-PFDP-joyun9X3Fald-Kc9-r7Hl5PfqVsSM66D-x3gqgvGqeR5zLIsVJ_4Yd-YS9oOA3eOtcLNhDCHS_BdSooAqzgFUg81JK9qUBpx3X_zWhqmb85YxKjKPbC56woZb83QtTzX9syHBmTblieTRylwEaUvYbSr_8zmepDIY0a34UDCfK9SoPWuDLV2GkvN0HqgsbBWw0OQI6iFmtv6Fc3pF3mprnCsGd3_MDmXNs6Yu6VLGL7dx5pEgAS9iWAs8PGM8chNjckuq9-M5nwCMmVfjGfsX0M0flVfvzze7ZLPBJl9yYlcz72YdFZxNGyqbfdSGpEH5KPUzuKFYeJg""",
           
           }




    



def make_workspaces(project_name):
    """
    Makes 3 workspaces in PowerBi with the names {project_name}_{environments}
    

    Arguments project_name  
    """
    url = f'https://api.powerbi.com/v1.0/myorg/groups'
    environments = ["Development", "Test", "Production"]
    workspace_names = [project_name + "_" + environment for environment in environments] 
    for workspace_name in workspace_names:
        url = f'https://api.powerbi.com/v1.0/myorg/groups?name={workspace_name}'
        data = {"name" : workspace_name}
        response = requests.post(url,headers=headers, json=data)
        print(response.status_code)

    
def make_pipeline(project_name, description=""):
    pipeline_name = project_name + "_" + "pipeline"
    url = f'https://api.powerbi.com/v1.0/myorg/pipelines?workspaceV2=True'
    data = {"displayName" : pipeline_name,
            'description' : description}
    response = requests.post(url,headers=headers, json=data)
    print(response.status_code)


def get_pipeline_id(project_name):
    pipeline_name = project_name + "_" + "pipeline"
    url = f'https://api.powerbi.com/v1.0/myorg/pipelines'
    response = requests.get(url,headers=headers)
    pipelines = response.json()["value"]
    for pipeline in pipelines:
        if pipeline["displayName"] == pipeline_name:
            pipeline_id = pipeline["id"]
    
    return pipeline_id

def get_workspace_id(project_name):
    url = f'https://api.powerbi.com/v1.0/myorg/groups'
    environments = ["Development", "Test", "Production"]
    workspace_names = [project_name + "_" + environment for environment in environments]
    list_workspace_id = []

    response = requests.get(url,headers=headers)
    workspaces = response.json()["value"]
    for workspace_name in workspace_names:
        for workspace in workspaces:
            if workspace["name"] == workspace_name:
                list_workspace_id.append(workspace["id"])
    
    return list_workspace_id

def assign_workspace_to_pipeline(pipeline_id, workspace_ids):
    for index, workspace_id in enumerate(workspace_ids):
        url = f'https://api.powerbi.com/v1.0/myorg/pipelines/{pipeline_id}/stages/{str(index)}/assignWorkspace'
        data = {"workspaceId" : workspace_id}
        response = requests.post(url,headers=headers, json=data)
        print(response.status_code)     

def get_capacitie_id():
    url = 'https://api.powerbi.com/v1.0/myorg/capacities'
    response = requests.get(url, headers=headers)
    capacities = response.json()["value"]
    for capacitie in capacities:
        if capacitie["displayName"] == 'Trial-fokke-de-noord-devoteam-com-06-20-2023-13-18-UTC':
            
            return capacitie["id"]

def assign_workspaces_to_capacity(workspace_ids, capacitie_id):
    for workspace_id in workspace_ids:
        url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/AssignToCapacity'
        data = {"capacityId" : capacitie_id }
        response = requests.post(url, headers=headers, json=data)
        print(response.status_code)

def delete_all(workspace_ids, pipeline_id):
    url = f'https://api.powerbi.com/v1.0/myorg/pipelines/{pipeline_id}'
    response = requests.delete(url, headers=headers)
    print(response.status_code)

    for workspace_id in workspace_ids:
        url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}'
        response = requests.delete(url, headers=headers)
        print(response.status_code)


make_workspaces(project_name)
make_pipeline(project_name)
assign_workspaces_to_capacity(get_workspace_id(project_name),get_capacitie_id())
assign_workspace_to_pipeline(get_pipeline_id(project_name),get_workspace_id(project_name))



#delete_all(get_workspace_id(project_name),get_pipeline_id(project_name))
