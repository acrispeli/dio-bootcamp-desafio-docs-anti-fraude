from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from ultils.Config import Config

def test_connection():
    try:
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentAnalysisClient(endpoint=Config.ENDPOINT, credential=credential)
        
        # Chamada de teste para obter o status do modelo
        model_id = "prebuilt-receipt"  # Usar um modelo pré-construído para teste
        poller = document_client.begin_analyze_document_from_url(
            model_id=model_id,
            document_url="https://stdiolabdocsdev001.blob.core.windows.net/cartoes/visa1.jpg"
        )
        result = poller.result()
        print("Conexão bem-sucedida e análise realizada com sucesso!")
        print("Resultado da análise:", result.to_dict())
    
    except Exception as e:
        print("Erro durante a conexão ou análise:", str(e))

if __name__ == "__main__":
    test_connection()
