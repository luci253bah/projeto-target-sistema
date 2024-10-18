import xml.etree.ElementTree as ET

def analisar_faturamento_mensal(faturamento_diario):

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    media_mensal = sum(faturamento_diario) / len( faturamento_diario )

    dias_acima_da_media =  sum(1 for valor in faturamento_diario if valor >media_mensal)

    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

    root = ET.Element("FaturamentoMensal")

    menor_elemento = ET.SubElement(root, "MenorFaturamento")
    menor_elemento.text = str(menor_faturamento)

    maior_elemento = ET.SubElement(root, "MaiorFaturamento")
    maior_elemento.text = str(maior_faturamento)

    dias_acima_media_elemento = ET.SubElement(root, "DiasAcimaMedia")
    dias_acima_media_elemento.text = str(dias_acima_da_media)

    tree = ET.ElementTree(root)
    tree.write("faturamento.xml", encoding="utf-8", xml_declaration=True)

    print("Arquivo XML gerado com sucesso!")
