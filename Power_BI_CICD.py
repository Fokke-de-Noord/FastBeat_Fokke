import requests



project_name = "Project_FastBeat"
headers = {"Authorization" : """""",
           
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
