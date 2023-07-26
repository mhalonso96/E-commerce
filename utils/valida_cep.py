import zeep

def consulta_cep(cep):
    try: 
        wsdl = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
        client = zeep.Client(wsdl=wsdl)
        res = client.service.consultaCEP(cep)   
        return res
                
    except Exception as error:
        return False   
    
