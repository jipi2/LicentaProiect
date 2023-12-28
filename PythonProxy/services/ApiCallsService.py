import httpx

class ApiCall():
    def __init__(self, baseUrl:str):
        self.api_url = baseUrl
    
    async def callBackendPostMethodDto(self, endPointName:str, token: str, param):
        if token != "":
            headers = {"Authorization": f"Bearer {token}"}
        else:
            headers = {} 
        json = param.model_dump()
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(self.api_url+endPointName, headers=headers, json=json)
        return response
    
    async def call_backend(self, endPointName:str, token:str, dtoParam):
        if token != "":
            headers = {"Authorization": f"Bearer {token}"}
        else:
            headers = {}
        params = dtoParam.model_dump()  
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(self.api_url+endPointName, headers=headers, json=params)
        return response
    
    async def callBackendGetMethod(self,endPointName:str, token:str):
        headers = {"Authorization": f"Bearer {token}"}
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(self.api_url+endPointName, headers=headers)
            return response
    
    