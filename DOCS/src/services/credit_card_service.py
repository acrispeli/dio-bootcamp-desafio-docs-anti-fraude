from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from ultils.Config import Config

def analize_credit_card(card_url):
    credential = AzureKeyCredential(Config.KEY)
    document_Client = DocumentAnalysisClient(endpoint=Config.ENDPOINT, credential=credential, api_version="2023-07-31")

    try:
        # Verificar a URL da imagem
        print(f"Verificando a URL da imagem: {card_url}")

        # Usar o modelo `prebuilt-receipt`
        poller = document_Client.begin_analyze_document_from_url(
            model_id="prebuilt-receipt", document_url=card_url)
        
        result = poller.result()  # Aguarde o resultado
        
        if not result.documents:
            print("Nenhum documento encontrado na resposta.")
            return None

        for document in result.documents:
            fields = document.fields
            print("Campos retornados:", fields)

            # Extrair informações específicas do campo `content`
            content = result.content
            card_info = {
                "card_name": None,
                "card_number": None,
                "expiry_date": None,
                "bank_name": None,
            }

            # Analisando as linhas do texto extraído
            lines = content.split('\n')
            for line in lines:
                if "PagBank" in line:
                    card_info["bank_name"] = line
                if any(char.isdigit() for char in line) and len(line.replace(' ', '')) >= 16:
                    card_info["card_number"] = line.strip()
                if "/" in line and len(line.strip()) == 5:
                    card_info["expiry_date"] = line.strip()
                if "RODRIGO" in line:  # Exemplo de como ajustar para outros nomes
                    card_info["card_name"] = line.strip()

            print("Informações do cartão extraídas:", card_info)
            return card_info
    
    except Exception as e:
        print("Erro durante a análise do documento:", str(e))
        return None

# Exemplo de uso
analize_credit_card("https://stdiolabdocsdev001.blob.core.windows.net/cartoes/visa1.jpg")
