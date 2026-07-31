# ⚕️ MedLookup — Busca de Medicamentos por Nome Científico

> Plataforma web médica que permite ao paciente ou profissional de saúde buscar um medicamento pelo **nome científico (DCI)** e obter todas as opções comerciais disponíveis no mercado brasileiro.

🔗 **Acesse o site:** [https://medlookup.onrender.com](https://medlookup.onrender.com)

---

## 📋 Sobre o Projeto

O MedLookup resolve um problema comum na prática clínica: receitas médicas e bulas utilizam a **Denominação Comum Internacional (DCI)** — o nome científico do princípio ativo — mas farmácias e pacientes conhecem apenas os **nomes comerciais** (ex: Tylenol, Novalgina, Prozac).

Com o MedLookup, basta digitar o nome científico para ver instantaneamente todas as marcas disponíveis, seus laboratórios e apresentações.

---

## ✨ Funcionalidades

- 🔍 **Busca inteligente** por nome científico com normalização de acentos e maiúsculas
- 💊 **25+ medicamentos** cadastrados com suas respectivas marcas comerciais
- 🏷️ **Destaque para genéricos** — identificados visualmente com tag própria
- ⚡ **Autocomplete** — sugestões enquanto você digita
- 🔗 **Aliases** — aceita variações do nome (ex: `metamizol` → dipirona, `acetaminofeno` → paracetamol)
- 🔎 **Busca parcial** — digitar parte do nome já retorna resultados
- 📱 **Design responsivo** — funciona em celular, tablet e desktop
- 🏥 **Visual médico profissional** com informações de categoria e indicação clínica

---

## 🖥️ Demonstração

### Tela inicial
Campo de busca com atalhos para os medicamentos mais consultados.

### Resultado de busca
Ao buscar `paracetamol`, o sistema retorna:

| Nome Comercial | Laboratório | Apresentação |
|---|---|---|
| Tylenol | Johnson & Johnson | Comprimidos 500mg / 750mg, Gotas, Xarope |
| Parador | EMS | Comprimidos 500mg / 750mg |
| Dôrico | Hypermarcas | Comprimidos 500mg, Gotas |
| Cibalena | GSK | Comprimidos 500mg |
| Paracetamol Genérico | Vários | Comprimidos 500mg / 750mg, Gotas |

---

## 🗂️ Medicamentos Disponíveis

| Nome Científico | Categoria | Indicação |
|---|---|---|
| Paracetamol | Analgésico / Antipirético | Dor e febre |
| Ibuprofeno | Anti-inflamatório / Analgésico | Dor, inflamação e febre |
| Dipirona (Metamizol) | Analgésico / Antipirético | Dor e febre |
| Amoxicilina | Antibiótico | Infecções bacterianas |
| Azitromicina | Antibiótico | Infecções respiratórias |
| Omeprazol | Inibidor de Bomba de Prótons | Refluxo e gastrite |
| Esomeprazol | Inibidor de Bomba de Prótons | Refluxo gastroesofágico |
| Metformina | Antidiabético | Diabetes tipo 2 |
| Losartana | Anti-hipertensivo | Hipertensão arterial |
| Atenolol | Betabloqueador | Hipertensão e arritmias |
| Amlodipino | Bloqueador de Canal de Cálcio | Hipertensão e angina |
| Captopril | Inibidor da ECA | Hipertensão arterial |
| Enalapril | Inibidor da ECA | Hipertensão arterial |
| Sinvastatina | Estatina | Colesterol alto |
| Clopidogrel | Antiagregante Plaquetário | Prevenção de trombose |
| Ácido Acetilsalicílico | Antiagregante / AINE | Dor e prevenção cardiovascular |
| Levotiroxina | Hormônio Tireoidiano | Hipotireoidismo |
| Prednisona | Corticosteroide | Inflamações e alergias graves |
| Clonazepam | Benzodiazepínico | Epilepsia e ansiedade |
| Sertralina | Antidepressivo (ISRS) | Depressão e ansiedade |
| Fluoxetina | Antidepressivo (ISRS) | Depressão e TOC |
| Cetirizina | Anti-histamínico | Alergias e rinite |
| Loratadina | Anti-histamínico | Alergias e rinite |
| Tramadol | Analgésico Opioide | Dor moderada a intensa |
| Diclofenaco | Anti-inflamatório (AINE) | Dor e artrite |

---

## 🛠️ Tecnologias Utilizadas

**Backend**
- [Python 3](https://python.org) — linguagem principal
- [Flask 3](https://flask.palletsprojects.com) — framework web
- [Flask-CORS](https://flask-cors.readthedocs.io) — suporte a requisições cross-origin
- [Gunicorn](https://gunicorn.org) — servidor WSGI para produção

**Frontend**
- HTML5 semântico
- CSS3 com variáveis, Grid e Flexbox
- JavaScript vanilla (sem dependências externas)
- Google Fonts (Inter)

**Deploy**
- [Render](https://render.com) — hospedagem gratuita
- [GitHub](https://github.com) — controle de versão

---

## 📁 Estrutura do Projeto

```
med_lookup/
├── app.py              # Backend Flask — rotas e lógica da API
├── med_data.py         # Base de dados de medicamentos e aliases
├── static/
│   ├── index.html      # Interface do usuário
│   ├── styles.css      # Estilos e design
│   └── app.js          # Lógica do frontend
├── requirements.txt    # Dependências Python
├── Procfile            # Comando de inicialização (Render/Heroku)
├── render.yaml         # Configuração de deploy no Render
└── .gitignore
```

---

## 🚀 Como Rodar Localmente

**Pré-requisitos:** Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/monica1602/medlookup.git
cd medlookup

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o servidor
python app.py

# 4. Acesse no navegador
# http://localhost:5000
```

No Windows, você também pode dar **duplo clique** no arquivo `iniciar.bat` — ele inicia o servidor e abre o navegador automaticamente.

---

## 🔌 API

O backend expõe duas rotas REST:

### `GET /api/buscar?q={nome}`
Busca um medicamento pelo nome científico.

**Exemplo:**
```
GET /api/buscar?q=paracetamol
```

**Resposta:**
```json
{
  "nome_cientifico": "Paracetamol",
  "categoria": "Analgésico / Antipirético",
  "indicacao": "Dor e febre",
  "total": 5,
  "marcas": [
    {
      "nome": "Tylenol",
      "laboratorio": "Johnson & Johnson",
      "apresentacao": "Comprimidos 500mg / 750mg, Gotas, Xarope"
    }
  ]
}
```

### `GET /api/lista`
Retorna todos os medicamentos disponíveis (usado para autocomplete).

```json
{
  "medicamentos": ["Amoxicilina", "Atenolol", "..."],
  "total": 25
}
```

---

## ⚠️ Aviso Legal

Este site tem caráter **exclusivamente informativo e educacional**. As informações sobre medicamentos e marcas comerciais não substituem a orientação de um médico ou farmacêutico. Sempre consulte um profissional de saúde antes de tomar qualquer medicamento.

---

## 👩‍💻 Autora

Desenvolvido por **Monica** · [github.com/monica1602](https://github.com/monica1602)

---

<p align="center">Feito com ❤️ para facilitar o acesso à informação em saúde</p>
