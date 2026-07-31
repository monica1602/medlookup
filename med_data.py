# Base de dados de medicamentos: nome científico → opções comerciais no mercado brasileiro
# Estrutura: { "nome_cientifico": { "categoria": str, "indicacao": str, "marcas": [ { "nome": str, "laboratorio": str, "apresentacao": str } ] } }

MEDICAMENTOS = {
    "paracetamol": {
        "categoria": "Analgésico / Antipirético",
        "indicacao": "Dor e febre",
        "marcas": [
            {"nome": "Tylenol", "laboratorio": "Johnson & Johnson", "apresentacao": "Comprimidos 500mg / 750mg, Gotas, Xarope"},
            {"nome": "Parador", "laboratorio": "EMS", "apresentacao": "Comprimidos 500mg / 750mg"},
            {"nome": "Dôrico", "laboratorio": "Hypermarcas", "apresentacao": "Comprimidos 500mg, Gotas"},
            {"nome": "Cibalena", "laboratorio": "GSK", "apresentacao": "Comprimidos 500mg"},
            {"nome": "Paracetamol Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 500mg / 750mg, Gotas"},
        ]
    },
    "ibuprofeno": {
        "categoria": "Anti-inflamatório / Analgésico",
        "indicacao": "Dor, inflamação e febre",
        "marcas": [
            {"nome": "Advil", "laboratorio": "Pfizer", "apresentacao": "Comprimidos 200mg / 400mg, Gel"},
            {"nome": "Alivium", "laboratorio": "Hypermarcas", "apresentacao": "Comprimidos 200mg / 400mg / 600mg"},
            {"nome": "Ibupril", "laboratorio": "Marjan", "apresentacao": "Comprimidos 300mg / 600mg"},
            {"nome": "Buscofem", "laboratorio": "GSK", "apresentacao": "Comprimidos 400mg"},
            {"nome": "Ibuprofeno Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 200mg / 400mg / 600mg"},
        ]
    },
    "amoxicilina": {
        "categoria": "Antibiótico (Penicilina)",
        "indicacao": "Infecções bacterianas",
        "marcas": [
            {"nome": "Amoxil", "laboratorio": "GSK", "apresentacao": "Cápsulas 500mg, Suspensão 250mg/5ml"},
            {"nome": "Novamox", "laboratorio": "Novartis", "apresentacao": "Cápsulas 500mg, Suspensão"},
            {"nome": "Flemoxin", "laboratorio": "Astellas", "apresentacao": "Comprimidos dispersíveis 500mg / 1g"},
            {"nome": "Amoxicilina Genérica", "laboratorio": "Vários", "apresentacao": "Cápsulas 500mg, Suspensão"},
        ]
    },
    "azitromicina": {
        "categoria": "Antibiótico (Macrolídeo)",
        "indicacao": "Infecções respiratórias, de pele e ISTs",
        "marcas": [
            {"nome": "Zithromax", "laboratorio": "Pfizer", "apresentacao": "Comprimidos 500mg, Suspensão"},
            {"nome": "Azitromicina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 500mg"},
            {"nome": "Clindal", "laboratorio": "EMS", "apresentacao": "Comprimidos 500mg"},
            {"nome": "Azi-Once", "laboratorio": "Eurofarma", "apresentacao": "Comprimidos 500mg"},
        ]
    },
    "atenolol": {
        "categoria": "Betabloqueador",
        "indicacao": "Hipertensão, angina e arritmias",
        "marcas": [
            {"nome": "Atenol", "laboratorio": "EMS", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
            {"nome": "Tenormin", "laboratorio": "AstraZeneca", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
            {"nome": "Atenolol Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
        ]
    },
    "losartana": {
        "categoria": "Anti-hipertensivo (BRA)",
        "indicacao": "Hipertensão arterial e insuficiência cardíaca",
        "marcas": [
            {"nome": "Cozaar", "laboratorio": "MSD", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
            {"nome": "Losartana Potássica Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
            {"nome": "Aradois", "laboratorio": "Hypermarcas", "apresentacao": "Comprimidos 50mg / 100mg"},
        ]
    },
    "metformina": {
        "categoria": "Antidiabético (Biguanida)",
        "indicacao": "Diabetes tipo 2",
        "marcas": [
            {"nome": "Glifage", "laboratorio": "Merck", "apresentacao": "Comprimidos 500mg / 850mg / 1g"},
            {"nome": "Glucoformin", "laboratorio": "EMS", "apresentacao": "Comprimidos 500mg / 850mg"},
            {"nome": "Metformina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 500mg / 850mg / 1g"},
            {"nome": "Dimefor", "laboratorio": "Zambon", "apresentacao": "Comprimidos 850mg / 1g"},
        ]
    },
    "omeprazol": {
        "categoria": "Inibidor de Bomba de Prótons",
        "indicacao": "Úlcera, refluxo gastroesofágico e gastrite",
        "marcas": [
            {"nome": "Losec", "laboratorio": "AstraZeneca", "apresentacao": "Cápsulas 10mg / 20mg / 40mg"},
            {"nome": "Peprazol", "laboratorio": "EMS", "apresentacao": "Cápsulas 20mg / 40mg"},
            {"nome": "Mepral", "laboratorio": "Eurofarma", "apresentacao": "Cápsulas 20mg / 40mg"},
            {"nome": "Omeprazol Genérico", "laboratorio": "Vários", "apresentacao": "Cápsulas 10mg / 20mg / 40mg"},
        ]
    },
    "sinvastatina": {
        "categoria": "Hipolipemiante (Estatina)",
        "indicacao": "Colesterol alto e prevenção cardiovascular",
        "marcas": [
            {"nome": "Zocor", "laboratorio": "MSD", "apresentacao": "Comprimidos 10mg / 20mg / 40mg"},
            {"nome": "Sinvastacor", "laboratorio": "EMS", "apresentacao": "Comprimidos 10mg / 20mg / 40mg"},
            {"nome": "Sinvastatina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 10mg / 20mg / 40mg"},
        ]
    },
    "clonazepam": {
        "categoria": "Benzodiazepínico",
        "indicacao": "Epilepsia, ansiedade e transtorno do pânico",
        "marcas": [
            {"nome": "Rivotril", "laboratorio": "Roche", "apresentacao": "Comprimidos 0,5mg / 2mg, Gotas"},
            {"nome": "Clonazepam Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 0,5mg / 2mg"},
        ]
    },
    "sertralina": {
        "categoria": "Antidepressivo (ISRS)",
        "indicacao": "Depressão, TOC, ansiedade e TEPT",
        "marcas": [
            {"nome": "Zoloft", "laboratorio": "Pfizer", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
            {"nome": "Assert", "laboratorio": "EMS", "apresentacao": "Comprimidos 50mg / 100mg"},
            {"nome": "Sertralina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 25mg / 50mg / 100mg"},
        ]
    },
    "fluoxetina": {
        "categoria": "Antidepressivo (ISRS)",
        "indicacao": "Depressão, bulimia e transtorno obsessivo-compulsivo",
        "marcas": [
            {"nome": "Prozac", "laboratorio": "Eli Lilly", "apresentacao": "Cápsulas 20mg / 40mg"},
            {"nome": "Daforin", "laboratorio": "EMS", "apresentacao": "Cápsulas 20mg"},
            {"nome": "Fluoxetina Genérica", "laboratorio": "Vários", "apresentacao": "Cápsulas 10mg / 20mg / 40mg"},
        ]
    },
    "diclofenaco": {
        "categoria": "Anti-inflamatório não esteroidal (AINE)",
        "indicacao": "Dor, inflamação e artrite",
        "marcas": [
            {"nome": "Voltaren", "laboratorio": "Novartis", "apresentacao": "Comprimidos 50mg, Gel, Injetável"},
            {"nome": "Cataflan", "laboratorio": "Novartis", "apresentacao": "Comprimidos 50mg"},
            {"nome": "Diclofenaco Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 25mg / 50mg, Gel"},
        ]
    },
    "cetirizina": {
        "categoria": "Anti-histamínico (2ª geração)",
        "indicacao": "Alergias, rinite e urticária",
        "marcas": [
            {"nome": "Zyrtec", "laboratorio": "UCB", "apresentacao": "Comprimidos 10mg, Solução oral"},
            {"nome": "Reactine", "laboratorio": "Pfizer", "apresentacao": "Comprimidos 10mg"},
            {"nome": "Cetirizina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 10mg, Solução oral"},
        ]
    },
    "loratadina": {
        "categoria": "Anti-histamínico (2ª geração)",
        "indicacao": "Alergias e rinite alérgica",
        "marcas": [
            {"nome": "Claritin", "laboratorio": "MSD", "apresentacao": "Comprimidos 10mg, Xarope"},
            {"nome": "Histadin", "laboratorio": "EMS", "apresentacao": "Comprimidos 10mg, Xarope"},
            {"nome": "Loradin", "laboratorio": "Hypermarcas", "apresentacao": "Comprimidos 10mg"},
            {"nome": "Loratadina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 10mg, Xarope"},
        ]
    },
    "amlodipinobessilato": {
        "categoria": "Bloqueador de Canal de Cálcio",
        "indicacao": "Hipertensão arterial e angina",
        "marcas": [
            {"nome": "Norvasc", "laboratorio": "Pfizer", "apresentacao": "Comprimidos 5mg / 10mg"},
            {"nome": "Amlogard", "laboratorio": "EMS", "apresentacao": "Comprimidos 5mg / 10mg"},
            {"nome": "Amlodipino Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 5mg / 10mg"},
        ]
    },
    "levotiroxina": {
        "categoria": "Hormônio Tireoidiano",
        "indicacao": "Hipotireoidismo",
        "marcas": [
            {"nome": "Puran T4", "laboratorio": "Abbott", "apresentacao": "Comprimidos 25mcg / 50mcg / 75mcg / 100mcg / 125mcg / 150mcg"},
            {"nome": "Euthyrox", "laboratorio": "Merck", "apresentacao": "Comprimidos 25mcg / 50mcg / 100mcg"},
            {"nome": "Levotiroxina Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 25mcg a 200mcg"},
        ]
    },
    "prednisona": {
        "categoria": "Corticosteroide",
        "indicacao": "Inflamações, alergias graves e doenças autoimunes",
        "marcas": [
            {"nome": "Meticorten", "laboratorio": "MSD", "apresentacao": "Comprimidos 5mg / 20mg"},
            {"nome": "Predsin", "laboratorio": "EMS", "apresentacao": "Comprimidos 5mg / 20mg"},
            {"nome": "Prednisona Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 5mg / 20mg"},
        ]
    },
    "captopril": {
        "categoria": "Inibidor da ECA",
        "indicacao": "Hipertensão arterial e insuficiência cardíaca",
        "marcas": [
            {"nome": "Capoten", "laboratorio": "Bristol-Myers Squibb", "apresentacao": "Comprimidos 12,5mg / 25mg / 50mg"},
            {"nome": "Captopril Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 12,5mg / 25mg / 50mg"},
        ]
    },
    "enalapril": {
        "categoria": "Inibidor da ECA",
        "indicacao": "Hipertensão arterial e insuficiência cardíaca",
        "marcas": [
            {"nome": "Renitec", "laboratorio": "MSD", "apresentacao": "Comprimidos 5mg / 10mg / 20mg"},
            {"nome": "Eupressin", "laboratorio": "EMS", "apresentacao": "Comprimidos 5mg / 10mg / 20mg"},
            {"nome": "Enalapril Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 5mg / 10mg / 20mg"},
        ]
    },
    "tramadol": {
        "categoria": "Analgésico Opioide",
        "indicacao": "Dor moderada a intensa",
        "marcas": [
            {"nome": "Tramal", "laboratorio": "Pfizer", "apresentacao": "Cápsulas 50mg, Gotas, Injetável"},
            {"nome": "Cronidor", "laboratorio": "EMS", "apresentacao": "Cápsulas 50mg / 100mg (liberação prolongada)"},
            {"nome": "Tramadol Genérico", "laboratorio": "Vários", "apresentacao": "Cápsulas 50mg, Gotas"},
        ]
    },
    "esomeprazol": {
        "categoria": "Inibidor de Bomba de Prótons",
        "indicacao": "Refluxo gastroesofágico e úlcera péptica",
        "marcas": [
            {"nome": "Nexium", "laboratorio": "AstraZeneca", "apresentacao": "Comprimidos 20mg / 40mg"},
            {"nome": "Esomeprazol Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 20mg / 40mg"},
        ]
    },
    "clopidogrel": {
        "categoria": "Antiagregante Plaquetário",
        "indicacao": "Prevenção de trombose e AVC",
        "marcas": [
            {"nome": "Plavix", "laboratorio": "Sanofi", "apresentacao": "Comprimidos 75mg"},
            {"nome": "Iscover", "laboratorio": "BMS", "apresentacao": "Comprimidos 75mg"},
            {"nome": "Clopidogrel Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 75mg"},
        ]
    },
    "acido acetilsalicilico": {
        "categoria": "Antiagregante / Anti-inflamatório / Antipirético",
        "indicacao": "Dor leve, febre, prevenção cardiovascular",
        "marcas": [
            {"nome": "Aspirina", "laboratorio": "Bayer", "apresentacao": "Comprimidos 100mg / 500mg"},
            {"nome": "AAS", "laboratorio": "Bayer", "apresentacao": "Comprimidos 100mg (uso cardiovascular)"},
            {"nome": "Melhoral", "laboratorio": "Hypermarcas", "apresentacao": "Comprimidos 500mg"},
            {"nome": "Ácido Acetilsalicílico Genérico", "laboratorio": "Vários", "apresentacao": "Comprimidos 100mg / 500mg"},
        ]
    },
    "dipirona": {
        "categoria": "Analgésico / Antipirético",
        "indicacao": "Dor e febre",
        "marcas": [
            {"nome": "Novalgina", "laboratorio": "Sanofi", "apresentacao": "Comprimidos 500mg / 1g, Gotas, Injetável"},
            {"nome": "Anador", "laboratorio": "EMS", "apresentacao": "Comprimidos 500mg, Gotas"},
            {"nome": "Baralgin", "laboratorio": "Sanofi", "apresentacao": "Injetável 2,5g/5ml"},
            {"nome": "Dipirona Genérica", "laboratorio": "Vários", "apresentacao": "Comprimidos 500mg, Gotas"},
        ]
    },
}

# Aliases: variações de nomes para facilitar a busca
ALIASES = {
    "metamizol": "dipirona",
    "metamizole": "dipirona",
    "acetaminofeno": "paracetamol",
    "acetaminophen": "paracetamol",
    "acido acetilsalicilico": "acido acetilsalicilico",
    "aspirina": "acido acetilsalicilico",
    "asa": "acido acetilsalicilico",
    "amlodipino": "amlodipinobessilato",
    "amlodipina": "amlodipinobessilato",
}
